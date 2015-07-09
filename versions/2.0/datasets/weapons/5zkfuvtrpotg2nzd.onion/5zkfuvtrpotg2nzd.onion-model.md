## 5zkfuvtrpotg2nzd.onion-sample.json

### PyTransforms
#### _price_clean_
From column: _price_
>``` python
return cleanPrice(getValue("price"))
```

#### _price_currency_
From column: _price_
>``` python
return getCurrency(getValue("price"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _price_clean_ | `schema:price` | `schema:PriceSpecification1`|
| _price_currency_ | `schema:priceCurrency` | `schema:PriceSpecification1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|
| _url_ | `schema:url` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Offer1` | `schema:itemOffered` | `schema:Product1`|
| `schema:Offer1` | `schema:priceSpecification` | `schema:PriceSpecification1`|
| `schema:Offer1` | `schema:publisher` | `schema:Organization1`|
| `schema:Organization1` | `schema:name` | `xsd:5zkfuvtrpotg2nzd.onion`|
