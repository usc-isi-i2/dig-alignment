## similar-body-sample.json

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

#### _feature_uri_
From column: _column_2_copy_
>``` python
return getValue("feature_collection") + "/" + getValue("cluster_uri")
```

#### _cluster_uri_
From column: _feature_uri_
>``` python
return cluster_body_uri(getValue("Column_2"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Column_1_ | `uri` | `schema:WebPage1`|
| _Column_2_ | `memex:featureValue` | `memex:Feature1`|
| _cluster_uri_ | `uri` | `memex:Cluster1`|
| _column_2_copy_ | `memex:similar_bodyPart_cluster` | `memex:Feature1`|
| _feature_collection_ | `uri` | `memex:FeatureCollection1`|
| _feature_uri_ | `uri` | `memex:Feature1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:similar_bodyPart_cluster`|
| `memex:Feature1` | `memex:featureObject` | `memex:Cluster1`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:similar_bodyPart_cluster_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://dig.isi.edu/ht/data/software/isi/lsh-clustering/version/0.1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
