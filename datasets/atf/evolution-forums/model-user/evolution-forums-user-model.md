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

#### _from_copy_
From column: _posts / Unfold: label / from / Values_
>``` python
return atf_clean_from_user(getValue("Values"))
```

#### _values_clean_
From column: _posts / Unfold: label / from / Values_
>``` python
return atf_clean_from_user(getValue("Values"))
```

#### _user_id2_
From column: _posts / user_id_
>``` python
return getValue("user_id")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _fc_uri_ | `uri` | `memex:FeatureCollection1`|
| _from_copy_ | `memex:fromUser` | `memex:Feature1`|
| _post_uri_ | `uri` | `memex:Post1`|
| _uri_ | `uri` | `memex:Thread1`|
| _user_id_ | `memex:person_userid` | `memex:Feature2`|
| _user_id2_ | `memex:featureValue` | `memex:Feature2`|
| _values_clean_ | `memex:featureValue` | `memex:Feature1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:fromUser`|
| `memex:Feature2` | `memex:featureName` | `xsd:person_userid`|
| `memex:FeatureCollection1` | `memex:fromUser_feature` | `memex:Feature1`|
| `memex:FeatureCollection1` | `memex:person_userid_feature` | `memex:Feature2`|
| `memex:Post1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
| `memex:Thread1` | `memex:hasPost` | `memex:Post1`|
