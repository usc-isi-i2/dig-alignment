## nucleuspf3izq7o6.onion-sample.json

### PyTransforms
#### _price_btc_clean_
From column: _price_btc_
>``` python
return cleanPrice(getValue("price_btc"))
```

#### _price_btc_currency_
From column: _price_btc_
>``` python
return "BTC"
```

#### _price_usd_
From column: _price_usd_
>``` python
return cleanPrice(getValue("price_usd"))
```

#### _price_usd_clean_
From column: _price_usd_
>``` python
return cleanPrice(getValue("price_usd"))
```

#### _price_usd_currency_
From column: _price_usd_
>``` python
return getCurrency(getValue("price_usd"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _description_ | `schema:description` | `schema:Offer1`|
| _price_btc_clean_ | `schema:price` | `schema:PriceSpecification1`|
| _price_btc_currency_ | `schema:priceCurrency` | `schema:PriceSpecification1`|
| _price_usd_clean_ | `schema:price` | `schema:PriceSpecification2`|
| _price_usd_currency_ | `schema:priceCurrency` | `schema:PriceSpecification2`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _seller_ | `schema:name` | `schema:ContactPoint1`|
| _ships_from_ | `schema:name` | `schema:PostalAddress1`|
| _ships_to_ | `schema:name` | `schema:PostalAddress2`|
| _src_ | `schema:url` | `schema:ImageObject1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|
| _url_ | `schema:url` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:PersonOrOrganization1` | `schema:contactPoint` | `schema:ContactPoint1`|
| `memex:PersonOrOrganization1` | `schema:memberOf` | `schema:OrganizationRole1`|
| `schema:Offer1` | `schema:availableAtOrFrom` | `schema:Place1`|
| `schema:Offer1` | `schema:eligibleRegion` | `schema:Place2`|
| `schema:Offer1` | `schema:itemOffered` | `schema:Product1`|
| `schema:Offer1` | `schema:priceSpecification` | `schema:PriceSpecification1`|
| `schema:Offer1` | `schema:priceSpecification` | `schema:PriceSpecification2`|
| `schema:Offer1` | `schema:publisher` | `schema:Organization1`|
| `schema:Offer1` | `schema:seller` | `memex:PersonOrOrganization1`|
| `schema:Organization1` | `schema:name` | `xsd:nucleuspf3izq7o6.onion`|
| `schema:OrganizationRole1` | `schema:memberOf` | `schema:Organization1`|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
| `schema:Place2` | `schema:address` | `schema:PostalAddress2`|
| `schema:Product1` | `schema:image` | `schema:ImageObject1`|