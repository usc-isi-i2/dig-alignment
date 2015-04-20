## mrs-patent-data-sample2.json

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

#### _inventor_clean_
From column: _Inventors / inventor_clean_
>``` python
return clean_name(getValue("values"))
```

#### _inventor_clean2_
From column: _Inventors / inventor_clean2_
>``` python
return getValue("inventor_clean")
```

#### _inventor_uri_
From column: _Inventors / inventor_uri_
>``` python
uri = author_uri(getValue("inventor_clean"))
if uri:
  return getValue("featurecollection_uri") + "/" + uri
return ''
```

#### _inventor_clean3_
From column: _Inventors / inventor_clean3_
>``` python
return getValue("inventor_clean")
```

#### _person_uri_
From column: _Inventors / person_uri_
>``` python
return person_name_uri(getValue("inventor_clean"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _inventor_clean_ | `memex:featureValue` | `memex:Feature1`|
| _inventor_clean2_ | `memex:author` | `memex:Feature1`|
| _inventor_clean3_ | `memex:person_name` | `memex:PersonName1`|
| _inventor_uri_ | `uri` | `memex:Feature1`|
| _person_uri_ | `uri` | `memex:PersonName1`|
| _uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureObject` | `memex:PersonName1`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:author_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://dig.isi.edu/mrs/data/api/google`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
