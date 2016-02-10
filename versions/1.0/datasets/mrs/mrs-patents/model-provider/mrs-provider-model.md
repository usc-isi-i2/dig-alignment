## mrs-patent-data-sample.json

### PyTransforms
#### _uri_
From column: _aid_
>``` python
publicationNumber = getValue("Publication Number")
publicationNumber = ''.join(publicationNumber.split())
return "page/" + publicationNumber + "/processed"
```

#### _url_
From column: _url_
>``` python
return getValue("URL")
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

#### _featurecollection_uri_
From column: _uri_
>``` python
return getValue("uri")+"/featurecollection"
```

#### _feature_uri_
From column: _featurecollection_uri_
>``` python
return getValue("featurecollection_uri")+"/provider/patents"
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _feature_uri_ | `uri` | `memex:Feature1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:provider_name`|
| `memex:Feature1` | `memex:featureValue` | `xsd:PATENTS`|
| `memex:Feature1` | `memex:provider_name` | `xsd:PATENTS`|
| `memex:FeatureCollection1` | `memex:provider_name_feature` | `memex:Feature1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
