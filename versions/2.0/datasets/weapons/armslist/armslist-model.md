## armslist-sample.json

### PyTransforms
#### _cleanprice_
From column: _Unfold: label / price / cleanprice_
>``` python
return cleanPrice(getValue("Values"))
```

#### _currency_
From column: _Unfold: label / price / currency_
>``` python
return getCurrency(getValue("Values"))
```

#### _listedOnDate_
From column: _Unfold: label / listed on / listedOnDate_
>``` python
return iso8601date(getValue("Values"))
```

#### _cleanRegistrationDate_
From column: _Unfold: label / account / Values_
>``` python
return iso8601date(removeAlpha(getValue("Values")).strip(),"%m/%d/%Y")
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


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `schema:category` | `schema:Product1`|
| _Values_ | `schema:description` | `memex:PersonOrOrganization1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:manufacturer` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _cleanprice_ | `schema:price` | `schema:Offer1`|
| _currency_ | `schema:priceCurrency` | `schema:Offer1`|
| _description_ | `schema:description` | `schema:Offer1`|
| _listedOnDate_ | `schema:availabilityStarts` | `schema:Offer1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _title_ | `schema:name` | `schema:Offer1`|
| _transactionActor_ | `km-dev:objectPropertySpecialization` | `schema:Offer1`|
| _transactionType_ | `km-dev:columnSubClassOfLink` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Offer1` | `schema:itemOffered` | `schema:Product1`|
| `schema:Offer1` | `schema:seller` | `memex:PersonOrOrganization1`|
