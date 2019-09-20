from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from faker import Faker
from pprint import pprint
import requests
API_KEY = 'agreR7FrrGl3BzOjmUjBhjBxkOaM47Ie'

def index(request):
    return render(request, 'jobs/index.html')
def past_job(request):
    jobs = Job.objects.all()
    name = request.POST.get('name')
    if jobs.filter(name=name):
        job = Job.objects.get(name=name)
    else:
        fake = Faker('ko_KR')
        job = Job(name=name, past_job=fake.job())
        job.save()
    headers = {
        'X-Naver-Client-Id': 'OFFvuywu7KRvDVTPGMcB',
        'X-Naver-Client-Secret': 'vhTpNn8htW',   # , 있는걸 추천 컨벤션 추가할때 혹시라도 오류가 생길까봐
    }                                                   # trailing comma
    data = {
        'source': 'ko',
        'target': 'en',
        'text': job.past_job,   # '/번역 ' 이후의 문자열만 대상으로 번역
    }
    papago_url = 'https://openapi.naver.com/v1/papago/n2mt'
    papago_res = requests.post(papago_url, headers=headers, data=data)
    text = papago_res.json().get('message').get('result').get('translatedText')
    print(text)
    URL = f'https://api.giphy.com/v1/gifs/search?api_key={API_KEY}&q={text}&limit=1/'
    data = requests.get(URL).json()
    url = data.get('data')[0].get('images').get('downsized').get('url')
    pprint(url)

    # headers = {
    #     'X-Naver-Client-Id': 'rnQHMbdiCjf0k3vUT6v1',
    #     'X-Naver-Client-Secret': 'LNX3UpYZqC',
    # }
    # image_url = 'https://openapi.naver.com/v1/search/image?query={job.past_job}&display=10&start=1/'
    # image_res = requests.get(image_url, headers=headers)
    # url = image_res.json().get('items')[0].get('link')
    # pprint(url)
    context = {
        'job': job,
        'url': url,
    }
    return render(request, 'jobs/past_job.html', context)
