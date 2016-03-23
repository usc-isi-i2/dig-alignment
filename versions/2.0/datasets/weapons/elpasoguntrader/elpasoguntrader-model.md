## extracted_elpasoguntrader.json

### PyTransforms
#### _uri_
From column: _uri_
>``` python
return uri_from_url_timestamp(getValue("url"),getValue('timestamp'))
```

#### _priceCurrency_
From column: _price_
>``` python
return price_currency(getValue("price"))
```

#### _cleanPrice_
From column: _price_
>``` python
return price_quantity_us_number(getValue("price"))
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

#### _title_2_
From column: _title_
>``` python
return getValue("title")
```

#### _org_uri_
From column: _username_
>``` python
return uri_from_fields('organization/',getValue("username"))
```

#### _username_2_
From column: _username_
>``` python
return getValue("username")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _cleanPrice_ | `schema:price` | `schema:Offer1`|
| _clean_phone_ | `schema:name` | `memex:PhoneNumber1`|
| _description_ | `schema:description` | `schema:Offer1`|
| _org_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _organization_uri_ | `uri` | `schema:Organization1`|
| _personOrOrganization_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _priceCurrency_ | `schema:priceCurrency` | `schema:Offer1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _title_2_ | `schema:name` | `schema:Product1`|
| _uri_ | `uri` | `schema:Offer1`|
| _url_ | `schema:url` | `schema:Offer1`|
| _user_id_ | `schema:name` | `memex:Identifier2`|
| _username_ | `schema:name` | `schema:ContactPoint1`|
| _username_2_ | `schema:name` | `schema:ContactPoint1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Identifier2` | `memex:hasType` | `xsd:http://dig.isi.edu/weapons/data/thesaurus/identifier/elpasoguntrader`|
| `memex:PersonOrOrganization1` | `schema:contactPoint` | `schema:ContactPoint1`|
| `memex:PersonOrOrganization1` | `schema:memberOf` | `schema:Organization1`|
| `schema:ContactPoint1` | `memex:identifier` | `memex:Identifier2`|
| `schema:ContactPoint1` | `schema:telephone` | `memex:PhoneNumber1`|
| `schema:Offer1` | `schema:publisher` | `schema:Organization1`|
| `schema:Offer1` | `schema:seller` | `memex:PersonOrOrganization1`|
| `schema:Offer1` | `schema:itemOffered` | `schema:Product1`|
| `schema:Organization1` | `schema:name` | `xsd:elpasoguntrader.com`|
| `schema:Product1` | `schema:offers` | `schema:Offer1`|
