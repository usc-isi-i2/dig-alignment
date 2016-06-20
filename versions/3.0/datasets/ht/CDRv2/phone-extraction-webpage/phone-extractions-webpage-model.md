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

#### _webpage_uri_
From column: _doc_id_
>``` python
return 'webpage/' + getValue("doc_id")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _text_phone_uri_ | `uri` | `memex:PhoneNumber1`|
| _title_country_uri_ | `uri` | `memex:PhoneNumber2`|
| _values_ | `schema:name` | `memex:PhoneNumber2`|
| _values_ | `schema:name` | `memex:PhoneNumber1`|
| _webpage_uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:WebPage1` | `schema:mentions` | `memex:PhoneNumber1`|
| `schema:WebPage1` | `schema:mentions` | `memex:PhoneNumber2`|
