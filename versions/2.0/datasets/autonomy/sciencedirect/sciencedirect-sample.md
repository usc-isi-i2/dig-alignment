## sciencedirect-sample.json

### PyTransforms
#### _datepublished_
From column: _conference_date_
>``` python
return clean_date(getValue("conference_date"))
```

#### _author_uri_
From column: _authors / values_
>``` python
return author_uri(getValue("values"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _abstract_ | `schema:text` | `schema:ScholarlyArticle1`|
| _author_uri_ | `uri` | `schema:Person1`|
| _datepublished_ | `schema:datePublished` | `schema:ScholarlyArticle1`|
| _title_ | `schema:name` | `schema:ScholarlyArticle1`|
| _uri_ | `uri` | `schema:ScholarlyArticle1`|
| _values_ | `schema:keywords` | `schema:ScholarlyArticle1`|
| _values_ | `schema:name` | `schema:Person1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:ScholarlyArticle1` | `schema:author` | `schema:Person1`|