## extractions-sample.json

### PyTransforms
#### _age_clean_
From column: _age / values_
>``` python
return SM.clean_age(getValue("values"))
```

#### _price_nice_
From column: _price / time_unit_
>``` python
return SearchEval.price_nice(getValue("price"), getValue("price_unit"), getValue("time_unit"))
```

#### _top_level_domain_
From column: _url_
>``` python
return SM.get_website_domain_only(getValue("url"))
```

#### _webpage_uri_
From column: __id_
>``` python
return 'webpage/' + getValue("_id")
```

#### _telephone_uri_
From column: _phone / telephone_
>``` python
return "phone/"+getValue("telephone")
```

#### _email_uri_
From column: _email / email_
>``` python
return UM.email_uri(getValue("email"))
```

#### _seller_uri_
From column: _url_
>``` python
return 'seller/' + SM.sha1_hash(getValue("url").strip())
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _age_clean_ | `memex:age` | `schema:WebPage1`|
| _business_name_ | `memex:business_name` | `schema:WebPage1`|
| _business_type_ | `memex:business_type` | `schema:WebPage1`|
| _description_ | `schema:description` | `schema:WebPage1`|
| _drug_use_ | `memex:drug_use` | `schema:WebPage1`|
| _email_ | `schema:name` | `memex:EmailAddress1`|
| _email_uri_ | `uri` | `memex:EmailAddress1`|
| _eye_color_ | `memex:eyeColor` | `schema:WebPage1`|
| _gender_ | `schema:gender` | `schema:WebPage1`|
| _hair_color_ | `memex:hairColor` | `schema:WebPage1`|
| _hyperlink_ | `schema:relatedLink` | `schema:WebPage1`|
| _inferlink_text_ | `memex:inferlink_text` | `schema:WebPage1`|
| _location_ | `schema:addressLocality` | `schema:WebPage1`|
| _name_ | `schema:name` | `schema:WebPage1`|
| _nationality_ | `schema:nationality` | `schema:WebPage1`|
| _obfuscation_ | `memex:isObfuscated` | `memex:PhoneNumber1`|
| _obfuscation_ | `memex:isObfuscated` | `memex:EmailAddress1`|
| _physical_address_ | `schema:streetAddress` | `schema:WebPage1`|
| _posting_date_ | `schema:dateCreated` | `schema:WebPage1`|
| _price_nice_ | `schema:price` | `schema:WebPage1`|
| _price_per_hour_ | `memex:price_per_hour` | `schema:WebPage1`|
| _readability_text_ | `memex:readability_text` | `schema:WebPage1`|
| _review_id_ | `memex:review_id` | `schema:WebPage1`|
| _review_site_ | `memex:review_site` | `schema:WebPage1`|
| _seller_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _telephone_ | `schema:name` | `memex:PhoneNumber1`|
| _telephone_uri_ | `uri` | `memex:PhoneNumber1`|
| _title_ | `schema:title` | `schema:WebPage1`|
| _top_level_domain_ | `memex:top_level_domain` | `schema:WebPage1`|
| _url_ | `schema:url` | `schema:WebPage1`|
| _values_ | `schema:serviceType` | `schema:WebPage1`|
| _values_ | `memex:ethnicity` | `schema:WebPage1`|
| _webpage_uri_ | `uri` | `schema:WebPage1`|
| _zipcode_ | `schema:postalCode` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:PersonOrOrganization1` | `schema:telephone` | `memex:PhoneNumber1`|
| `memex:PersonOrOrganization1` | `schema:email` | `memex:EmailAddress1`|
| `schema:WebPage1` | `schema:email` | `memex:EmailAddress1`|
| `schema:WebPage1` | `schema:telephone` | `memex:PhoneNumber1`|
