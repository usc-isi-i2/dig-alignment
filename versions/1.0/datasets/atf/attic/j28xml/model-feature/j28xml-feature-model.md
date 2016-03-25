## j28xml-sample.xml

### PyTransforms
#### _featureValue_
From column: _add / doc / field / content_
>``` python
if j28xmlFeatureName(getValue("name")):
    return getValue("content")
else:
    return ""
```

#### _featureValue2_
From column: _add / doc / field / featureValue_
>``` python
return getValue("featureValue")
```

#### _featureName_
From column: _add / doc / field / name_
>``` python
return j28xmlFeatureName(getValue("name"))
```

#### _featureValueSpec_
From column: _add / doc / field / name_
>``` python
return j28xmlFeatureNameUri(getValue("featureName"))
```

#### _hasFeaturesSpec_
From column: _add / doc / field / featureName_
>``` python
return j28xmlFeatureCollectionLinkName(getValue("name"))
```

#### _fcUri_
From column: _add / doc / field / hasFeaturesSpec_
>``` python
if getValue("featureName"):
    postUri = getValueFromNestedColumnByIndex("Unfold: name", "url/postUri", 0)
    return j28xmlFeatureCollectionUri(postUri)
else:
    return ""
```

#### _postUri_
From column: _add / doc / Unfold: name / url / Values_
>``` python
return j28PostUri(getValue("Values"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _fcUri_ | `uri` | `memex:FeatureCollection1`|
| _featureName_ | `memex:featureName` | `memex:Feature1`|
| _featureValue_ | `memex:featureValue` | `memex:Feature1`|
| _featureValue2_ | `memex:featureValue` | `memex:Feature1`|
| _featureValueSpec_ | `km-dev:dataPropertyOfColumnLink` | `memex:Feature1`|
| _hasFeatureSpec_ | `km-dev:objectPropertySpecialization` | `memex:FeatureCollection1`|
| _postUri_ | `uri` | `memex:Post1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:FeatureCollection1` | `memex:hasFeatures` | `memex:Feature1`|
| `memex:Post1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
