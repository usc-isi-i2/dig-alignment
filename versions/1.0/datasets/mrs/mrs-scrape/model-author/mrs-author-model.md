## mrs-data-sample.json

### PyTransforms
#### _uri_
From column: _url_
>``` python
return "page/"+getValue("aid")+"/processed"
```

#### _featurecollection_uri_
From column: _uri_
>``` python
return getValue("uri") + "/featurecollection"
```

#### _author_clean_
From column: _authors / values_
>``` python
return clean_name(getValue("values"))
```

#### _author_clean2_
From column: _authors / author_clean_
>``` python
return getValue("author_clean")
```

#### _author_uri_
From column: _authors / author_clean2_
>``` python
uri = author_uri(getValue("author_clean"))
if uri:
  return getValue("featurecollection_uri") + "/" + uri
return ''
```

#### _author_clean3_
From column: _authors / author_uri_
>``` python
return getValue("author_clean")
```

#### _person_uri_
From column: _authors / author_clean3_
>``` python
return person_name_uri(getValue("author_clean"))
```

#### _aid_
From column: _uri_
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
| _author_clean_ | `memex:featureValue` | `memex:Feature1`|
| _author_clean2_ | `memex:author` | `memex:Feature1`|
| _author_clean3_ | `memex:person_name` | `memex:PersonName1`|
| _author_uri_ | `uri` | `memex:Feature1`|
| _doi_ | `memex:databaseId` | `prov:Activity1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _person_uri_ | `uri` | `memex:PersonName1`|
| _uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:author`|
| `memex:Feature1` | `memex:featureObject` | `memex:PersonName1`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:author_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://dig.isi.edu/mrs/data/software/mrs/version/0.1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
