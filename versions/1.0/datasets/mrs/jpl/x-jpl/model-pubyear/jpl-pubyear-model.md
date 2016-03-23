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

#### _year_clean_
From column: _response / docs / featurecollection_uri_
>``` python
x = numericOnly(getValue("date"))
if len(x) > 3:
   return x[0:4]
return ''
```

#### _year_clean2_
From column: _response / docs / year_clean_
>``` python
return getValue("year_clean")
```

#### _year_uri_
From column: _response / docs / year_clean2_
>``` python
uri = publication_year_uri(getValue("year_clean"))
if uri:
  return getValue("featurecollection_uri") + "/" + uri
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _id_ | `memex:databaseId` | `prov:Activity1`|
| _uri_ | `uri` | `schema:WebPage1`|
| _year_clean_ | `memex:featureValue` | `memex:Feature1`|
| _year_clean2_ | `memex:publication_year` | `memex:Feature1`|
| _year_uri_ | `uri` | `memex:Feature1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:publication_year_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memex.zapto.org/data/software/jpl/version/0.1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
