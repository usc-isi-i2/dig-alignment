## jpl-solr-pdf.json

### PyTransforms
#### _uri_
From column: _response / docs / url_
>``` python
return "http://memex.zapto.org/data/page/"+get_url_hash(getValue("url"))+"/processed"
```

#### _date_iso_
From column: _response / docs / date_
>``` python
return iso8601date(getValue("date"), "%Y-%m-%dT%H:%M:%SZ")
```

#### _snapshotUri_
From column: _response / docs / uri_
>``` python
return "http://memex.zapto.org/data/page/"+get_url_hash(getValue("url"))+"/raw"
```

#### _content_uri_
From column: _response / docs / content_
>``` python
if getValue("content"):
    return getValue("uri") + "/body"
return ''
```

#### _title_uri_
From column: _response / docs / title / values_
>``` python
if getValue("title"):
  return getValue("uri") + "/title"
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _content_ | `schema:text` | `schema:WebPageElement1`|
| _content_uri_ | `uri` | `schema:WebPageElement1`|
| _date_iso_ | `schema:dateCreated` | `schema:WebPage1`|
| _lang_ | `schema:inLanguage` | `schema:WebPage1`|
| _snapshotUri_ | `memex:snapshotUri` | `schema:WebPage1`|
| _title_uri_ | `uri` | `schema:WebPageElement2`|
| _uri_ | `uri` | `schema:WebPage1`|
| _url_ | `schema:url` | `schema:WebPage1`|
| _values_ | `schema:text` | `schema:WebPageElement2`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:WebPage1` | `memex:hasBodyPart` | `schema:WebPageElement1`|
| `schema:WebPage1` | `memex:hasTitlePart` | `schema:WebPageElement2`|
