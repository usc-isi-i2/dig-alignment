## evolution-sample.json

### PyTransforms
#### _uri_
From column: _url_
>``` python
return get_url_hash(getValue("url"))
```

#### _fc_uri_
From column: _uri_
>``` python
return atf_fc_uri(getValue("uri"))
```

#### _username2_
From column: _username_
>``` python
return getValue("username")
```

#### _price_clean_
From column: _price_
>``` python
return get_bitcoin_prices(getValue("price"))
```

#### _price_clean2_
From column: _price_clean_
>``` python
return getValue("price_clean")
```

#### _weapons_mentioned_
From column: _stock_
>``` python
return get_weapons(getValue("title"),getValue("description"))
```

#### _Values2_
From column: _weapons_mentioned_list / Values_
>``` python
return getValue("Values")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `memex:weaponsMentioned` | `memex:Feature3`|
| _Values2_ | `memex:featureValue` | `memex:Feature3`|
| _description_ | `schema:text` | `schema:WebPageElement1`|
| _fc_uri_ | `uri` | `memex:FeatureCollection1`|
| _price_clean_ | `memex:bitcoinPricesMentioned` | `memex:Feature2`|
| _price_clean2_ | `memex:featureValue` | `memex:Feature2`|
| _title_ | `schema:text` | `schema:WebPageElement2`|
| _uri_ | `uri` | `schema:Article1`|
| _url_ | `schema:url` | `schema:Article1`|
| _username_ | `memex:featureValue` | `memex:Feature1`|
| _username2_ | `memex:person_username` | `memex:Feature1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:person_username`|
| `memex:Feature1` | `memex:featureName` | `xsd:person_username`|
| `memex:Feature2` | `memex:featureName` | `xsd:bitcoinPricesMentioned`|
| `memex:Feature3` | `memex:featureName` | `xsd:weaponsMentioned`|
| `memex:FeatureCollection1` | `memex:bitcoinPricesMentioned_feature` | `memex:Feature2`|
| `memex:FeatureCollection1` | `memex:person_username_feature` | `memex:Feature1`|
| `memex:FeatureCollection1` | `memex:weaponsMentioned_feature` | `memex:Feature3`|
| `schema:Article1` | `memex:hasBodyPart` | `schema:WebPageElement1`|
| `schema:Article1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
| `schema:Article1` | `memex:hasTitlePart` | `schema:WebPageElement2`|
