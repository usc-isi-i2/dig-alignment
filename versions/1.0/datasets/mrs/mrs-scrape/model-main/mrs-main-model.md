## mrs-data-sample.json

### PyTransforms
#### _uri_
From column: _url_
>``` python
return "page/"+ getValue("aid")+"/processed"
```

#### _snapshotUri_
From column: _uri_
>``` python
uri = getValue("uri")
idx = uri.rfind("/processed")
if idx != -1:
  uri = uri[0:idx]
return getMRSBaseUrl() + uri + "/raw"
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
return iso8601date(numericOnly(getValue("year")) + "-1-1")
```

#### _doi_id_
From column: _doi_
>``` python
doi = getValue("doi")
doi = doi.replace("http://dx.doi.org/", "")
return doi
```

#### _fileId_
From column: _abstract_uri_
>``` python
url = getValue("url")
idx = url.find("fileId=")
if idx != -1:
   fileId = url[idx+7:]
   if fileId.endswith(".html"):
      fileId = fileId[0:len(fileId)-5]
   return fileId
return ""
```

#### _abstract_url_
From column: _fileId_
>``` python
fileId = getValue("fileId")
if fileId:
  return "http://journals.cambridge.org/abstract_" + fileId
return ""
```

#### _aid_
From column: _url_
>``` python
url = getValue("url")
idx = url.find("aid=")
if idx != -1:
   aid = url[idx+4:]
   idx = aid.find("&")
   if idx != -1:
      aid = aid[0:idx]
   return aid
return ""
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _abstract_ | `schema:text` | `schema:WebPageElement1`|
| _abstract_uri_ | `uri` | `schema:WebPageElement1`|
| _abstract_url_ | `schema:url` | `schema:WebPageElement1`|
| _dateCreated_ | `schema:dateCreated` | `schema:WebPage1`|
| _doi_id_ | `memex:digitalObjectIdentifier` | `schema:WebPage1`|
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
