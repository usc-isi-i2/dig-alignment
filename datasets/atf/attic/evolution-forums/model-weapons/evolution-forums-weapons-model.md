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

#### _clean_content_
From column: _posts / content_
>``` python
return atf_body_clean(getValue('content'))
```

#### _weapons_
From column: _posts / signature_
>``` python
return get_weapons(getValue("topic_title"), getValue("title"), getValue("signature"), getValue("clean_content"))
```

#### _weapons_split2_
From column: _posts / weapons_split / Values_
>``` python
return getValue("Values")
```

#### _weapons_uri_
From column: _posts / weapons_split / weapons_split2_
>``` python
uri = weaponsMentioned_uri(getValue("Values"))
if uri:
  return getValue("fc_uri") + "/" + uri
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `memex:featureValue` | `memex:Feature1`|
| _fc_uri_ | `uri` | `memex:FeatureCollection1`|
| _post_uri_ | `uri` | `memex:Post1`|
| _uri_ | `uri` | `memex:Thread1`|
| _weapons_split2_ | `memex:weaponsMentioned` | `memex:Feature1`|
| _weapons_uri_ | `uri` | `memex:Feature1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:weaponsMentioned`|
| `memex:FeatureCollection1` | `memex:weaponsMentioned_feature` | `memex:Feature1`|
| `memex:Post1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
| `memex:Thread1` | `memex:hasPost` | `memex:Post1`|
