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

#### _content_type_clean_
From column: _response / docs / type / values_
>``` python
return clean_content_type(getValue("values"))
```

#### _content_type_clean2_
From column: _response / docs / type / content_type_clean_
>``` python
return getValue("content_type_clean")
```

#### _content_type_uri_
From column: _response / docs / type / content_type_clean2_
>``` python
uri = content_type_uri(getValue("content_type_clean"))
if uri:
  return getValue("featurecollection_uri") + "/" + uri
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _content_type_clean_ | `memex:featureValue` | `memex:Feature1`|
| _content_type_clean2_ | `memex:content_type` | `memex:Feature1`|
| _content_type_uri_ | `uri` | `memex:Feature1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _id_ | `memex:databaseId` | `prov:Activity1`|
| _uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:content_type_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memex.zapto.org/data/software/jpl/version/0.1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
