## armoryx7kvdq3jds.onion-sample.json

### PyTransforms
#### _clean_price_
From column: _price_
>``` python
return cleanPrice(getValue("price"))
```

#### _price_currency_
From column: _price_
>``` python
return getCurrency(getValue("price"))
```

#### _clean_price_btc_
From column: _price_btc_
>``` python
return getValue("price_btc")
```

#### _price_btc_currency_
From column: _price_btc_
>``` python
return "BTC"
```

#### _price_uri_
From column: _price_
>``` python
return price_uri(getValue("price"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:category` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _brand_ | `schema:name` | `schema:Brand1`|
| _clean_price_ | `schema:price` | `schema:PriceSpecification1`|
| _clean_price_btc_ | `schema:price` | `schema:PriceSpecification2`|
| _description_ | `schema:description` | `schema:Offer1`|
| _price_btc_currency_ | `schema:priceCurrency` | `schema:PriceSpecification2`|
| _price_currency_ | `schema:priceCurrency` | `schema:PriceSpecification1`|
| _product_code_ | `schema:productID` | `schema:Product1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|
| _url_ | `schema:url` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Offer1` | `schema:itemOffered` | `schema:Product1`|
| `schema:Offer1` | `schema:priceSpecification` | `schema:PriceSpecification1`|
| `schema:Offer1` | `schema:priceSpecification` | `schema:PriceSpecification2`|
| `schema:Offer1` | `schema:publisher` | `schema:Organization1`|
| `schema:Organization1` | `schema:name` | `xsd:armoryx7kvdq3jds.onion`|
| `schema:Product1` | `schema:brand` | `schema:Brand1`|
