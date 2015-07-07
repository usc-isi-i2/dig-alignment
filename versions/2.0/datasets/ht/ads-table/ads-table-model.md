## ads-sample.json

### PyTransforms
#### _offer_uri_
From column: _url_
>``` python
return ht_offer_uri(getValue("url"))
```

#### _offer-version_uri_
From column: _url_
>``` python
return ht_offer_version_uri(getValue("url"),getValue("timestamp"))
```

#### _dateCreated_
From column: _timestamp_
>``` python
return iso8601date(getValue("timestamp"), "%f")
```

#### _offer_place_uri_
From column: _offer-version_uri_
>``` python
return ht_offer_place_uri(getValue("offer-version_uri"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _city_ | `schema:addressLocality` | `schema:PostalAddress1`|
| _country_ | `schema:addressCountry` | `schema:PostalAddress1`|
| _dateCreated_ | `schema:dateCreated` | `schema:Role1`|
| _offer-version_uri_ | `uri` | `schema:Offer2`|
| _offer_uri_ | `uri` | `schema:Offer1`|
| _state_ | `schema:addressRegion` | `schema:PostalAddress1`|
| _text_ | `schema:description` | `schema:Offer2`|
| _title_ | `schema:title` | `schema:Offer2`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:PersonOrOrganization1` | `schema:contactPoint` | `schema:ContactPoint1`|
| `schema:Offer1` | `memex:snapshot` | `schema:Role1`|
| `schema:Offer2` | `schema:availableAtOrFrom` | `schema:Place1`|
| `schema:Offer2` | `schema:seller` | `memex:PersonOrOrganization1`|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
| `schema:Role1` | `memex:snapshot` | `schema:Offer2`|
