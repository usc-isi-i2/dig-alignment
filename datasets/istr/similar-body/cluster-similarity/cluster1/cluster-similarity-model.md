## cluster-similarity-sample.json

### PyTransforms
#### _cluster_uri_
From column: _Column_1_
>``` python
return cluster_body_uri(getValue("Column_1"))
```

#### _cluster2_uri_
From column: _Column_2_
>``` python
uri = cluster_body_uri(getValue("Column_2"))
if uri:
   return getHTBaseUrl() + uri
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Column_1_ | `rdfs:label` | `memex:Cluster1`|
| _Column_3_ | `memex:similarity_score` | `memex:SimilarObject1`|
| _Column_4_ | `memex:numberOfItems` | `memex:Cluster1`|
| _cluster2_uri_ | `memex:similar_url` | `memex:SimilarObject1`|
| _cluster_uri_ | `uri` | `memex:Cluster1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Cluster1` | `schema:isSimilarTo` | `memex:SimilarObject1`|
