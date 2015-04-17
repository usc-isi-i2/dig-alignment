## achecrawler.json

### PyTransforms
#### _article_uri_
From column: __source / url_
>``` python
return atf_article_uri(getValue("url"), "0")
```

#### _domain2_
From column: __source / domain_
>``` python
return getValue("domain")
```

#### _fc_uri_
From column: __source / url_
>``` python
return atf_fc_uri(getValue("article_uri"))
```

#### _joined_weapons_
From column: __source / text_
>``` python
return get_weapons(getValue("title"), getValue("text"))
```

#### _joined_prices_
From column: __source / text_
>``` python
return get_prices(getValue("title"), getValue("text"))
```

#### _weapons2_
From column: __source / weapons / Values_
>``` python
return getValue("Values")
```

#### _prices2_
From column: __source / prices / Values_
>``` python
return getValue("Values")
```

#### _joined_bitcoin_prices_
From column: __source / joined_prices_
>``` python
return get_prices(getValue("title"), getValue("text"))
```

#### _bitcoin_prices2_
From column: __source / bitcoin_prices / Values_
>``` python
return getValue("Values")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `memex:weaponsMentioned` | `memex:Feature2`|
| _Values_ | `memex:pricesMentioned` | `memex:Feature3`|
| _Values_ | `memex:bitcoinPricesMentioned` | `memex:Feature4`|
| _article_uri_ | `uri` | `schema:Article1`|
| _bitcoin_prices2_ | `memex:featureValue` | `memex:Feature4`|
| _domain_ | `memex:featureValue` | `memex:Feature1`|
| _domain2_ | `memex:provider_name` | `memex:Feature1`|
| _fc_uri_ | `uri` | `memex:FeatureCollection1`|
| _prices2_ | `memex:featureValue` | `memex:Feature3`|
| _text_ | `schema:text` | `schema:WebPageElement2`|
| _title_ | `schema:text` | `schema:WebPageElement1`|
| _weapons2_ | `memex:featureValue` | `memex:Feature2`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature2` | `memex:featureName` | `xsd:weapons_mentioned`|
| `memex:Feature3` | `memex:featureName` | `xsd:prices_mentioned`|
| `memex:Feature4` | `memex:featureName` | `xsd:bitcoinPricesMentioned`|
| `memex:FeatureCollection1` | `memex:bitcoinPricesMentioned_feature` | `memex:Feature4`|
| `memex:FeatureCollection1` | `memex:pricesMentioned_feature` | `memex:Feature3`|
| `memex:FeatureCollection1` | `memex:provider_name_feature` | `memex:Feature1`|
| `memex:FeatureCollection1` | `memex:weaponsMentioned_feature` | `memex:Feature2`|
| `schema:Article1` | `memex:hasBodyPart` | `schema:WebPageElement1`|
| `schema:Article1` | `memex:hasBodyPart` | `schema:WebPageElement2`|
| `schema:Article1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
