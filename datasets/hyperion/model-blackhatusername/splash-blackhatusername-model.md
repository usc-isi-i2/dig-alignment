## splash.json

### PyTransforms
#### _cache_uri_
From column: _timestamp_
>``` python
return getCacheBaseUrl()+"page/"+get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/processed"
```

#### _fetaurecollection_uri_
From column: _cache_uri_
>``` python
return getValue("cache_uri") + "/featurecollection"
```

#### _username_clean_
From column: _blackhat_username_histogram / fold_1 / names_
>``` python
return clean_username(getValue("names"))
```

#### _username_clean2_
From column: _blackhat_username_histogram / fold_1 / username_clean_
>``` python
return getValue("username_clean")
```

#### _username_uri_
From column: _blackhat_username_histogram / fold_1 / username_clean2_
>``` python
uri = person_blackhat_username_uri(getValue("username_clean"))
if uri:
  return getValue("fetaurecollection_uri") + "/" + uri
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _cache_uri_ | `uri` | `schema:WebPage1`|
| _fetaurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _username_clean_ | `memex:featureValue` | `memex:Feature1`|
| _username_clean2_ | `memex:person_blackhat_username` | `memex:Feature1`|
| _username_uri_ | `uri` | `memex:Feature1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:person_blackhat_username`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:person_blackhat_username_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memex.zapto.org/data/software/extractor/hyperion/version/jan2015`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
