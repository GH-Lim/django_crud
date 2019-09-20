```python
>>> article = Article()
>>> article.title = '새로운 데이터'
>>> article.content = '새로운 내용'
>>> article.save()
>>> article
<Article: Article object (16)>
>>> comment = Comment()
>>> comment.content = 'First comment'
>>> comment.article = article
>>> comment.article_id = article.pk
>>> comment.save()
>>> comment
<Comment: First comment>
>>> comment.article
<Article: Article object (16)>
>>> comment.article_id
16
>>> comment.article_pk
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Comment' object has no attribute 'article_pk'
# 이런식으로 접근이 가능하다.
>>> comment.article.pk
16
>>> comment.article.content
'새로운 내용'
>>> comment.article.title
'새로운 데이터'
>>> comment = Comment(article=article, content='Second comment')
>>> comment.save()
>>> comment.pk
2
>>> comment.content
'Second comment'
>>> comment.article
<Article: Article object (16)>
>>> dir(article)
['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table', '_set_pk_val', '_state', 'check', 'clean', 'clean_fields', 'comment_set', 'content', 'created_at', 'date_error_message', 'delete', 'from_db', 'full_clean', 'get_deferred_fields', 'get_next_by_created_at', 'get_next_by_updated_at', 'get_previous_by_created_at', 'get_previous_by_updated_at', 'id', 'objects', 'pk', 'prepare_database_save', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'title',
'unique_error_message', 'updated_at', 'validate_unique']
>>> dir(article.comment_set)
['__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', '__str__', '__subclasshook__', '__weakref__', '_apply_rel_filters', '_constructor_args', '_db', '_get_queryset_methods', '_hints', '_insert', '_queryset_class', '_remove_prefetched_objects', '_set_creation_counter', '_update', 'add', 'aggregate', 'all', 'annotate', 'auto_created', 'bulk_create', 'bulk_update', 'check', 'complex_filter', 'contribute_to_class', 'core_filters', 'count', 'create', 'creation_counter', 'dates', 'datetimes', 'db', 'db_manager', 'deconstruct', 'defer', 'difference', 'distinct', 'do_not_call_in_templates', 'earliest', 'exclude', 'exists', 'explain', 'extra', 'field', 'filter', 'first', 'from_queryset', 'get', 'get_or_create', 'get_prefetch_queryset', 'get_queryset', 'in_bulk', 'instance', 'intersection', 'iterator', 'last', 'latest', 'model', 'name', 'none', 'only', 'order_by', 'prefetch_related', 'raw', 'reverse', 'select_for_update', 'select_related', 'set', 'union', 'update', 'update_or_create', 'use_in_migrations', 'using', 'values', 'values_list']

```

```bash
$ pip install ipython
```



```python
In [2]: article = Article.objects.get(pk=16)

In [3]: article
Out[3]: <Article: Article object (16)>

In [4]: dir(article.comment_set)
Out[4]: 
['__call__',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__slotnames__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_apply_rel_filters',
 '_constructor_args',
 '_db',
 '_get_queryset_methods',
 '_hints',
 '_insert',
 '_queryset_class',
 '_remove_prefetched_objects',
 '_set_creation_counter',
 '_update',
 'add',
 'aggregate',
 'all',
 'annotate',
 'auto_created',
 'bulk_create',
 'bulk_update',
 'check',
 'complex_filter',
 'contribute_to_class',
 'core_filters',
 'count',
 'create',
 'creation_counter',
 'dates',
 'datetimes',
 'db',
 'db_manager',
 'deconstruct',
 'defer',
 'difference',
 'distinct',
 'do_not_call_in_templates',
 'earliest',
 'exclude',
 'exists',
 'explain',
 'extra',
 'field',
 'filter',
 'first',
 'from_queryset',
 'get',
 'get_or_create',
 'get_prefetch_queryset',
 'get_queryset',
 'in_bulk',
 'instance',
 'intersection',
 'iterator',
 'last',
 'latest',
 'model',
 'name',
 'none',
 'only',
 'order_by',
 'prefetch_related',
 'raw',
 'reverse',
 'select_for_update',
 'select_related',
 'set',
 'union',
 'update',
 'update_or_create',
 'use_in_migrations',
 'using',
 'values',
 'values_list']

In [5]: comments = article.comment_set.all()

In [6]: comments
Out[6]: <QuerySet [<Comment: Second comment>, <Comment: First comment>]>

In [7]: article.comment_set.get(pk=1)
Out[7]: <Comment: First comment>

In [8]: article.comment_set.filter(content='Second comment')
Out[8]: <QuerySet [<Comment: Second comment>]>

In [9]: article.comment_set.filter(content='Second comment').first()
Out[9]: <Comment: Second comment>
```

