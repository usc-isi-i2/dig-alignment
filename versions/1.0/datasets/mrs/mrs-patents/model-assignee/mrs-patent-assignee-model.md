## backreflection(1).json

### PyTransforms
#### _uri_
From column: _uri_
>``` python
publicationNumber = getValue("Publication Number")
publicationNumber = ''.join(publicationNumber.split())
return "page/" + publicationNumber + "/processed"
```

#### _featurecollection_uri_
From column: _featurecollection_uri_
>``` python
return getValue("uri") + "/featurecollection"
```

#### _organization_clean_
From column: _Assignee / organization_clean_
>``` python
return clean_name(getValue("values"))
```

#### _organization_clean2_
From column: _Assignee / organization_clean2_
>``` python
return getValue("organization_clean")
```

#### _organization_uri_
From column: _Assignee / organization_uri_
>``` python
uri = author_uri(getValue("organization_clean"))
if uri:
  return getValue("featurecollection_uri") + "/" + uri
return ''
```

#### _feature_uri_
From column: _feature_uri_
>``` python
return getValue("featurecollection_uri")+"/organization/mrs-patent"
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _feature_uri_ | `uri` | `memex:Feature1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _organization_clean_ | `memex:featureValue` | `memex:Feature1`|
| _organization_clean2_ | `memex:organization` | `memex:Feature1`|
| _organization_uri_ | `uri` | `memex:Feature1`|
| _uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:organization_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://dig.isi.edu/mrs/data/api/google`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
