## ieee-references-sample.json

### PyTransforms
#### _abstract_uri_
From column: _abstract_
>``` python
return abstract_uri(getValue("abstract"))
```

#### _reference_uri_
From column: _references / ref_links / link_url_
>``` python
return article_uri_from_citation_url(getValue("link_url"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _abstract_uri_ | `uri` | `schema:ScholarlyArticle1`|
| _reference_uri_ | `uri` | `schema:ScholarlyArticle2`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:ScholarlyArticle1` | `schema:citation` | `schema:ScholarlyArticle2`|
| `schema:ScholarlyArticle2` | `memex:isCitationOf` | `schema:ScholarlyArticle1`|
