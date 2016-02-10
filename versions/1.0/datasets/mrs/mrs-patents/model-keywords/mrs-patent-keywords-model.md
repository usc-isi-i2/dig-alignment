## Patents_keywrods_csv

### PyTransforms
#### _featureCollectionUri_
From column: _featureCollectionUri_
>``` python
return getValue("uri") + "/featurecollection"
```

#### _featureUri_
From column: _featureUri_
>``` python
return getValue("featureCollectionUri") + "/keywords"
```

#### _featureValue_
From column: _featureValue_
>``` python
return getValue("keywords")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _featureCollectionUri_ | `uri` | `memex:FeatureCollection1`|
| _featureUri_ | `uri` | `memex:Feature1`|
| _featureValue_ | `memex:featureValue` | `memex:Feature1`|
| _keywords_ | `schema:keywords` | `memex:Feature1`|
| _uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:FeatureCollection1` | `memex:keywords_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://dig.isi.edu/mrs/data/stanford/keywords`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
