## phone-extractions-sample.jl

### PyTransforms
#### _country_code_
From column: _text_phone_numbers / values_
>``` python
return PM.get_country_code(getValue("values"),'')
```

#### _text_phone_uri_
From column: _text_phone_numbers / country_code_
>``` python
return PM.phone_uri(getValue("values"), getValue('country_code'))
```

#### _title_country_code_
From column: _url_phone_numbers / values_
>``` python
return PM.get_country_code(getValue("values"),'')
```

#### _title_country_uri_
From column: _url_phone_numbers / title_country_code_
>``` python
return PM.phone_uri(getValue("values"),getValue('title_country_code'))
```

#### _seller_uri_
From column: _url_
>``` python
return 'seller/' + SM.sha1_hash(getValue("url").strip())
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _seller_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _text_phone_uri_ | `uri` | `memex:PhoneNumber1`|
| _title_country_uri_ | `uri` | `memex:PhoneNumber2`|
| _values_ | `schema:name` | `memex:PhoneNumber2`|
| _values_ | `schema:name` | `memex:PhoneNumber1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:PersonOrOrganization1` | `schema:telephone` | `memex:PhoneNumber1`|
| `memex:PersonOrOrganization1` | `schema:telephone` | `memex:PhoneNumber2`|
| `memex:PhoneNumber1` | `memex:owner` | `memex:PersonOrOrganization1`|
| `memex:PhoneNumber2` | `memex:owner` | `memex:PersonOrOrganization1`|
