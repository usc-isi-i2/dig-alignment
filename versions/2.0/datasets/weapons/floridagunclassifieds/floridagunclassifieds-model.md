## floridagunclassifieds-sample.json

### PyTransforms
#### _cleanPrice_
From column: _price_
>``` python
return cleanPrice(getValue("price"))
```

#### _priceCurrency_
From column: _price_
>``` python
return getCurrency(getValue("price"))
```

#### _listedOnDate_
From column: _Unfold: label / listed: / Values_
>``` python
return iso8601date(getValue("Values"))
```

#### _clean_member_since_
From column: _member_since_
>``` python
return iso8601date(getValue("member_since"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _URL_ | `schema:url` | `schema:Offer1`|
| _Values_ | `schema:addressLocality` | `schema:PostalAddress1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:manufacturer` | `schema:Product1`|
| _address_ | `schema:name` | `schema:PostalAddress1`|
| _cleanPrice_ | `schema:price` | `schema:Offer1`|
| _clean_member_since_ | `schema:startDate` | `schema:OrganizationRole1`|
| _description_ | `schema:description` | `schema:Offer1`|
| _listedOnDate_ | `schema:availabilityStarts` | `schema:Offer1`|
| _priceCurrency_ | `schema:priceCurrency` | `schema:Offer1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|
| _user_id_ | `schema:name` | `memex:Identifier1`|
| _username_ | `schema:name` | `schema:ContactPoint1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:PersonOrOrganization1` | `schema:contactPoint` | `schema:ContactPoint1`|
| `memex:PersonOrOrganization1` | `schema:memberOf` | `schema:OrganizationRole1`|
| `schema:ContactPoint1` | `memex:identifier` | `memex:Identifier1`|
| `schema:Offer1` | `schema:availableAtOrFrom` | `schema:Place1`|
| `schema:Offer1` | `schema:itemOffered` | `schema:Product1`|
| `schema:Offer1` | `schema:seller` | `memex:PersonOrOrganization1`|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
