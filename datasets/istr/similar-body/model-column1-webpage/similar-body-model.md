## similar-body-sample.csv

### PyTransforms
#### _feature_collection_
From column: _Column_1_
>``` python
return getValue("Column_1") + "/featurecollection"
```

#### _column_2_copy_
From column: _Column_2_
>``` python
return getValue("Column_2")
```

#### _column_2_copy2_
From column: _column_2_copy_
>``` python
return getValue("Column_2")
```

#### _column_2_rel_
From column: _column_2_copy_
>``` python
baseurl = getHTBaseUrl()
baselen = len(baseurl)
return getValue("Column_2")[baselen:]
```

#### _feature_uri_
From column: _column_2_rel_
>``` python
return getValue("feature_collection") + "/similar/" + getValue("column_2_rel")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Column_1_ | `uri` | `schema:WebPage1`|
| _Column_2_ | `memex:featureValue` | `memex:Feature1`|
| _Column_3_ | `memex:similarity_score` | `memex:SimilarObject1`|
| _column_2_copy_ | `memex:similar_bodyPart` | `memex:Feature1`|
| _column_2_copy2_ | `memex:similar_url` | `memex:SimilarObject1`|
| _feature_collection_ | `uri` | `memex:FeatureCollection1`|
| _feature_uri_ | `uri` | `memex:Feature1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:similar_bodyPart`|
| `memex:Feature1` | `memex:featureObject` | `memex:SimilarObject1`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:similar_bodyPart_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://dig.isi.edu/ht/data/software/isi/lsh-clustering/version/0.1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
