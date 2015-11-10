## ht-crf-eyes-hair.json

### PyTransforms
#### _feature_name_
From column: _featureName_
>``` python
return get_eye_hair_feature_name(getValue("featureName"), getValue("featureValue"))
```

#### _offer_uri_
From column: _uri_
>``` python
if getValue("feature_name") != "":
    return getValue("uri")
return ""
```

#### _adultservice_uri_
From column: _offer_uri_
>``` python
uri = getValue("offer_uri")
if uri != "":
    splits = uri.split("/")
    val=''
    for i in range(0,len(splits)-2):
        val=val+splits[i]+"/"
    return val + "adultservice"
return ""
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _adultservice_uri_ | `uri` | `memex:AdultService1`|
| _featureValue_ | `memex:hairColor` | `memex:AdultService1`|
| _feature_name_ | `km-dev:dataPropertyOfColumnLink` | `memex:AdultService1`|
| _offer_uri_ | `uri` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:AdultService1` | `schema:offers` | `schema:Offer1`|
| `schema:Offer1` | `schema:itemOffered` | `memex:AdultService1`|
