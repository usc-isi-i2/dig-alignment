## floridaguntrader-sample.json

### PyTransforms
#### _cleanprice_
From column: _price_
>``` python
return cleanPrice(getValue("price"))
```

#### _pricecurrency_
From column: _price_
>``` python
return getCurrency(getValue("price"))
```

#### _registrationdate_
From column: _member_since_
>``` python
return iso8601date(getValue("member_since"),"%B %d, %Y")
```

#### _location_
From column: _location_
>``` python
return getValue("location") + " Florida"
```

#### _placewithstate_
From column: _location_
>``` python
return getValue("location") + " Florida"
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _cleanprice_ | `schema:price` | `schema:Offer1`|
| _description_ | `schema:description` | `schema:Offer1`|
| _listing_id_ | `schema:name` | `memex:Identifier1`|
| _placewithstate_ | `schema:name` | `schema:PostalAddress1`|
| _pricecurrency_ | `schema:priceCurrency` | `schema:Offer1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _registrationdate_ | `schema:startDate` | `schema:OrganizationRole1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|
| _url_ | `schema:url` | `schema:Offer1`|
| _user_id_ | `schema:name` | `memex:Identifier2`|
| _username_ | `schema:name` | `schema:ContactPoint1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Identifier1` | `memex:hasType` | `xsd:http://dig.isi.edu/weapons/data/thesaurus/identifier/floridaguntrader`|
| `memex:Identifier2` | `memex:hasType` | `xsd:http://dig.isi.edu/weapons/data/thesaurus/identifier/floridaguntrader`|
| `memex:PersonOrOrganization1` | `schema:contactPoint` | `schema:ContactPoint1`|
| `memex:PersonOrOrganization1` | `schema:memberOf` | `schema:OrganizationRole1`|
| `schema:ContactPoint1` | `memex:identifier` | `memex:Identifier2`|
| `schema:Offer1` | `memex:identifier` | `memex:Identifier1`|
| `schema:Offer1` | `schema:availableAtOrFrom` | `schema:Place1`|
| `schema:Offer1` | `schema:seller` | `memex:PersonOrOrganization1`|
| `schema:Organization1` | `schema:name` | `xsd:floridaguntrader.com`|
| `schema:OrganizationRole1` | `schema:memberOf` | `schema:Organization1`|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
