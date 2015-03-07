## nr-data-sample.json

### PyTransforms
#### _doi_id_
From column: _doi_
>``` python
doi = getValue("doi")
doi = doi.replace("http://dx.doi.org/", "")
return doi
```

#### _uri_
From column: _doi_id_
>``` python
doi = getValue("doi_id")
if doi:
  return "page/" + get_url_hash(doi) + "/processed"
return ''
```

#### _featurecollection_uri_
From column: _uri_
>``` python
return getValue("uri") + "/featurecollection"
```

#### _feature_uri_
From column: _featurecollection_uri_
>``` python
return getValue("featurecollection_uri")+"/provider/nature_research"
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
| `memex:Feature1` | `memex:featureValue` | `xsd:Nature Research`|
| `memex:Feature1` | `memex:provider_name` | `xsd:Nature Research`|
| `memex:FeatureCollection1` | `memex:provider_name_feature` | `memex:Feature1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
