## j28xml-sample.xml

### PyTransforms
#### _postUri_
From column: _doc / Unfold: name / url / Values_
>``` python
return j28PostUri(getValue("Values"))
```

#### _fcUri_
From column: _doc / Unfold: name / url / postUri_
>``` python
return j28xmlFeatureCollectionUri(getValue("postUri"))
```

#### _toUsers_
From column: _doc / Unfold: name / to_user / Values_
>``` python
return getValue("Values")
```

#### _weaponsMentioned_
From column: _doc / Unfold: name / firearm_type / Values_
>``` python
return getValue("Values")
```

#### _userPlacePostalAddress_
From column: _doc / Unfold: name / user_location / Values_
>``` python
return getValue("Values")
```

#### _postPlacePostalAddress_
From column: _doc / Unfold: name / post_location / Values_
>``` python
return getValue("Values")
```

#### _keywords_
From column: _doc / Unfold: name / keyword / Values_
>``` python
return getValue("Values")
```

#### _transactionType_
From column: _doc / Unfold: name / action / Values_
>``` python
return getValue("Values")
```

#### _phonenumber_
From column: _doc / Unfold: name / phone / Values_
>``` python
return getValue("Values")
```

#### _fromUser_
From column: _doc / Unfold: name / from_user / Values_
>``` python
return getValue("Values")
```

#### _emailDomainsMentioned_
From column: _doc / Unfold: name / email_domain / Values_
>``` python
return getValue("Values")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `memex:featureValue` | `memex:Feature8`|
| _Values_ | `memex:featureValue` | `memex:Feature5`|
| _Values_ | `memex:featureValue` | `memex:Feature1`|
| _Values_ | `memex:featureValue` | `memex:Feature4`|
| _Values_ | `memex:featureValue` | `memex:Feature6`|
| _Values_ | `memex:featureValue` | `memex:Feature7`|
| _Values_ | `memex:featureValue` | `memex:Feature2`|
| _Values_ | `memex:featureValue` | `memex:Feature9`|
| _Values_ | `memex:featureValue` | `memex:Feature3`|
| _emailDomainsMentioned_ | `memex:emailDomainsMentioned` | `memex:Feature9`|
| _fcUri_ | `uri` | `memex:FeatureCollection1`|
| _fromUser_ | `memex:fromUser` | `memex:Feature8`|
| _keywords_ | `memex:keywords` | `memex:Feature4`|
| _phonenumber_ | `memex:phonenumber` | `memex:Feature6`|
| _postPlacePostalAddress_ | `memex:place_postalAddress` | `memex:Feature3`|
| _postUri_ | `uri` | `memex:Post1`|
| _toUsers_ | `memex:toUsers` | `memex:Feature7`|
| _transactionType_ | `memex:transactionTypesMentioned` | `memex:Feature5`|
| _userPlacePostalAddress_ | `memex:place_postalAddress` | `memex:Feature2`|
| _weaponsMentioned_ | `memex:weaponsMentioned` | `memex:Feature1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:weaponsMentioned`|
| `memex:Feature2` | `memex:featureName` | `xsd:place_postalAddress`|
| `memex:Feature3` | `memex:featureName` | `xsd:place_postalAddress`|
| `memex:Feature4` | `memex:featureName` | `xsd:keywords`|
| `memex:Feature5` | `memex:featureName` | `xsd:transactionTypesMentioned`|
| `memex:Feature6` | `memex:featureName` | `xsd:phonenumber`|
| `memex:Feature7` | `memex:featureName` | `xsd:toUsers`|
| `memex:Feature8` | `memex:featureName` | `xsd:fromUser`|
| `memex:Feature9` | `memex:featureName` | `xsd:emailDomainsMentioned`|
| `memex:FeatureCollection1` | `memex:emailDomainsMentioned_feature` | `memex:Feature9`|
| `memex:FeatureCollection1` | `memex:fromUser_feature` | `memex:Feature8`|
| `memex:FeatureCollection1` | `memex:keywords_feature` | `memex:Feature4`|
| `memex:FeatureCollection1` | `memex:phonenumber_feature` | `memex:Feature6`|
| `memex:FeatureCollection1` | `memex:place_postalAddress_feature` | `memex:Feature2`|
| `memex:FeatureCollection1` | `memex:place_postalAddress_feature` | `memex:Feature3`|
| `memex:FeatureCollection1` | `memex:toUsers_feature` | `memex:Feature7`|
| `memex:FeatureCollection1` | `memex:transactionTypesMentioned_feature` | `memex:Feature5`|
| `memex:FeatureCollection1` | `memex:weaponsMentioned_feature` | `memex:Feature1`|
| `memex:Post1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
