## extracted_stbux7lrtpegcra2.json

### PyTransforms
#### _uri_
From column: _timestamp_
>``` python
return uri_from_url_timestamp(getValue("url"),getValue("timestamp"))
```

#### _currency_
From column: _price_
>``` python
return getCurrency(getValue("price"))
```

#### _cleanPrice_
From column: _currency_
>``` python
return cleanPrice(getValue("price"))
```

#### _contact_point_uri_
From column: _seller_
>``` python
return uuid_uri("person")
```

#### _org_uri_
From column: _contact_point_uri_
>``` python
return uuid_uri("organization")
```

#### _org_role_uri_
From column: _org_uri_
>``` python
return uuid_uri("organizationrole")
```

#### _per_org_uri_
From column: _contact_point_uri_
>``` python
return uuid_uri("organization")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `schema:name` | `schema:Place1`|
| _Values_ | `schema:name` | `schema:PostalAddress1`|
| _cleanPrice_ | `schema:price` | `schema:Offer1`|
| _contact_point_uri_ | `uri` | `schema:ContactPoint1`|
| _currency_ | `schema:priceCurrency` | `schema:Offer1`|
| _description_ | `schema:description` | `schema:Offer1`|
| _org_role_uri_ | `uri` | `schema:OrganizationRole1`|
| _org_uri_ | `uri` | `schema:Organization1`|
| _per_org_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _seller_ | `schema:name` | `schema:ContactPoint1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|
| _url_ | `schema:url` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:PersonOrOrganization1` | `schema:contactPoint` | `schema:ContactPoint1`|
| `memex:PersonOrOrganization1` | `schema:memberOf` | `schema:OrganizationRole1`|
| `schema:Offer1` | `schema:availableAtOrFrom` | `schema:Place2`|
| `schema:Offer1` | `schema:eligibleRegion` | `schema:Place1`|
| `schema:Offer1` | `schema:publisher` | `schema:Organization1`|
| `schema:Offer1` | `schema:seller` | `memex:PersonOrOrganization1`|
| `schema:OrganizationRole1` | `schema:memberOf` | `schema:Organization1`|
| `schema:Place2` | `schema:address` | `schema:PostalAddress1`|
