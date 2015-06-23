## j28json-sample.json

### PyTransforms
#### _sourceName_
From column: _thread_link_
>``` python
return inferSourceName(getValue("thread_link"), getValue("link"))
```

#### _siteRoot_
From column: _sourceName_
>``` python
return j28SiteRoot(getValue("sourceName"))
```

#### _threadLinkAbsolute_
From column: _siteRoot_
>``` python
return j28ThreadLinkAbsolute(getValue("siteRoot"), getValue("thread_link"))
```

#### _threadUri_
From column: _threadLinkAbsolute_
>``` python
return j28ThreadUri(getValue("threadLinkAbsolute"))
```

#### _postUri_
From column: _link_
>``` python
return j28PostUri(getValue("link"))
```

#### _fcUri_
From column: _link_
>``` python
return atf_fc_uri(getValue("postUri"))
```

#### _username2_
From column: _author / username_
>``` python
return getValue("username")
```

#### _fromUserUri_
From column: _author / username2_
>``` python
uri = fromUser_uri(getValue("username2"))
if uri:
  return getValue("fcUri") + "/" + uri
return ''
```

#### _author_id2_
From column: _author / author_id_
>``` python
return getValue("author_id")
```

#### _personUseridUri_
From column: _author / author_id2_
>``` python
uri = person_userid_uri(getValue("author_id2"))
if uri:
  return getValue("fcUri") + "/" + uri
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _author_id_ | `memex:person_userid` | `memex:Feature2`|
| _author_id2_ | `memex:featureValue` | `memex:Feature2`|
| _fcUri_ | `uri` | `memex:FeatureCollection1`|
| _fromUserUri_ | `uri` | `memex:Feature1`|
| _personUseridUri_ | `uri` | `memex:Feature2`|
| _postUri_ | `uri` | `memex:Post1`|
| _threadUri_ | `uri` | `memex:Thread1`|
| _username_ | `memex:fromUser` | `memex:Feature1`|
| _username2_ | `memex:featureValue` | `memex:Feature1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:fromUser`|
| `memex:Feature2` | `memex:featureName` | `xsd:person_userid`|
| `memex:FeatureCollection1` | `memex:fromUser_feature` | `memex:Feature1`|
| `memex:FeatureCollection1` | `memex:person_userid_feature` | `memex:Feature2`|
| `memex:Post1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
| `memex:Thread1` | `memex:hasPost` | `memex:Post1`|
