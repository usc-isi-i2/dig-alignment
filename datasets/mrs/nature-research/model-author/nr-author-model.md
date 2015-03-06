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

#### _author_clean3_
From column: _authors / author_clean2_
>``` python
return getValue("author_clean")
```

#### _feature_uri_
From column: _authors / author_clean2_
>``` python
uri = author_uri(getValue("author_clean"))
if uri:
  return getValue("featurecollection_uri") + "/" + uri
return ''
```

#### _person_uri_
From column: _authors / author_clean3_
>``` python
return person_name_uri(getValue("author_clean"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _author_clean_ | `memex:author` | `memex:Feature1`|
| _author_clean2_ | `memex:featureValue` | `memex:Feature1`|
| _author_clean3_ | `memex:person_name` | `memex:PersonName1`|
| _doi_ | `memex:databaseId` | `prov:Activity1`|
| _feature_uri_ | `uri` | `memex:Feature1`|
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
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://dig.isi.edu/mrs/data/software/nr/version/0.1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
