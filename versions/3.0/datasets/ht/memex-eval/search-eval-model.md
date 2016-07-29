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

#### _readability_first_date_
From column: _readability_text / values_
>``` python
return DM.date_created(getValue("values"),"0",'date')
```

#### _inferlink_postingdate_clean_
From column: _posting_date / values_
>``` python
return DM.date_created(getValue("values"),"0",'date')
```

#### _high_recall_posting_date_
From column: _high_recall_readability_text_
>``` python
return DM.date_created(getValue("high_recall_readability_text"),"0",'date')
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| __id_ | `memex:identifier` | `schema:WebPage1`|
| _age_clean_ | `memex:age` | `schema:WebPage1`|
| _business_name_ | `memex:business_name` | `schema:WebPage1`|
| _description_ | `schema:description` | `schema:WebPage1`|
| _email_ | `schema:name` | `memex:EmailAddress1`|
| _email_uri_ | `uri` | `memex:EmailAddress1`|
| _high_recall_posting_date_ | `memex:high_recall_readability_date` | `schema:WebPage1`|
| _high_recall_readability_text_ | `memex:high_recall_readability_text` | `schema:WebPage1`|
| _identifier_ | `memex:review_id` | `schema:WebPage1`|
| _inferlink_postingdate_clean_ | `memex:inferlink_date` | `schema:WebPage1`|
| _location_ | `schema:addressLocality` | `schema:WebPage1`|
| _obfuscation_ | `memex:isObfuscated` | `memex:EmailAddress1`|
| _obfuscation_ | `memex:isObfuscated` | `memex:PhoneNumber1`|
| _price_nice_ | `schema:price` | `schema:WebPage1`|
| _readability_first_date_ | `memex:readability_date` | `schema:WebPage1`|
| _seller_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _site_ | `memex:review_site` | `schema:WebPage1`|
| _telephone_ | `schema:name` | `memex:PhoneNumber1`|
| _telephone_uri_ | `uri` | `memex:PhoneNumber1`|
| _title_ | `schema:title` | `schema:WebPage1`|
| _top_level_domain_ | `memex:top_level_domain` | `schema:WebPage1`|
| _url_ | `schema:url` | `schema:WebPage1`|
| _values_ | `schema:postalCode` | `schema:WebPage1`|
| _values_ | `memex:price_per_hour` | `schema:WebPage1`|
| _values_ | `memex:inferlink_text` | `schema:WebPage1`|
| _values_ | `schema:gender` | `schema:WebPage1`|
| _values_ | `schema:name` | `schema:WebPage1`|
| _values_ | `memex:hairColor` | `schema:WebPage1`|
| _values_ | `schema:relatedLink` | `schema:WebPage1`|
| _values_ | `memex:review_site` | `schema:WebPage1`|
| _values_ | `schema:nationality` | `schema:WebPage1`|
| _values_ | `memex:ethnicity` | `schema:WebPage1`|
| _values_ | `memex:drug_use` | `schema:WebPage1`|
| _values_ | `schema:streetAddress` | `schema:WebPage1`|
| _values_ | `memex:readability_text` | `schema:WebPage1`|
| _values_ | `memex:eyeColor` | `schema:WebPage1`|
| _values_ | `schema:serviceType` | `schema:WebPage1`|
| _values_ | `memex:business_type` | `schema:WebPage1`|
| _webpage_uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:EmailAddress1` | `memex:owner` | `memex:PersonOrOrganization1`|
| `memex:PersonOrOrganization1` | `schema:telephone` | `memex:PhoneNumber1`|
| `memex:PersonOrOrganization1` | `schema:email` | `memex:EmailAddress1`|
| `memex:PhoneNumber1` | `memex:owner` | `memex:PersonOrOrganization1`|
| `schema:WebPage1` | `schema:email` | `memex:EmailAddress1`|
| `schema:WebPage1` | `schema:seller` | `memex:PersonOrOrganization1`|
| `schema:WebPage1` | `schema:telephone` | `memex:PhoneNumber1`|
