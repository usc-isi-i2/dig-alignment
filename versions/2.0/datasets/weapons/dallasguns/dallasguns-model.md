## dallasguns-sample.json

### PyTransforms
#### _cleanPrice_
From column: _Unfold: label / price: / Values_
>``` python
return cleanPrice(getValue("Values"))
```

#### _currency_
From column: _Unfold: label / price: / cleanPrice_
>``` python
return getCurrency(getValue("Values"))
```

#### _cleanPhone_
From column: _Unfold: label / phone / Values_
>``` python
return clean_phone(getValue("Values"))
```

#### _placewithstate_
From column: _Unfold: label / address: / Values_
>``` python
return getValue("Values") + " Texas"
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `schema:description` | `memex:PersonOrOrganization1`|
| _Values_ | `schema:model` | `schema:Product1`|
| _Values_ | `schema:manufacturer` | `schema:Product1`|
| _Values_ | `schema:itemCondition` | `schema:Product1`|
| _Values_ | `schema:name` | `schema:ContactPoint1`|
| _cleanPhone_ | `schema:name` | `memex:PhoneNumber1`|
| _cleanPrice_ | `schema:price` | `schema:Offer1`|
| _currency_ | `schema:priceCurrency` | `schema:Offer1`|
| _description_ | `schema:description` | `schema:Offer1`|
| _listing_id_ | `schema:name` | `memex:Identifier1`|
| _placewithstate_ | `schema:name` | `schema:PostalAddress1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Identifier1` | `memex:hasType` | `xsd:http://dig.isi.edu/weapons/data/thesaurus/identifier/dallasguns`|
| `memex:PersonOrOrganization1` | `schema:contactPoint` | `schema:ContactPoint1`|
| `memex:PersonOrOrganization1` | `schema:memberOf` | `schema:OrganizationRole1`|
| `schema:ContactPoint1` | `schema:telephone` | `memex:PhoneNumber1`|
| `schema:Offer1` | `memex:identifier` | `memex:Identifier1`|
| `schema:Offer1` | `schema:availableAtOrFrom` | `schema:Place1`|
| `schema:Offer1` | `schema:itemOffered` | `schema:Product1`|
| `schema:Offer1` | `schema:seller` | `memex:PersonOrOrganization1`|
| `schema:Organization1` | `schema:name` | `xsd:dallasguns.com`|
| `schema:OrganizationRole1` | `schema:memberOf` | `schema:Organization1`|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
