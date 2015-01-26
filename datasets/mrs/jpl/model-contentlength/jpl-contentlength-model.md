## jpl-solr-pdf.json

### PyTransforms
#### _uri_
From column: _response / docs / url_
>``` python
return "http://memex.zapto.org/data/page/"+get_url_hash(getValue("url"))+"/processed"
```

#### _featurecollection_uri_
From column: _response / docs / uri_
>``` python
return getValue("uri") + "/featurecollection"
```

#### _content_length_clean_
From column: _response / docs / contentLength_
>``` python
return clean_content_length(getValue("contentLength"))
```

#### _content_length_clean2_
From column: _response / docs / content_length_clean_
>``` python
return getValue("content_length_clean")
```

#### _content_length_uri_
From column: _response / docs / content_length_clean2_
>``` python
uri = content_length_uri(getValue("content_length_clean"))
if uri:
  return getValue("featurecollection_uri") + "/" + uri
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _content_length_clean_ | `memex:featureValue` | `memex:Feature1`|
| _content_length_clean2_ | `memex:content_length` | `memex:Feature1`|
| _content_length_uri_ | `uri` | `memex:Feature1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _id_ | `memex:databaseId` | `prov:Activity1`|
| _uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:content_length_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memex.zapto.org/data/software/jpl/version/0.1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
