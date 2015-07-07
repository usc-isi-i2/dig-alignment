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

#### _personOrOrganization_uri_
From column: _uri_
>``` python
return getValue("uri")+"personororganization"
```

#### _clean_phone_
From column: _contact_
>``` python
return clean_phone(getValue("contact"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _URL_ | `schema:url` | `schema:Offer1`|
| _cleanPrice_ | `schema:price` | `schema:Offer1`|
| _clean_phone_ | `schema:telephone` | `schema:ContactPoint1`|
| _description_ | `schema:description` | `schema:Offer1`|
| _personOrOrganization_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _priceCurrency_ | `schema:priceCurrency` | `schema:Offer1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|
| _user_id_ | `schema:name` | `memex:Identifier2`|
| _username_ | `schema:name` | `schema:ContactPoint1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Identifier2` | `memex:hasType` | `xsd:http://dig.isi.edu/weapons/data/thesaurus/identifier/elpasogunclassifieds`|
| `memex:PersonOrOrganization1` | `schema:contactPoint` | `schema:ContactPoint1`|
| `schema:ContactPoint1` | `memex:identifier` | `memex:Identifier2`|
| `schema:Offer1` | `schema:seller` | `memex:PersonOrOrganization1`|
