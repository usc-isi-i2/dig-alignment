## montanagunclassifieds-sample.json

### PyTransforms
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


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _URL_ | `schema:url` | `schema:Offer1`|
| _cleanPrice_ | `schema:price` | `schema:Offer1`|
| _description_ | `schema:description` | `schema:Offer1`|
| _expiryDate_ | `schema:availabilityEnds` | `schema:Offer1`|
| _listedOnDate_ | `schema:availabilityStarts` | `schema:Offer1`|
| _location_ | `schema:name` | `schema:PostalAddress1`|
| _priceCurrency_ | `schema:priceCurrency` | `schema:Offer1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Offer1` | `schema:availableAtOrFrom` | `schema:Place1`|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
