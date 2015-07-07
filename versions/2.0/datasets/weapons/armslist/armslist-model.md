## armslist-sample.json

### PyTransforms
#### _label_fields_
From column: _fields / label_
>``` python
return getValue("label")
```

#### _label_info_
From column: _info / label_
>``` python
return getValue("label")
```

#### _transactionType_
From column: _title_
>``` python
return getTransactionType(getValue("title"))
```

#### _transactionActor_
From column: _transactionType_
>``` python
return getTransactionActor(getValue("transactionType"))
```

#### _cleanRegistrationDate_
From column: _Unfold: label_info / account / Values_
>``` python
return iso8601date(removeAlpha(getValue("Values")).strip(),"%m/%d/%Y")
```

#### _listedOnDate_
From column: _Unfold: label_info / listed on / Values_
>``` python
return iso8601date(getValue("Values"))
```

#### _currency_
From column: _Unfold: label_info / price / Values_
>``` python
return getCurrency(getValue("Values"))
```

#### _cleanPrice_
From column: _Unfold: label_info / price / Values_
>``` python
return cleanPrice(getValue("Values"))
```

#### _cleanimgurl_
From column: _images / src_
>``` python
return al_clean_image_url(getValue("src"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `schema:category` | `schema:Product1`|
| _Values_ | `schema:name` | `schema:PostalAddress1`|
| _Values_ | `schema:manufacturer` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:description` | `memex:PersonOrOrganization1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _cleanPrice_ | `schema:price` | `schema:Offer1`|
| _cleanRegistrationDate_ | `schema:startDate` | `schema:OrganizationRole1`|
| _cleanimgurl_ | `schema:url` | `schema:ImageObject1`|
| _currency_ | `schema:priceCurrency` | `schema:Offer1`|
| _description_ | `schema:description` | `schema:Offer1`|
| _listedOnDate_ | `schema:availabilityStarts` | `schema:Offer1`|
| _listing_id_ | `schema:name` | `memex:Identifier1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _title_ | `schema:name` | `schema:Offer1`|
| _transactionActor_ | `km-dev:objectPropertySpecialization` | `schema:Offer1`|
| _transactionType_ | `km-dev:columnSubClassOfLink` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|
| _url_ | `schema:url` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Identifier1` | `memex:hasType` | `xsd:http://dig.isi.edu/weapons/data/thesaurus/identifier/armslist`|
| `memex:PersonOrOrganization1` | `schema:memberOf` | `schema:OrganizationRole1`|
| `schema:Offer1` | `memex:identifier` | `memex:Identifier1`|
| `schema:Offer1` | `schema:availableAtOrFrom` | `schema:Place1`|
| `schema:Offer1` | `schema:itemOffered` | `schema:Product1`|
| `schema:Offer1` | `schema:publisher` | `schema:Organization1`|
| `schema:Offer1` | `schema:seller` | `memex:PersonOrOrganization1`|
| `schema:Organization1` | `schema:name` | `xsd:armslist.com`|
| `schema:OrganizationRole1` | `schema:memberOf` | `schema:Organization1`|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
| `schema:Product1` | `schema:image` | `schema:ImageObject1`|
