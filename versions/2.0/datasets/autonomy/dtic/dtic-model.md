## dtic-sample.json

### PyTransforms
#### _author_uri_
From column: _personal_author / values_
>``` python
return author_uri_dtic(getValue("values"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _abstract_ | `schema:text` | `schema:ScholarlyArticle1`|
| _author_uri_ | `uri` | `schema:Person1`|
| _title_ | `schema:name` | `schema:ScholarlyArticle1`|
| _values_ | `schema:name` | `schema:Person1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Person1` | `memex:isAuthorOf` | `schema:ScholarlyArticle1`|
| `schema:ScholarlyArticle1` | `schema:author` | `schema:Person1`|
