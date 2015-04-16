## evolution-forums_2015-01-16.tsv.jl.json

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

#### _prices_
From column: _url_
>``` python
return get_prices(getValue("topic_title"), getValue("title"), getValue("content"))
```

#### _prices2_
From column: _prices_
>``` python
return getValue("prices")
```

#### _provider_name_
From column: _posts / article_uri_
>``` python
return atf_provider_name(getValue("url"))
```

#### _provider_name2_
From column: _posts / provider_name_
>``` python
return getValue("provider_name")
```

#### _split_prices2_
From column: _split_prices / Values_
>``` python
return getValue("Values")
```

#### _joined_bitcoin_prices_
From column: _split_prices_
>``` python
return get_bitcoin_prices(getValue("topic_title"), getValue("title"), getValue("signature"), getValue("clean_content"))
```

#### _bitcoin_prices2_
From column: _bitcoin_prices / Values_
>``` python
return getValue("Values")
```

#### _post_count_
From column: _posts / Unfold: label / posts / Values_
>``` python
return numericOnly(getValue("Values"))
```

#### _post_count2_
From column: _posts / Unfold: label / posts / post_count_
>``` python
return getValue("post_count")
```

#### _enrollment_date_
From column: _posts / Unfold: label / registered / Values_
>``` python
return atf_joined_date(getValue("Values"), "%Y-%M-%D")
```

#### _enrollment_date2_
From column: _posts / Unfold: label / registered / enrollment_date_
>``` python
return getValue("enrollment_date")
```

#### _clean_content_
From column: _posts / content_
>``` python
return atf_body_clean(getValue('content'))
```

#### _joined_dollar_prices_
From column: _joined_bitcoin_prices_
>``` python
return get_dollar_prices(getValue("topic_title"), getValue("title"), getValue("signature"), getValue("clean_content"))
```

#### _dollar_prices2_
From column: _dollar_prices / Values_
>``` python
return getValue("Values")
```

#### _joined_weapons2_
From column: _bitcoin_prices_
>``` python
return get_weapons(getValue("topic_title"), getValue("title"), getValue("signature"), getValue("clean_content"))
```

#### _split_weapons2_
From column: _split_weapons / Values_
>``` python
return getValue("Values")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `memex:pricesMentioned` | `memex:Feature6`|
| _Values_ | `memex:featureValue` | `memex:Feature8`|
| _Values_ | `memex:featureValue` | `memex:Feature5`|
| _article_uri_ | `uri` | `schema:Article1`|
| _bitcoin_prices2_ | `memex:bitcoinPricesMentioned` | `memex:Feature8`|
| _clean_address_ | `memex:featureValue` | `memex:Feature3`|
| _clean_address2_ | `memex:place_postalAddress` | `memex:Feature3`|
| _clean_content_ | `schema:text` | `schema:WebPageElement2`|
| _dateCreated_ | `schema:dateCreated` | `schema:Article1`|
| _dollar_prices2_ | `memex:featureValue` | `memex:Feature6`|
| _enrollment_date_ | `memex:enrollment_date` | `memex:Feature2`|
| _enrollment_date2_ | `memex:featureValue` | `memex:Feature2`|
| _fc_uri_ | `uri` | `memex:FeatureCollection1`|
| _post_count_ | `memex:person_postCount` | `memex:Feature4`|
| _post_count2_ | `memex:featureValue` | `memex:Feature4`|
| _post_id_ | `rdfs:label` | `memex:Identifier1`|
| _provider_name_ | `memex:featureValue` | `memex:Feature7`|
| _provider_name2_ | `memex:provider_name` | `memex:Feature7`|
| _signature_clean_ | `schema:text` | `schema:WebPageElement3`|
| _split_weapons2_ | `memex:weaponsMentioned` | `memex:Feature5`|
| _title_ | `schema:text` | `schema:WebPageElement1`|
| _topic_id_ | `rdfs:label` | `memex:Identifier2`|
| _topic_title_ | `schema:text` | `schema:WebPageElement4`|
| _url_ | `schema:url` | `schema:Article2`|
| _username_ | `memex:featureValue` | `memex:Feature1`|
| _username2_ | `memex:person_username` | `memex:Feature1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:person_username`|
| `memex:Feature2` | `memex:featureName` | `xsd:enrollment_date`|
| `memex:Feature3` | `memex:featureName` | `xsd:place_postalAddress`|
| `memex:Feature4` | `memex:featureName` | `xsd:person_postCount`|
| `memex:Feature5` | `memex:featureName` | `xsd:weaponsMentioned`|
| `memex:Feature6` | `memex:featureName` | `xsd:pricesMentioned`|
| `memex:Feature7` | `memex:featureName` | `xsd:provider_name`|
| `memex:Feature8` | `memex:featureName` | `xsd:bitcoinPricesMentioned`|
| `memex:FeatureCollection1` | `memex:bitcoinPricesMentioned_feature` | `memex:Feature8`|
| `memex:FeatureCollection1` | `memex:enrollment_date_feature` | `memex:Feature2`|
| `memex:FeatureCollection1` | `memex:person_postCount_feature` | `memex:Feature4`|
| `memex:FeatureCollection1` | `memex:person_username_feature` | `memex:Feature1`|
| `memex:FeatureCollection1` | `memex:place_postalAddress_feature` | `memex:Feature3`|
| `memex:FeatureCollection1` | `memex:pricesMentioned_feature` | `memex:Feature6`|
| `memex:FeatureCollection1` | `memex:provider_name_feature` | `memex:Feature7`|
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
