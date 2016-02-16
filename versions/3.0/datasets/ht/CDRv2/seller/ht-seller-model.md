## ht-cdr2-seller-sample.jl

### PyTransforms
#### _seller_uri_
From column: _url_
>``` python
return 'seller/' + SM.sha1_hash(getValue("url").strip())
```

#### _clean_email_
From column: _extractions / email / results / values_
>``` python
return SM.clean_email(getValue("values"))
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
From column: _extractions / phone / results / values_
>``` python
return PM.get_country_code(getValue("values"),'')
```

#### _clean_phone_
From column: _extractions / phone / results / values_
>``` python
return PM.clean_phone(getValue("values"))
```

#### _phone_uri_
From column: _extractions / phone / results / country_code_
>``` python
phone = getValue('clean_phone').strip()
cc = getValue('country_code').strip()
if phone == ''  and cc == '':
    return ''
if cc == '':
    cc = getValue('isi_id')
return 'phone/' + cc + '-' + phone
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _clean_email_ | `schema:name` | `memex:EmailAddress1`|
| _clean_phone_ | `schema:name` | `memex:PhoneNumber1`|
| _email_uri_ | `uri` | `memex:EmailAddress1`|
| _phone_uri_ | `uri` | `memex:PhoneNumber1`|
| _seller_uri_ | `uri` | `memex:PersonOrOrganization1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:EmailAddress1` | `memex:owner` | `memex:PersonOrOrganization1`|
| `memex:PersonOrOrganization1` | `schema:telephone` | `memex:PhoneNumber1`|
| `memex:PersonOrOrganization1` | `schema:email` | `memex:EmailAddress1`|
| `memex:PhoneNumber1` | `memex:owner` | `memex:PersonOrOrganization1`|
