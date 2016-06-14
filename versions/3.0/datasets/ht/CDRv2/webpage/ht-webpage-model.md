## cdr_with_name.jl

### PyTransforms
#### _webpage_uri_
From column: _isi_id_
>``` python
return 'webpage/' + getValue("isi_id")
```

#### _clean_text_
From column: _extractions / text / results / values_
>``` python
return HM.clean_html_tags(getValue("values"))
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
ts = getValue("timestamp")
return DM.epoch_to_iso8601(ts)
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

#### _phone_uri_
From column: _extractions / phone / results / values_
>``` python
cc = PM.get_country_code(getValue("values"),'')
phone = PM.clean_phone(getValue("values"))
if phone == ''  and cc == '':
    return ''
if cc == '':
    cc = getValue('isi_id')
return 'phone/' + cc + '-' + phone
```

#### _title_email_
From column: _extractions / title / results / values_
>``` python
return EE.extract_email(getValue("values"), True)
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

#### _title_email_uri_
From column: _extractions / title / results / title_email_split / Values_
>``` python
email = getValue("Values")
if email != '':
    return 'email/' + email
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _clean_text_ | `schema:description` | `schema:WebPage1`|
| _domain_url_ | `schema:name` | `schema:Organization1`|
| _iso_finaltime_ | `schema:dateCreated` | `schema:WebPage1`|
| _organization_domain_uri_ | `uri` | `schema:Organization1`|
| _phone_uri_ | `uri` | `memex:PhoneNumber1`|
| _text_email_uri_ | `uri` | `memex:EmailAddress1`|
| _title_email_uri_ | `uri` | `memex:EmailAddress2`|
| _url_ | `schema:url` | `schema:WebPage1`|
| _values_ | `schema:name` | `schema:WebPage1`|
| _webpage_uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:EmailAddress1` | `memex:isMentionedIn` | `schema:WebPage1`|
| `memex:EmailAddress2` | `memex:isMentionedIn` | `schema:WebPage1`|
| `memex:PhoneNumber1` | `memex:isMentionedIn` | `schema:WebPage1`|
| `schema:WebPage1` | `schema:mentions` | `memex:EmailAddress1`|
| `schema:WebPage1` | `schema:mentions` | `memex:EmailAddress2`|
| `schema:WebPage1` | `schema:mentions` | `memex:PhoneNumber1`|
| `schema:WebPage1` | `schema:publisher` | `schema:Organization1`|
