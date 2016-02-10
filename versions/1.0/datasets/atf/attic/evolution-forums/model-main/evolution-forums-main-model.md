## evolution-forums-sample.json

### PyTransforms
#### _uri_
From column: _topic_title_
>``` python
return atf_thread_uri(getValue("url"))
```

#### _post_uri_
From column: _posts / post_number_
>``` python
return atf_article_uri(getValue("url"), getValue("post_id"))
```

#### _content_clean_
From column: _posts / content_
>``` python
return atf_body_clean(getValue("content"))
```

#### _signature_clean_
From column: _posts / signature_
>``` python
return signature_clean(getValue("signature"))
```

#### _iso_date_posted_
From column: _posts / date_posted_
>``` python
return iso8601date(getValue("date_posted"), "%Y-%m-%d %H:%M:%S")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _content_clean_ | `schema:text` | `schema:WebPageElement3`|
| _iso_date_posted_ | `schema:dateCreated` | `memex:Post1`|
| _post_id_ | `rdfs:label` | `memex:Identifier2`|
| _post_uri_ | `uri` | `memex:Post1`|
| _signature_clean_ | `schema:text` | `schema:WebPageElement4`|
| _title_ | `schema:text` | `schema:WebPageElement2`|
| _topic_id_ | `rdfs:label` | `memex:Identifier1`|
| _topic_title_ | `schema:text` | `schema:WebPageElement1`|
| _uri_ | `uri` | `memex:Thread1`|
| _url_ | `schema:url` | `memex:Thread1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Post1` | `memex:hasBodyPart` | `schema:WebPageElement3`|
| `memex:Post1` | `memex:hasIdentifier` | `memex:Identifier2`|
| `memex:Post1` | `memex:hasSignaturePart` | `schema:WebPageElement4`|
| `memex:Post1` | `memex:hasTitlePart` | `schema:WebPageElement2`|
| `memex:Thread1` | `memex:hasIdentifier` | `memex:Identifier1`|
| `memex:Thread1` | `memex:hasPost` | `memex:Post1`|
| `memex:Thread1` | `memex:hasTitlePart` | `schema:WebPageElement1`|
