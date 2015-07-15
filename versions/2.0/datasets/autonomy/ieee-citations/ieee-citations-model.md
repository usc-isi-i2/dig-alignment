## ieee-citations-sample.json

### PyTransforms
#### _abstract_uri_
From column: _abstract_
>``` python
return abstract_uri(getValue("abstract"))
```

#### _citation_uri_
From column: _citations / ref_links / link_url_
>``` python
return article_uri_from_citation_url(getValue("link_url"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _abstract_uri_ | `uri` | `schema:ScholarlyArticle1`|
| _citation_uri_ | `uri` | `schema:ScholarlyArticle2`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:ScholarlyArticle1` | `memex:isCitationOf` | `schema:ScholarlyArticle2`|
| `schema:ScholarlyArticle2` | `schema:citation` | `schema:ScholarlyArticle1`|
