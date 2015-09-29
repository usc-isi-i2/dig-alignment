## ht.json

### PyTransforms
#### _modtime_epoch_
From column: __source / modtime_
>``` python
return converTimetoEpoch(getValue("modtime"))
```

#### _posttime_epoch_
From column: __source / posttime_
>``` python
return converTimetoEpoch(getValue("posttime"))
```

#### _offer_uri_
From column: __source / url_
>``` python
uri = genericUri(getValue("posttime_epoch"),getValue("modtime_epoch"),getValue("url"))

return  uri + "/offer"
```

#### _clean_age_
From column: __source / age / values_
>``` python
return clean_age(getValue("values"))
```

#### _clean_hair_
From column: __source / hair_
>``` python
return clean_hair(getValue("hair"))
```

#### _clean_eyes_
From column: __source / eyes_
>``` python
return clean_eyes(getValue("eyes"))
```

#### _adultservice_uri_
From column: __source / offer_uri_
>``` python
uri = genericUri(getValue("posttime_epoch"),getValue("modtime_epoch"),getValue("url"))

return uri + "/adultservice"
```

#### _webpage_uri_
From column: __source / adultservice_uri_
>``` python
uri = genericUri(getValue("posttime_epoch"),getValue("modtime_epoch"),getValue("url"))

return uri + "/webpage"
```

#### _clean_phone_
From column: __source / phone / values_
>``` python
return clean_phone(getValue("values"))
```

#### _phone_uri_
From column: __source / phone / clean_phone_
>``` python
return phonenumber_uri(getValue("clean_phone"))
```

#### _clean_email_
From column: __source / email / values_
>``` python
return clean_email(getValue("values"))
```

#### _email_uri_
From column: __source / email / clean_email_
>``` python
return emailaddress_uri(getValue("clean_email"))
```

#### _clean_name_
From column: __source / name_
>``` python
return clean_name(getValue("name"))
```

#### _place_uri_
From column: __source / webpage_uri_
>``` python
uri = genericUri(getValue("posttime_epoch"),getValue("modtime_epoch"),getValue("url"))

return uri + "/place"
```

#### _clean_city_
From column: __source / city / values_
>``` python
return cleaner_city(getValue("values"))
```

#### _clean_country_
From column: __source / country_
>``` python
return clean_country(getValue("country"))
```

#### _clean_state_
From column: __source / state_
>``` python
return clean_state(getValue("state"),getValue("clean_country"))
```

#### _clean_place_name_
From column: __source / city / clean_city_
>``` python
return clean_place_name(getValue("clean_city"),getValue("clean_state"),getValue("clean_country"))
```

#### _personororg_uri_
From column: __source / place_uri_
>``` python
uri = genericUri(getValue("posttime_epoch"),getValue("modtime_epoch"),getValue("url"))

return uri + "/personororganization"
```

#### _clean_rate60_
From column: __source / rate60_
>``` python
return clean_rate(getValue("rate60"))
```

#### _clean_rate15_
From column: __source / rate15_
>``` python
return clean_rate15(getValue("rate15"))
```

#### _clean-rate30_
From column: __source / rate30_
>``` python
return clean_rate30(getValue("rate30"))
```

#### _rate_price60_
From column: __source / clean_rate60_
>``` python
return rate_price(getValue("clean_rate60"))
```

#### _rate_duration60_
From column: __source / rate_price60_
>``` python
return rate_duration(getValue("clean_rate60"))
```

#### _rate_unit60_
From column: __source / rate_duration60_
>``` python
return rate_unit(getValue("clean_rate60"))
```

#### _rate_price15_
From column: __source / clean_rate15_
>``` python
return rate_price(getValue("clean_rate15"))
```

#### _rate_duration15_
From column: __source / rate_price15_
>``` python
return rate_duration(getValue("clean_rate15"))
```

#### _rate_unit15_
From column: __source / rate_duration15_
>``` python
return rate_unit(getValue("clean_rate15"))
```

#### _rate_price30_
From column: __source / clean-rate30_
>``` python
return rate_price(getValue("clean-rate30"))
```

#### _rate_duration30_
From column: __source / rate_price30_
>``` python
return rate_duration(getValue("clean-rate30"))
```

#### _rate_unit30_
From column: __source / rate_duration30_
>``` python
return rate_unit(getValue("clean-rate30"))
```

#### _pricespecification_uri_
From column: __source / personororg_uri_
>``` python
check= getValue("clean_rate60")
if check.strip() == '':
    return ''
uri = genericUri(getValue("posttime_epoch"),getValue("modtime_epoch"),getValue("url"))

return uri + "/pricespecification"
```

#### _pricespecification_uri15_
From column: __source / pricespecification_uri_
>``` python
check= getValue("clean_rate15")
if check.strip() == '':
    return ''
uri = genericUri(getValue("posttime_epoch"),getValue("modtime_epoch"),getValue("url"))

return uri + "/pricespecification15"
```

#### _pricespecification_uri30_
From column: __source / pricespecification_uri15_
>``` python
check= getValue("clean-rate30")
if check.strip() == '':
    return ''
uri = genericUri(getValue("posttime_epoch"),getValue("modtime_epoch"),getValue("url"))

return uri + "/pricespecification30"
```

#### _publisher_
From column: __source / url_
>``` python
return getWebsiteDomainOnly(getValue("url"))
```

#### _date_created_
From column: __source / modtime_
>``` python
dt = getValue("posttime")
if dt.strip() == "":
    dt = getValue("modtime")

return dt
```

#### _valid_from_date_
From column: __source / date_created_
>``` python
return getValue("date_created")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _adultservice_uri_ | `uri` | `memex:AdultService1`|
| _clean-rate30_ | `schema:name` | `schema:PriceSpecification3`|
| _clean_age_ | `memex:personAge` | `memex:AdultService1`|
| _clean_city_ | `schema:addressLocality` | `schema:PostalAddress1`|
| _clean_country_ | `schema:addressCountry` | `schema:PostalAddress1`|
| _clean_email_ | `schema:name` | `memex:EmailAddress1`|
| _clean_eyes_ | `memex:eyeColor` | `memex:AdultService1`|
| _clean_hair_ | `memex:hairColor` | `memex:AdultService1`|
| _clean_name_ | `schema:name` | `memex:AdultService1`|
| _clean_phone_ | `schema:name` | `memex:PhoneNumber1`|
| _clean_place_name_ | `schema:name` | `schema:Place1`|
| _clean_rate15_ | `schema:name` | `schema:PriceSpecification2`|
| _clean_rate60_ | `schema:name` | `schema:PriceSpecification1`|
| _clean_state_ | `schema:addressRegion` | `schema:PostalAddress1`|
| _date_created_ | `schema:dateCreated` | `schema:WebPage1`|
| _email_uri_ | `uri` | `memex:EmailAddress1`|
| _id_ | `memex:identifier` | `schema:Offer1`|
| _latitude_ | `schema:latitude` | `schema:GeoCoordinates1`|
| _longitude_ | `schema:longitude` | `schema:GeoCoordinates1`|
| _offer_uri_ | `uri` | `schema:Offer1`|
| _personororg_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _phone_uri_ | `uri` | `memex:PhoneNumber1`|
| _place_uri_ | `uri` | `schema:Place1`|
| _pricespecification_uri_ | `uri` | `schema:PriceSpecification1`|
| _pricespecification_uri15_ | `uri` | `schema:PriceSpecification2`|
| _pricespecification_uri30_ | `uri` | `schema:PriceSpecification3`|
| _publisher_ | `schema:name` | `schema:Organization1`|
| _rate_duration15_ | `schema:name` | `schema:PriceSpecification2`|
| _rate_duration30_ | `schema:billingIncrement` | `schema:PriceSpecification3`|
| _rate_duration60_ | `schema:billingIncrement` | `schema:PriceSpecification1`|
| _rate_price15_ | `schema:price` | `schema:PriceSpecification2`|
| _rate_price30_ | `schema:price` | `schema:PriceSpecification3`|
| _rate_price60_ | `schema:price` | `schema:PriceSpecification1`|
| _rate_unit15_ | `schema:unitCode` | `schema:PriceSpecification2`|
| _rate_unit30_ | `schema:unitCode` | `schema:PriceSpecification3`|
| _rate_unit60_ | `schema:unitCode` | `schema:PriceSpecification1`|
| _raw_text_ | `schema:description` | `schema:WebPage1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _url_ | `schema:url` | `schema:WebPage1`|
| _valid_from_date_ | `schema:validFrom` | `schema:Offer1`|
| _webpage_uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:AdultService1` | `schema:offers` | `schema:Offer1`|
| `memex:EmailAddress1` | `memex:owner` | `memex:PersonOrOrganization1`|
| `memex:PersonOrOrganization1` | `schema:email` | `memex:EmailAddress1`|
| `memex:PersonOrOrganization1` | `schema:makesOffer` | `schema:Offer1`|
| `memex:PersonOrOrganization1` | `schema:telephone` | `memex:PhoneNumber1`|
| `memex:PhoneNumber1` | `memex:owner` | `memex:PersonOrOrganization1`|
| `schema:Offer1` | `schema:availableAtOrFrom` | `schema:Place1`|
| `schema:Offer1` | `schema:mainEntityOfPage` | `schema:WebPage1`|
| `schema:Offer1` | `schema:priceSpecification` | `schema:PriceSpecification1`|
| `schema:Offer1` | `schema:priceSpecification` | `schema:PriceSpecification2`|
| `schema:Offer1` | `schema:priceSpecification` | `schema:PriceSpecification3`|
| `schema:Offer1` | `schema:seller` | `memex:PersonOrOrganization1`|
| `schema:Offer1` | `schema:itemOffered` | `memex:AdultService1`|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
| `schema:Place1` | `schema:geo` | `schema:GeoCoordinates1`|
| `schema:WebPage1` | `schema:publisher` | `schema:Organization1`|
| `schema:WebPage1` | `schema:mainEntity` | `schema:Offer1`|
