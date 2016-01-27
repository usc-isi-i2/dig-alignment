## ht-cdr2-ads-500.jl

### PyTransforms
#### _seller_uri_
From column: _url_
>``` python
return 'seller/' + SM.sha1_hash(getValue("url").strip())
```

#### _clean_email_
From column: _extractions / email / results / value_
>``` python
return SM.clean_email(getValue("value"))
```

#### _email_uri_
From column: _extractions / email / results / clean_email_
>``` python
email = getValue('clean_email')
if email != '':
    return 'email/' + email
return ''
```

#### _country_code_
From column: _extractions / Glue_1 / Glue_1 / extractions_Glue_1_extractions_country_results_values_
>``` python
return PM.get_country_code(getValue("extractions_Glue_1_extractions_phone_results_values"),getValue("extractions_Glue_1_extractions_country_results_values"))
```

#### _phone_uri_
From column: _extractions / Glue_1 / Glue_1 / country_code_
>``` python
cc = getValue("country_code")
phone = getValue("extractions_Glue_1_extractions_phone_results_values")
if len(phone) > 20:
    return ''
prefix = 'phone/'
if phone != '':
    if cc != '':
        return prefix + cc + '-' + phone
    else:
        return prefix + getValue('isi_id') + '-' + phone
return ''




```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _adultservice_uri_ | `uri` | `memex:AdultService1`|
| _author_ | `schema:name` | `memex:UserName1`|
| _clean_age_ | `memex:age` | `memex:AdultService1`|
| _clean_email_ | `schema:name` | `memex:EmailAddress1`|
| _clean_email_ | `schema:name` | `memex:EmailAddress1`|
| _clean_ethnicity_ | `memex:ethnicity` | `memex:AdultService1`|
| _clean_height_ | `schema:height` | `memex:AdultService1`|
| _clean_name_ | `schema:name` | `memex:AdultService1`|
| _clean_weight_ | `schema:weight` | `memex:AdultService1`|
| _email_uri_ | `uri` | `memex:EmailAddress1`|
| _email_uri_ | `uri` | `memex:EmailAddress1`|
| _eventTime_ | `schema:startDate` | `schema:Event1`|
| _eventType_ | `km-dev:columnSubClassOfLink` | `schema:Event1`|
| _extractions_Glue_1_extractions_phone_results_values_ | `schema:name` | `memex:PhoneNumber1`|
| _extractions_Glue_1_extractions_phone_results_values_ | `schema:name` | `memex:PhoneNumber1`|
| _lat_ | `schema:latitude` | `schema:GeoCoordinates1`|
| _lon_ | `schema:longitude` | `schema:GeoCoordinates1`|
| _person_uri_ | `uri` | `schema:Person1`|
| _phone_uri_ | `uri` | `memex:PhoneNumber1`|
| _phone_uri_ | `uri` | `memex:PhoneNumber1`|
| _seller_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _seller_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _sentence_ | `schema:text` | `schema:CreativeWork1`|
| _sentiment_ | `memex:polarityValue` | `memex:Sentiment1`|
| _values_ | `schema:name` | `schema:CreativeWork1`|
| _values_ | `schema:name` | `schema:CreativeWork1`|
| _values_ | `schema:name` | `schema:Person2`|
| _values_ | `schema:name` | `memex:Topic1`|
| _values_ | `schema:mentions` | `schema:CreativeWork1`|
| _values_ | `schema:name` | `schema:Place1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:EmailAddress1` | `memex:owner` | `memex:PersonOrOrganization1`|
| `memex:PersonOrOrganization1` | `schema:telephone` | `memex:PhoneNumber1`|
| `memex:PersonOrOrganization1` | `schema:email` | `memex:EmailAddress1`|
| `memex:PhoneNumber1` | `memex:owner` | `memex:PersonOrOrganization1`|
