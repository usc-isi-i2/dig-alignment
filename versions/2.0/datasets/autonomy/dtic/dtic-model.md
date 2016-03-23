## dtic-sample.json

### PyTransforms
#### _author_uri_
From column: _personal_author / values_
>``` python
return author_uri_dtic(getValue("values"))
```

#### _author_name_normalized_
From column: _personal_author / values_
>``` python
return jp_author_name_normalized(getValue("values"))
```

#### _article_uri_
From column: _title_
>``` python
return dtic_article_uri(getValue("title"), getValue("abstract"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _abstract_ | `schema:text` | `schema:ScholarlyArticle1`|
| _article_uri_ | `uri` | `schema:ScholarlyArticle1`|
| _author_name_normalized_ | `schema:name` | `schema:Person1`|
| _author_uri_ | `uri` | `schema:Person1`|
| _title_ | `schema:name` | `schema:ScholarlyArticle1`|
| _values_ | `schema:alternateName` | `schema:Person1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Person1` | `memex:isAuthorOf` | `schema:ScholarlyArticle1`|
| `schema:ScholarlyArticle1` | `schema:author` | `schema:Person1`|
