## extracted_carolinabargaintrader.json

### PyTransforms
#### _uri_
From column: _crawler_
>``` python
return uri_from_url_timestamp(getValue("url"),getValue("timestamp"))
```

#### _listedondate_
From column: _ad_began_
>``` python
return iso8601date(getValue("ad_began"),"%m/%d/%y")
```

#### _clean_alt_phone_
From column: _alt_phone_
>``` python
return clean_phone(getValue("alt_phone"))
```

#### _clean_image_url_
From column: _images / src_
>``` python
return cbt_clean_image_url(getValue("src"))
```

#### _clean_member_since_
From column: _member_since_
>``` python
return iso8601date(getValue("member_since"),"%m/%d/%y")
```

#### _clean_phone_
From column: _phone_
>``` python
return clean_phone(getValue("phone"))
```

#### _currency_
From column: _price_
>``` python
return getCurrency(getValue("price"))
```

#### _clean_price_
From column: _price_
>``` python
return cleanPrice(getValue("price"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _clean_alt_phone_ | `schema:name` | `memex:PhoneNumber2`|
| _clean_image_url_ | `schema:url` | `schema:ImageObject1`|
| _clean_member_since_ | `schema:startDate` | `schema:OrganizationRole1`|
| _clean_phone_ | `schema:name` | `memex:PhoneNumber1`|
| _clean_price_ | `schema:price` | `schema:Offer1`|
| _currency_ | `schema:priceCurrency` | `schema:Offer1`|
| _description_ | `schema:description` | `schema:Offer1`|
| _listedondate_ | `schema:availabilityStarts` | `schema:Offer1`|
| _location_ | `schema:name` | `schema:PostalAddress1`|
| _organization_uri_ | `uri` | `schema:Organization1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _serial_number_ | `schema:serialNumber` | `schema:Product1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|
| _url_ | `schema:url` | `schema:Offer1`|
| _username_ | `schema:name` | `schema:ContactPoint1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:PersonOrOrganization1` | `schema:contactPoint` | `schema:ContactPoint1`|
| `memex:PersonOrOrganization1` | `schema:memberOf` | `schema:OrganizationRole1`|
| `schema:ContactPoint1` | `schema:telephone` | `memex:PhoneNumber1`|
| `schema:ContactPoint1` | `schema:telephone` | `memex:PhoneNumber2`|
| `schema:Offer1` | `schema:availableAtOrFrom` | `schema:Place1`|
| `schema:Offer1` | `schema:itemOffered` | `schema:Product1`|
| `schema:Offer1` | `schema:publisher` | `schema:Organization1`|
| `schema:Offer1` | `schema:seller` | `memex:PersonOrOrganization1`|
| `schema:Organization1` | `schema:name` | `xsd:carolinabargaintrader.net`|
| `schema:OrganizationRole1` | `schema:memberOf` | `schema:Organization1`|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
| `schema:Product1` | `schema:image` | `schema:ImageObject1`|
| `schema:Product1` | `schema:offers` | `schema:Offer1`|
