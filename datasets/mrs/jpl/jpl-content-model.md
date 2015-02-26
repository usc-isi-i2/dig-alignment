## jpl-sample.json

### PyTransforms
#### _aid_
From column: _response / docs / id_
>``` python
url = getValue("id")
idx = url.find("aid=")
if idx != -1:
   aid = url[idx+4:]
   idx = aid.find("&")
   if idx != -1:
      aid = aid[0:idx]
   return aid
return ""
```

#### _uri_
From column: _response / docs / aid_
>``` python
return "page/" + getValue("aid") + "/processed"
```

#### _body_uri_
From column: _response / docs / dc_title_
>``` python
return getValue("uri") + "/body"
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _body_uri_ | `uri` | `schema:WebPageElement1`|
| _uri_ | `uri` | `schema:WebPage1`|
| _values_ | `schema:text` | `schema:WebPageElement1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:WebPage1` | `memex:hasBodyPart` | `schema:WebPageElement1`|
