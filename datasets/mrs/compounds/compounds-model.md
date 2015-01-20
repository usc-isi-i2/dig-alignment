## compounds-sample.json

### PyTransforms
#### _fc_uri_
From column: _uri_
>``` python
return getValue("uri") + "/featurecollection"
```

#### _feature_uri_
From column: _chemistry_names / values_
>``` python
x = getValue("values")
x = x.replace(" ", "_").lower()
return getValue("uri") + "/featurecollection/"+x
```

#### _values_2_
From column: _chemistry_names / values_
>``` python
return getValue("values")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _fc_uri_ | `uri` | `memex:FeatureCollection1`|
| _feature_uri_ | `uri` | `memex:Feature1`|
| _uri_ | `uri` | `schema:WebPage1`|
| _values_ | `memex:featureValue` | `memex:Feature1`|
| _values_2_ | `memex:compound` | `memex:Feature1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:compound`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity2`|
| `memex:FeatureCollection1` | `memex:compound_feature` | `memex:Feature1`|
| `prov:Activity2` | `prov:endedAtTime` | `xsd:2014-01-14`|
| `prov:Activity2` | `prov:wasAttributedTo` | `xsd:http://chemicaltagger.ch.cam.ac.uk/`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
