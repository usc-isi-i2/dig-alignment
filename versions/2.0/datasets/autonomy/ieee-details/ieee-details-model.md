## ieee-details-sample.json

### PyTransforms
#### _abstract_uri_
From column: _crawl_data / url_
>``` python
return article_uri_from_citation_url(getValue("url"))
```

#### _author_uri_
From column: _crawl_data / authors / values_
>``` python
return author_uri(getValue("values"))
```

#### _datepublished_
From column: _crawl_data / year_
>``` python
return iso8601date(getValue("year"),"%Y")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _abstract_ | `schema:text` | `schema:ScholarlyArticle1`|
| _abstract_uri_ | `uri` | `schema:ScholarlyArticle1`|
| _author_uri_ | `uri` | `schema:Person1`|
| _datepublished_ | `schema:datePublished` | `schema:ScholarlyArticle1`|
| _title_ | `schema:name` | `schema:ScholarlyArticle1`|
| _values_ | `schema:name` | `schema:Person1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Person1` | `memex:isAuthorOf` | `schema:ScholarlyArticle1`|
| `schema:ScholarlyArticle1` | `schema:author` | `schema:Person1`|
