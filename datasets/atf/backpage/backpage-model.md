## backpage-sample.json

### PyTransforms
#### _clean_body_
From column: _body_html_
>``` python
return atf_body_clean(getValue("body_html"))
```

#### _article_uri_
From column: _original_url_
>``` python
return atf_article_uri(getValue("original_uri"),getValue("post_id"))
```

#### _date_created_
From column: _download_timestamp_
>``` python
return atf_date_created(getValue("posting_date"), format="%A, %B %d, %Y %I:%M %p")


```

#### _clean_address_
From column: _location_
>``` python
return clean_address(getValue("location"), "", "", ",")
```

#### _clean_address2_
From column: _clean_address_
>``` python
return getValue("clean_address")
```

#### _joined_weapons_
From column: _posting_date_
>``` python
return get_weapons(getValue("clean_body"), getValue("title"))
```

#### _Values_
From column: _weapons / Values_
>``` python
return getValue("Values")
```

#### _weapons2_
From column: _weapons / Values_
>``` python
return getValue("Values")
```

#### _joined_prices_
From column: _posting_date_
>``` python
return get_prices(getValue("clean_body"), getValue("title"))
```

#### _prices2_
From column: _prices / Values_
>``` python
return getValue("Values")
```

#### _fc_uri_
From column: _clean_body_
>``` python
return atf_fc_uri(getValue("article_uri"))
```

#### _provider_name_
From column: _original_url_
>``` python
return atf_provider_name(getValue("original_url"))
```

#### _provider_name2_
From column: _provider_name_
>``` python
return getValue("provider_name")
```

#### _joined_bitcoin_prices_
From column: _joined_prices_
>``` python
return get_bitcoin_prices(getValue("clean_body"), getValue("title"))
```

#### _bitcoin_prices2_
From column: _bitcoin_prices / Values_
>``` python
return getValue("Values")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `memex:bitcoinPricesMentioned` | `memex:Feature5`|
| _Values_ | `memex:featureValue` | `memex:Feature2`|
| _Values_ | `memex:featureValue` | `memex:Feature3`|
| _article_uri_ | `uri` | `schema:Article1`|
| _bitcoin_prices2_ | `memex:featureValue` | `memex:Feature5`|
| _clean_address_ | `memex:featureValue` | `memex:Feature1`|
| _clean_address2_ | `memex:place_postalAddress` | `memex:Feature1`|
| _clean_body_ | `schema:text` | `schema:WebPageElement2`|
| _date_created_ | `schema:dateCreated` | `schema:Article1`|
| _fc_uri_ | `uri` | `memex:FeatureCollection1`|
| _original_url_ | `schema:url` | `schema:Article1`|
| _post_id_ | `rdfs:label` | `memex:Identifier1`|
| _prices2_ | `memex:pricesMentioned` | `memex:Feature3`|
| _provider_name_ | `memex:featureValue` | `memex:Feature4`|
| _provider_name2_ | `memex:provider_name` | `memex:Feature4`|
| _title_ | `schema:text` | `schema:WebPageElement1`|
| _weapons2_ | `memex:weaponsMentioned` | `memex:Feature2`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:place_postalAddress`|
| `memex:Feature2` | `memex:featureName` | `xsd:weaponsMentioned`|
| `memex:Feature3` | `memex:featureName` | `xsd:pricesMentioned`|
| `memex:Feature4` | `memex:featureName` | `xsd:provider_name`|
| `memex:Feature5` | `memex:featureName` | `xsd:bitcoinPricesMentioned`|
| `memex:FeatureCollection1` | `memex:bitcoinPricesMentioned_feature` | `memex:Feature5`|
| `memex:FeatureCollection1` | `memex:place_postalAddress_feature` | `memex:Feature1`|
| `memex:FeatureCollection1` | `memex:pricesMentioned_feature` | `memex:Feature3`|
| `memex:FeatureCollection1` | `memex:provider_name_feature` | `memex:Feature4`|
| `memex:FeatureCollection1` | `memex:weaponsMentioned_feature` | `memex:Feature2`|
| `memex:Identifier1` | `memex:hasType` | `xsd:http://dig.isi.edu/data/thesauri/identifiertype/postid`|
| `schema:Article1` | `memex:hasBodyPart` | `schema:WebPageElement2`|
| `schema:Article1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
| `schema:Article1` | `memex:hasIdentifier` | `memex:Identifier1`|
| `schema:Article1` | `memex:hasTitlePart` | `schema:WebPageElement1`|
