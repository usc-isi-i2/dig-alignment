## elpasoguntrader-sample.json

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
| _URL_ | `schema:url` | `schema:Offer1`|
| _cleanPrice_ | `schema:price` | `schema:Offer1`|
| _contact_ | `schema:telephone` | `schema:ContactPoint1`|
| _description_ | `schema:description` | `schema:Offer1`|
| _priceCurrency_ | `schema:priceCurrency` | `schema:Offer1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|
| _user_id_ | `schema:name` | `memex:Identifier2`|
| _user_rating_ | `schema:name` | `memex:Identifier1`|
| _username_ | `schema:name` | `schema:ContactPoint1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:PersonOrOrganization1` | `schema:contactPoint` | `schema:ContactPoint1`|
| `schema:ContactPoint1` | `memex:identifier` | `memex:Identifier1`|
| `schema:ContactPoint1` | `memex:identifier` | `memex:Identifier2`|
| `schema:Offer1` | `schema:seller` | `memex:PersonOrOrganization1`|
