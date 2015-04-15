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

#### _username2_
From column: _posts / username_
>``` python
return getValue("username")
```

#### _fc_uri_
From column: _posts / username2_
>``` python
return atf_fc_uri(getValue("article_uri"))
```

#### _city_
From column: _posts / Unfold: label / city, state: / Values_
>``` python
return atf_get_city(getValue("Values"))
```

#### _state_
From column: _posts / Unfold: label / city, state: / city_
>``` python
return atf_get_state(getValue("Values"))
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

#### _country_
From column: _posts / Unfold: label / city, state: / state_
>``` python
return "US"
```

#### _address_uri_
From column: _posts / Unfold: label / city, state: / country_
>``` python
return atf_address_uri(getValue("city"), getValue("state"), getValue("country"))
```

#### _clean_address_
From column: _posts / Unfold: label / city, state: / country_
>``` python
return clean_address(getValue("city"), getValue("state"), getValue("country"), ",")
```

#### _clean_address2_
From column: _posts / Unfold: label / city, state: / clean_address_
>``` python
return getValue("clean_address")
```

#### _clean_post_count_
From column: _posts / Unfold: label / posts: / Values_
>``` python
return atf_clean_post_count(getValue("Values"))
```

#### _clean_post_count2_
From column: _posts / Unfold: label / posts: / clean_post_count_
>``` python
return getValue("clean_post_count")
```

#### _joined_weapons_
From column: _posts / Unfold: label / Glue_1 / Values_1_
>``` python
return get_weapons(getValue("Values"), getValue("Values_1"), getValue("topic_title"), getValue("title"), getValue("signature_clean"), getValue("content"))
```

#### _weapons2_
From column: _posts / Unfold: label / Glue_1 / weapons / Values_
>``` python
return getValue("Values")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `memex:weaponsMentioned` | `memex:Feature5`|
| _article_uri_ | `uri` | `schema:Article1`|
| _clean_address_ | `memex:featureValue` | `memex:Feature3`|
| _clean_address2_ | `memex:place_postalAddress` | `memex:Feature3`|
| _clean_post_count_ | `memex:featureValue` | `memex:Feature4`|
| _clean_post_count2_ | `memex:person_postCount` | `memex:Feature4`|
| _content_ | `schema:text` | `schema:WebPageElement2`|
| _dateCreated_ | `schema:dateCreated` | `schema:Article1`|
| _fc_uri_ | `uri` | `memex:FeatureCollection1`|
| _joined_iso_ | `memex:enrollment_date` | `memex:Feature2`|
| _joined_iso2_ | `memex:featureValue` | `memex:Feature2`|
| _post_id_ | `rdfs:label` | `memex:Identifier1`|
| _signature_clean_ | `schema:text` | `schema:WebPageElement3`|
| _title_ | `schema:text` | `schema:WebPageElement1`|
| _topic_id_ | `rdfs:label` | `memex:Identifier2`|
| _topic_title_ | `schema:text` | `schema:WebPageElement4`|
| _url_ | `schema:url` | `schema:Article2`|
| _username_ | `memex:featureValue` | `memex:Feature1`|
| _username2_ | `memex:person_username` | `memex:Feature1`|
| _weapons2_ | `memex:featureValue` | `memex:Feature5`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:person_username`|
| `memex:Feature2` | `memex:featureName` | `xsd:enrollment_date`|
| `memex:Feature3` | `memex:featureName` | `xsd:place_postalAddress`|
| `memex:Feature4` | `memex:featureName` | `xsd:person_postCount`|
| `memex:Feature5` | `memex:featureName` | `xsd:weaponsMentioned_feature`|
| `memex:FeatureCollection1` | `memex:enrollment_date_feature` | `memex:Feature2`|
| `memex:FeatureCollection1` | `memex:person_postCount_feature` | `memex:Feature4`|
| `memex:FeatureCollection1` | `memex:person_username_feature` | `memex:Feature1`|
| `memex:FeatureCollection1` | `memex:place_postalAddress_feature` | `memex:Feature3`|
| `memex:FeatureCollection1` | `memex:weaponsMentioned_feature` | `memex:Feature5`|
| `memex:Identifier1` | `memex:hasType` | `xsd:http://dig.isi.edu/data/thesauri/identifiertype/postid`|
| `memex:Identifier2` | `memex:hasType` | `xsd:http://dig.isi.edu/data/thesauri/identifiertype/postid`|
| `schema:Article1` | `memex:hasBodyPart` | `schema:WebPageElement2`|
| `schema:Article1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
| `schema:Article1` | `memex:hasSignaturePart` | `schema:WebPageElement3`|
| `schema:Article1` | `memex:hasTitlePart` | `schema:WebPageElement1`|
| `schema:Article1` | `schema:isPartOf` | `schema:Article2`|
| `schema:Article1` | `memex:hasIdentifier` | `memex:Identifier1`|
| `schema:Article2` | `memex:hasIdentifier` | `memex:Identifier2`|
| `schema:Article2` | `memex:hasTitlePart` | `schema:WebPageElement4`|
