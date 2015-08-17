## extracted_armsmhmd4c3hb5xu.json

### PyTransforms
#### _uri_
From column: _crawler_
>``` python
return uri_from_url_timestamp(getValue("url"),getValue("timestamp"))
```

#### _price_btc_clean_
From column: _listings / price_btc_
>``` python
return cleanPrice(getValue("price_btc"))
```

#### _price_btc_currency_
From column: _listings / price_btc_
>``` python
return "BTC"
```

#### _price_usd_clean_
From column: _listings / price_usd_
>``` python
return cleanPrice(getValue("price_usd"))
```

#### _price_usd_currency_
From column: _listings / price_usd_
>``` python
return getCurrency(getValue("price_usd"))
```

#### _offer_uri_
From column: _listings / title_
>``` python
return getValue("uri") + "/" + alphaNumeric(getValue("title")).replace(" ","_").lower()
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _offer_uri_ | `uri` | `schema:Offer1`|
| _organization_uri_ | `uri` | `schema:Organization1`|
| _price_btc_clean_ | `schema:price` | `schema:PriceSpecification1`|
| _price_btc_currency_ | `schema:priceCurrency` | `schema:PriceSpecification1`|
| _price_usd_clean_ | `schema:price` | `schema:PriceSpecification2`|
| _price_usd_currency_ | `schema:priceCurrency` | `schema:PriceSpecification2`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _url_ | `schema:url` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Offer1` | `schema:priceSpecification` | `schema:PriceSpecification1`|
| `schema:Offer1` | `schema:priceSpecification` | `schema:PriceSpecification2`|
| `schema:Offer1` | `schema:publisher` | `schema:Organization1`|
| `schema:Offer1` | `schema:itemOffered` | `schema:Product1`|
| `schema:Organization1` | `schema:name` | `xsd:armsmhmd4c3hb5xu.onion`|
| `schema:Product1` | `schema:offers` | `schema:Offer1`|
