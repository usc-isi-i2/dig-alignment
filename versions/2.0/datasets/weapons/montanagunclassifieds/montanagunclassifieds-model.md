## extracted_montanagunclassifieds.json

### PyTransforms
#### _uri_
From column: _posted_
>``` python
return uri_from_url_timestamp(getValue("url"),getValue("timestamp"))
```

#### _priceCurrency_
From column: _Unfold: label / price / Values_
>``` python
return getCurrency(getValue("Values"))
```

#### _cleanPrice_
From column: _Unfold: label / price / Values_
>``` python
return cleanPrice(getValue("Values"))
```

#### _expiryDate_
From column: _expires_
>``` python
return iso8601date(getValue("expires"),"%B %d, %Y")
```

#### _listedOnDate_
From column: _posted_
>``` python
return iso8601date(getValue("posted"),"%B %d, %Y")
```

#### _place_uri_
From column: _uri_
>``` python
return getValue("uri")+"/placeuri"
```

#### _location_enhanced_
From column: _location_
>``` python
return getEnhancedLocation(getValue("location"))
```

#### _title_2_
From column: _title_
>``` python
return getValue("title")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _cleanPrice_ | `schema:price` | `schema:Offer1`|
| _description_ | `schema:description` | `schema:Offer1`|
| _expiryDate_ | `schema:availabilityEnds` | `schema:Offer1`|
| _listedOnDate_ | `schema:availabilityStarts` | `schema:Offer1`|
| _location_enhanced_ | `schema:name` | `schema:PostalAddress1`|
| _organizationuri_ | `uri` | `schema:Organization1`|
| _place_uri_ | `uri` | `schema:Place1`|
| _priceCurrency_ | `schema:priceCurrency` | `schema:Offer1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _title_2_ | `schema:name` | `schema:Product1`|
| _uri_ | `uri` | `schema:Offer1`|
| _url_ | `schema:url` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Offer1` | `schema:availableAtOrFrom` | `schema:Place1`|
| `schema:Offer1` | `schema:publisher` | `schema:Organization1`|
| `schema:Offer1` | `schema:itemOffered` | `schema:Product1`|
| `schema:Organization1` | `schema:name` | `xsd:montanagunclassifieds.com`|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
| `schema:Product1` | `schema:offers` | `schema:Offer1`|
