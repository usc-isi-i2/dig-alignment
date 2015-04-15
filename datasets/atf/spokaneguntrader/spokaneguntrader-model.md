## spokaneguntrader-sample.json

### PyTransforms
#### _dateCreated_
From column: _posts / date_posted_
>``` python
return atf_date_created(getValue("date_posted"))
```

#### _signature_clean_
From column: _posts / signature_
>``` python
return signature_clean(getValue("signature"))
```

#### _article_uri_
From column: _posts / post_id_
>``` python
return atf_article_uri(getValue("url"), getValue("post_id"))
```

#### _fc_uri_
From column: _posts / username_
>``` python
return atf_fc_uri(getValue("article_uri"))
```

#### _username2_
From column: _posts / username_
>``` python
return getValue("username")
```

#### _joined_iso_
From column: _posts / Unfold: label / joined: / Values_
>``` python
return atf_joined_date(getValue("Values"))
```

#### _joined_iso2_
From column: _posts / Unfold: label / joined: / joined_iso_
>``` python
return getValue("joined_iso")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _article_uri_ | `uri` | `schema:Article1`|
| _content_ | `schema:text` | `schema:WebPageElement2`|
| _dateCreated_ | `schema:dateCreated` | `schema:Article1`|
| _fc_uri_ | `uri` | `memex:FeatureCollection1`|
| _joined_iso_ | `memex:enrollment_date` | `memex:Feature2`|
| _joined_iso2_ | `memex:featureValue` | `memex:Feature2`|
| _signature_clean_ | `schema:text` | `schema:WebPageElement3`|
| _title_ | `schema:text` | `schema:WebPageElement1`|
| _username_ | `memex:featureValue` | `memex:Feature1`|
| _username2_ | `memex:person_username` | `memex:Feature1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:person_username`|
| `memex:Feature2` | `memex:featureName` | `xsd:enrollment_date`|
| `memex:FeatureCollection1` | `memex:enrollment_date_feature` | `memex:Feature2`|
| `memex:FeatureCollection1` | `memex:person_username_feature` | `memex:Feature1`|
| `schema:Article1` | `memex:hasBodyPart` | `schema:WebPageElement2`|
| `schema:Article1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
| `schema:Article1` | `memex:hasSignaturePart` | `schema:WebPageElement3`|
| `schema:Article1` | `memex:hasTitlePart` | `schema:WebPageElement1`|
