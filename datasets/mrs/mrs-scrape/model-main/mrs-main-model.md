## msr-data-sample.json

### PyTransforms
#### _uri_
From column: _url_
>``` python
return "http://memex.zapto.org/data/page/"+get_url_hash(getValue("url"))+"/processed"
```

#### _snapshotUri_
From column: _uri_
>``` python
return "http://memex.zapto.org/data/page/"+get_url_hash(getValue("url"))+"/raw"
```

#### _abstract_uri_
From column: _abstract_
>``` python
return getValue("uri") + "/abstract"
```

#### _title_uri_
From column: _title_
>``` python
return getValue("uri") + "/title"
```

#### _dateCreated_
From column: _year_
>``` python
return iso8601date(getValue("year") + "-1-1")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _abstract_ | `schema:text` | `schema:WebPageElement1`|
| _abstract_uri_ | `uri` | `schema:WebPageElement1`|
| _dateCreated_ | `schema:dateCreated` | `schema:WebPage1`|
| _snapshotUri_ | `memex:snapshotUri` | `schema:WebPage1`|
| _title_ | `schema:text` | `schema:WebPageElement2`|
| _title_uri_ | `uri` | `schema:WebPageElement2`|
| _uri_ | `uri` | `schema:WebPage1`|
| _url_ | `schema:url` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:WebPage1` | `memex:hasAbstractPart` | `schema:WebPageElement1`|
| `schema:WebPage1` | `memex:hasTitlePart` | `schema:WebPageElement2`|
