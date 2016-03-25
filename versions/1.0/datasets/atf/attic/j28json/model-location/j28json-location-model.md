## j28-sample.json

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

#### _location2_
From column: _author / location_
>``` python
return getValue("location")
```

#### _postaladdressUri_
From column: _author / location2_
>``` python
uri = place_postalAddress_uri(getValue("location2"))
if uri:
  return getValue("fcUri") + "/" + uri
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _fcUri_ | `uri` | `memex:FeatureCollection1`|
| _location_ | `memex:place_postalAddress` | `memex:Feature1`|
| _location2_ | `memex:featureValue` | `memex:Feature1`|
| _postUri_ | `uri` | `memex:Post1`|
| _postaladdressUri_ | `uri` | `memex:Feature1`|
| _threadUri_ | `uri` | `memex:Thread1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:FeatureCollection1` | `memex:place_postalAddress_feature` | `memex:Feature1`|
| `memex:Post1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
| `memex:Thread1` | `memex:hasPost` | `memex:Post1`|
