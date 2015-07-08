## tennesseegunexchange-sample.json

### PyTransforms
#### _clean_member_since_
From column: _member_since_
>``` python
return iso8601date(getValue("member_since"))
```

#### _currency_
From column: _price_
>``` python
return getCurrency(getValue("price"))
```

#### _cleanPrice_
From column: _price_
>``` python
return cleanPrice(getValue("price"))
```

#### _cleanlistedon_
From column: _Unfold: label / listed: / Values_
>``` python
return iso8601date(getValue("Values"))
```

#### _cleanphone_
From column: _Unfold: label / phone: / Values_
>``` python
return clean_phone(getValue("Values"))
```

#### _cleanimages_
From column: _images / src_
>``` python
return tge_clean_image_url(getValue("src"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `schema:addressLocality` | `schema:PostalAddress1`|
| _Values_ | `schema:postalCode` | `schema:PostalAddress1`|
| _Values_ | `schema:itemCondition` | `schema:Product1`|
| _Values_ | `schema:addressRegion` | `schema:PostalAddress1`|
| _Values_ | `schema:addressCountry` | `schema:PostalAddress1`|
| _address_ | `schema:name` | `schema:PostalAddress1`|
| _cleanPrice_ | `schema:price` | `schema:Offer1`|
| _clean_member_since_ | `schema:startDate` | `schema:OrganizationRole1`|
| _cleanimages_ | `schema:url` | `schema:ImageObject1`|
| _cleanlistedon_ | `schema:availabilityStarts` | `schema:Offer1`|
| _cleanphone_ | `schema:name` | `memex:PhoneNumber1`|
| _currency_ | `schema:priceCurrency` | `schema:Offer1`|
| _description_ | `schema:description` | `schema:Offer1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|
| _url_ | `schema:url` | `schema:Offer1`|
| _user_id_ | `schema:name` | `memex:Identifier1`|
| _username_ | `schema:name` | `schema:ContactPoint1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:PersonOrOrganization1` | `schema:contactPoint` | `schema:ContactPoint1`|
| `memex:PersonOrOrganization1` | `schema:memberOf` | `schema:OrganizationRole1`|
| `schema:ContactPoint1` | `memex:identifier` | `memex:Identifier1`|
| `schema:ContactPoint1` | `schema:telephone` | `memex:PhoneNumber1`|
| `schema:Offer1` | `schema:availableAtOrFrom` | `schema:Place1`|
| `schema:Offer1` | `schema:itemOffered` | `schema:Product1`|
| `schema:Offer1` | `schema:publisher` | `schema:Organization1`|
| `schema:Offer1` | `schema:seller` | `memex:PersonOrOrganization1`|
| `schema:Organization1` | `schema:name` | `xsd:tennesseegunexchange.com`|
| `schema:OrganizationRole1` | `schema:memberOf` | `schema:Organization1`|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
| `schema:Product1` | `schema:image` | `schema:ImageObject1`|
