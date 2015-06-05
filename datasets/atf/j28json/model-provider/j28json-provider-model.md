## j28json-sample.json

### PyTransforms
#### _threadLinkAbsolute_
From column: _thread_link_
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

#### _featureUri_
From column: _threadUri_
>``` python
return getValue("fcUri") + "/" + provider_uri(getValue("sourceName"))
```

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

#### _providerName_
From column: _featureUri_
>``` python
return getValue("sourceName").split(".")[0]
```

#### _providerName2_
From column: _providerName_
>``` python
return getValue("providerName")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _fcUri_ | `uri` | `memex:FeatureCollection1`|
| _featureUri_ | `uri` | `memex:Feature1`|
| _postUri_ | `uri` | `memex:Post1`|
| _providerName_ | `memex:provider_name` | `memex:Feature1`|
| _providerName2_ | `memex:featureValue` | `memex:Feature1`|
| _threadUri_ | `uri` | `memex:Thread1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:provider_name`|
| `memex:FeatureCollection1` | `memex:provider_name_feature` | `memex:Feature1`|
| `memex:Post1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
| `memex:Thread1` | `memex:hasPost` | `memex:Post1`|
