## cdr_test_email.jl

### PyTransforms
#### _clean_phone_
From column: _extractions / phone / results / values_
>``` python
return PM.clean_phone(getValue("values"))
```

#### _country_code_
From column: _extractions / phone / results / values_
>``` python
return PM.get_country_code(getValue("values"),'')
```

#### _phone_uri_
From column: _extractions / phone / results / clean_phone_
>``` python
phone = getValue('clean_phone').strip()
cc = getValue('country_code').strip()
if phone == ''  and cc == '':
    return ''
if cc == '':
    cc = "x"
return 'phone/' + cc + '-' + phone
```

#### _clean_text_
From column: _extractions / text / results / values_
>``` python
return HM.clean_html_tags(getValue("values"))
```

#### _text_email_
From column: _extractions / text / results / clean_text_
>``` python
return EE.extract_email(getValue("clean_text"), True)
```

#### _text_email_uri_
From column: _extractions / text / results / text_email_split / Values_
>``` python
email = getValue("Values")
if email != '':
    return 'email/' + email
```

#### _clean_title_
From column: _extractions / title / results / values_
>``` python
return HM.clean_html_tags(getValue("values"))
```

#### _title_email_
From column: _extractions / title / results / clean_title_
>``` python
return EE.extract_email(getValue("clean_title"), True)
```

#### _title_email_uri_
From column: _extractions / title / results / title_email_split / Values_
>``` python
email = getValue("Values")
if email != '':
    return 'email/' + email
```

#### _iso_posttime_
From column: _extractions / posttime / results / values_
>``` python
posttime = getValue("values")
if posttime.strip() != '':
    return DM.iso8601date(posttime)
return ''
```

#### _iso_posttime2_
From column: _crawl_data / context / timestamp_
>``` python
return DM.epoch_to_iso8601(getValue("timestamp"))
```

#### _iso_crawltime_
From column: _extractions / posttime / results / iso_posttime_
>``` python
return getValueFromNestedColumnByIndex("crawl_data", "context/iso_posttime2",0)
```

#### _iso_finaltime_
From column: _extractions / posttime / results / iso_crawltime_
>``` python
posttime = getValue("iso_posttime")
if posttime != '':
    return posttime
return getValue("iso_crawltime")
```

#### _domain_url_
From column: _url_
>``` python
return SM.get_website_domain_only(getValue("url"))
```

#### _organization_domain_uri_
From column: _domain_url_
>``` python
return 'organization/' + getValue("domain_url")
```

#### _webpage_uri_
From column: _isi_id_
>``` python
return 'webpage/' + getValue("isi_id")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _clean_text_ | `schema:description` | `schema:WebPage1`|
| _clean_title_ | `schema:name` | `schema:WebPage1`|
| _domain_url_ | `schema:name` | `schema:Organization1`|
| _iso_finaltime_ | `schema:dateCreated` | `schema:WebPage1`|
| _organization_domain_uri_ | `uri` | `schema:Organization1`|
| _phone_uri_ | `uri` | `memex:PhoneNumber1`|
| _text_email_uri_ | `uri` | `memex:EmailAddress2`|
| _title_email_uri_ | `uri` | `memex:EmailAddress1`|
| _url_ | `schema:url` | `schema:WebPage1`|
| _webpage_uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:WebPage1` | `schema:mentions` | `memex:EmailAddress1`|
| `schema:WebPage1` | `schema:mentions` | `memex:EmailAddress2`|
| `schema:WebPage1` | `schema:mentions` | `memex:PhoneNumber1`|
| `schema:WebPage1` | `schema:publisher` | `schema:Organization1`|
