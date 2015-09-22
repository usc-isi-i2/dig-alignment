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
return clean_city(getValue("values"))
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


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _adultservice_uri_ | `uri` | `memex:AdultService1`|
| _clean_age_ | `memex:personAge` | `memex:AdultService1`|
| _clean_email_ | `schema:name` | `memex:EmailAddress1`|
| _clean_eyes_ | `memex:eyeColor` | `memex:AdultService1`|
| _clean_hair_ | `memex:hairColor` | `memex:AdultService1`|
| _clean_name_ | `schema:name` | `memex:AdultService1`|
| _clean_place_name_ | `schema:name` | `schema:Place1`|
| _email_uri_ | `uri` | `memex:EmailAddress1`|
| _latitude_ | `schema:latitude` | `schema:GeoCoordinates1`|
| _longitude_ | `schema:longitude` | `schema:GeoCoordinates1`|
| _offer_uri_ | `uri` | `schema:Offer1`|
| _personororg_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _phone_uri_ | `uri` | `memex:PhoneNumber1`|
| _place_uri_ | `uri` | `schema:Place1`|
| _raw_text_ | `schema:description` | `schema:Offer1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _url_ | `schema:url` | `schema:WebPage1`|
| _webpage_uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:AdultService1` | `schema:offers` | `schema:Offer1`|
| `memex:PersonOrOrganization1` | `schema:email` | `memex:EmailAddress1`|
| `memex:PersonOrOrganization1` | `schema:telephone` | `memex:PhoneNumber1`|
| `schema:Offer1` | `schema:availableAtOrFrom` | `schema:Place1`|
| `schema:Offer1` | `schema:mainEntityOfPage` | `schema:WebPage1`|
| `schema:Offer1` | `schema:seller` | `memex:PersonOrOrganization1`|
| `schema:Offer1` | `schema:itemOffered` | `memex:AdultService1`|
| `schema:Place1` | `schema:geo` | `schema:GeoCoordinates1`|
