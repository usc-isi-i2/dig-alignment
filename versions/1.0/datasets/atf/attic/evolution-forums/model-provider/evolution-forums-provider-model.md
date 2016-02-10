## evolution-forums-sample.json

### PyTransforms
#### _uri_
From column: _topic_title_
>``` python
return atf_thread_uri(getValue("url"))
```

#### _post_uri_
From column: _posts / post_number_
>``` python
return atf_article_uri(getValue("url"), getValue("post_id"))
```

#### _fc_uri_
From column: _posts / post_uri_
>``` python
return atf_fc_uri(getValue("post_uri"))
```

#### _feature_uri_
From column: _posts / fc_uri_
>``` python
return getValue("fc_uri") + "/" + provider_uri("evolution-forums")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _fc_uri_ | `uri` | `memex:FeatureCollection1`|
| _feature_uri_ | `uri` | `memex:Feature1`|
| _post_uri_ | `uri` | `memex:Post1`|
| _uri_ | `uri` | `memex:Thread1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:provider_name`|
| `memex:Feature1` | `memex:featureValue` | `xsd:evolution-forums`|
| `memex:Feature1` | `memex:provider_name` | `xsd:evolution-forums`|
| `memex:FeatureCollection1` | `memex:provider_name_feature` | `memex:Feature1`|
| `memex:Post1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
| `memex:Thread1` | `memex:hasPost` | `memex:Post1`|
