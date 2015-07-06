## blueridgefirearms-sample.json

### PyTransforms
#### _priceCurrency_
From column: _price_
>``` python
return getCurrency(getValue("price"))
```

#### _cleanPrice_
From column: _price_
>``` python
return cleanPrice(getValue("price"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _SKU_ | `schema:sku` | `schema:Offer1`|
| _URL_ | `schema:url` | `schema:Offer1`|
| _cleanPrice_ | `schema:price` | `schema:Offer1`|
| _description_ | `schema:description` | `schema:Offer1`|
| _manufacturer_ | `schema:manufacturer` | `schema:Product1`|
| _manufacturer_no_ | `schema:keywords` | `schema:Product1`|
| _priceCurrency_ | `schema:priceCurrency` | `schema:Offer1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Offer1` | `schema:itemOffered` | `schema:Product1`|
