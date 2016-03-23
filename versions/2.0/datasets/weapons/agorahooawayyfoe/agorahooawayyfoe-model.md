## extracted_agorahooawayyfoe.json

### PyTransforms
#### _uri_
From column: _url_
>``` python
return uri_from_url_timestamp(getValue("url"),getValue("timestamp"))
```

#### _cleanPrice_
From column: _price_
>``` python
return cleanPrice(getValue("price"))
```

#### _currency_
From column: _price_
>``` python
return getCurrency(getValue("price"))
```

#### _organizationuri_
From column: _raw_text_
>``` python
return uuid_uri("organization")
```

#### _contact_point_uri_
From column: _seller_
>``` python
return uuid_uri("person")
```

#### _per_org_uri_
From column: _contact_point_uri_
>``` python
return uuid_uri("organization")
```

#### _org_role_uri_
From column: _organizationuri_
>``` python
return uuid_uri("organizationrole")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _cleanPrice_ | `schema:price` | `schema:Offer1`|
| _contact_point_uri_ | `uri` | `schema:ContactPoint1`|
| _currency_ | `schema:priceCurrency` | `schema:Offer1`|
| _description_ | `schema:description` | `schema:Offer1`|
| _org_role_uri_ | `uri` | `schema:OrganizationRole1`|
| _organizationuri_ | `uri` | `schema:Organization1`|
| _per_org_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _rating_ | `schema:ratingValue` | `schema:AggregateRating1`|
| _seller_ | `schema:name` | `schema:ContactPoint1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|
| _url_ | `schema:url` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:PersonOrOrganization1` | `schema:contactPoint` | `schema:ContactPoint1`|
| `memex:PersonOrOrganization1` | `schema:memberOf` | `schema:OrganizationRole1`|
| `schema:Offer1` | `schema:aggregateRating` | `schema:AggregateRating1`|
| `schema:Offer1` | `schema:publisher` | `schema:Organization1`|
| `schema:Offer1` | `schema:seller` | `memex:PersonOrOrganization1`|
| `schema:Organization1` | `schema:name` | `xsd:agorahooawayyfoe.onion`|
| `schema:OrganizationRole1` | `schema:memberOf` | `schema:Organization1`|
