## deob-title-sample.json

### PyTransforms
#### _webpage_uri_
From column: _title_uri_
>``` python
uri = getValue("title_uri")
idx = uri.rfind("/title")
wuri = ''
if idx != -1:
  wuri = uri[0:idx]
return wuri
```

#### _featureCollection_uri_
From column: _webpage_uri_
>``` python
wuri =  getValue("webpage_uri")
if wuri:
  return wuri +"/featurecollection"
return ''
```

#### _clean_title2_
From column: _clean_title_
>``` python
return getValue("clean_title")
```

#### _gentime_iso_
From column: _gentime_
>``` python
if getValue("clean_title"):
  return iso8601date(getValue("gentime"))
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _clean_title_ | `memex:featureValue` | `memex:Feature1`|
| _clean_title2_ | `memex:text_title_clean` | `memex:Feature1`|
| _featureCollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _gentime_iso_ | `prov:endedAtTime` | `prov:Activity1`|
| _title_uri_ | `uri` | `schema:WebPageElement1`|
| _webpage_uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:text_title_clean`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPageElement1`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:FeatureCollection1` | `memex:text_title_clean_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memex.zapto.org/data/software/deobfuscator/isi/version/0.1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
| `schema:WebPage1` | `memex:hasTitlePart` | `schema:WebPageElement1`|
