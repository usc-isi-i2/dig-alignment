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

#### _post_count_
From column: _posts / Unfold: label / posts / Values_
>``` python
return numericOnly(getValue("Values"))
```

#### _post_count2_
From column: _posts / Unfold: label / posts / post_count_
>``` python
return getValue("post_count")
```

#### _registered_date_
From column: _posts / Unfold: label / registered / Values_
>``` python
return iso8601date(getValue("Values"), "%Y-%M-%D")
```

#### _registered_date2_
From column: _posts / Unfold: label / registered / registered_date_
>``` python
return getValue("registered_date")
```

#### _user_uri_
From column: _posts / user_id2_
>``` python
uri = person_userid_uri(getValue("user_id"))
if uri:
  return getValue("fc_uri") + "/" + uri
return ''
```

#### _post_count_uri_
From column: _posts / Unfold: label / posts / post_count2_
>``` python
uri = person_postcount_uri(getValue("post_count"))
if uri:
  return getValue("fc_uri") + "/" + uri
return ''
```

#### _enrollment_uri_
From column: _posts / Unfold: label / registered / registered_date2_
>``` python
uri = enrollment_date_uri(getValue("registered_date"))
if uri:
  return getValue("fc_uri") + "/" + uri
return ''
```

#### _fromUser_uri_
From column: _posts / Unfold: label / from / from_copy_
>``` python
uri = fromUser_uri(getValue("from_copy"))
if uri:
  return getValue("fc_uri") + "/" + uri
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _enrollment_uri_ | `uri` | `memex:Feature4`|
| _fc_uri_ | `uri` | `memex:FeatureCollection1`|
| _fromUser_uri_ | `uri` | `memex:Feature1`|
| _from_copy_ | `memex:fromUser` | `memex:Feature1`|
| _post_count_ | `memex:featureValue` | `memex:Feature3`|
| _post_count2_ | `memex:person_postCount` | `memex:Feature3`|
| _post_count_uri_ | `uri` | `memex:Feature3`|
| _post_uri_ | `uri` | `memex:Post1`|
| _registered_date_ | `memex:enrollment_date` | `memex:Feature4`|
| _registered_date2_ | `memex:featureValue` | `memex:Feature4`|
| _uri_ | `uri` | `memex:Thread1`|
| _user_id_ | `memex:person_userid` | `memex:Feature2`|
| _user_id2_ | `memex:featureValue` | `memex:Feature2`|
| _user_uri_ | `uri` | `memex:Feature2`|
| _values_clean_ | `memex:featureValue` | `memex:Feature1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:fromUser`|
| `memex:Feature2` | `memex:featureName` | `xsd:person_userid`|
| `memex:Feature3` | `memex:featureName` | `xsd:person_postCount`|
| `memex:Feature4` | `memex:featureName` | `xsd:enrollment_date`|
| `memex:FeatureCollection1` | `memex:enrollment_date_feature` | `memex:Feature4`|
| `memex:FeatureCollection1` | `memex:fromUser_feature` | `memex:Feature1`|
| `memex:FeatureCollection1` | `memex:person_postCount_feature` | `memex:Feature3`|
| `memex:FeatureCollection1` | `memex:person_userid_feature` | `memex:Feature2`|
| `memex:Post1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
| `memex:Thread1` | `memex:hasPost` | `memex:Post1`|
