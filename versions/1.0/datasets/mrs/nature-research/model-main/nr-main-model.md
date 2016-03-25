## nr-data-sample.json

### PyTransforms
#### _dio_id_
From column: _doi_
>``` python
doi = getValue("doi")
doi = doi.replace("http://dx.doi.org/", "")
return doi
```

#### _uri_
From column: _dio_id_
>``` python
doi = getValue("dio_id")
if doi:
  return "page/" + get_url_hash(doi) + "/processed"
return ''
```

#### _snapshot_uri_
From column: _uri_
>``` python
uri = getValue("uri")
if uri:
    idx = uri.rfind("/processed")
    if idx != -1:
      uri = uri[0:idx]
    return getMRSBaseUrl() + uri + "/raw"
return ''
```

#### _title_uri_
From column: _title_
>``` python
uri = getValue("uri")
if uri:
   return getValue("uri") + "/title"
return ''
```

#### _abstract_uri_
From column: _abstract_
>``` python
uri = getValue("uri")
if uri:
  return uri + "/abstract"
return ''
```

#### _dateCreated_
From column: _year_
>``` python
year = getValue("year")
if year:
  return iso8601date(numericOnly(year) + "-1-1")
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _abstract_ | `schema:text` | `schema:WebPageElement2`|
| _abstract_uri_ | `uri` | `schema:WebPageElement2`|
| _dateCreated_ | `schema:dateCreated` | `schema:WebPage1`|
| _dio_id_ | `memex:digitalObjectIdentifier` | `schema:WebPage1`|
| _snapshot_uri_ | `memex:snapshotUri` | `schema:WebPage1`|
| _title_ | `schema:text` | `schema:WebPageElement1`|
| _title_uri_ | `uri` | `schema:WebPageElement1`|
| _uri_ | `uri` | `schema:WebPage1`|
| _url_ | `schema:url` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:WebPage1` | `memex:hasAbstractPart` | `schema:WebPageElement2`|
| `schema:WebPage1` | `memex:hasTitlePart` | `schema:WebPageElement1`|
