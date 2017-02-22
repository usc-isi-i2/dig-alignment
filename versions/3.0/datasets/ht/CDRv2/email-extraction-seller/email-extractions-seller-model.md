## email-extractions-sample.jl

### PyTransforms
#### _seller_uri_
From column: _url_
>``` python
return 'seller/' + SM.sha1_hash(getValue("url").strip())
```

#### _url_email_uri_
From column: _url_emails / values_
>``` python
return UM.email_uri(getValue("values"))

```

#### _text_email_uri_
From column: _text_emails / values_
>``` python
return UM.email_uri(getValue("values"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _seller_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _text_email_uri_ | `uri` | `memex:EmailAddress1`|
| _url_email_uri_ | `uri` | `memex:EmailAddress2`|
| _values_ | `schema:name` | `memex:EmailAddress2`|
| _values_ | `schema:name` | `memex:EmailAddress1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:EmailAddress1` | `memex:owner` | `memex:PersonOrOrganization1`|
| `memex:EmailAddress2` | `memex:owner` | `memex:PersonOrOrganization1`|
| `memex:PersonOrOrganization1` | `schema:email` | `memex:EmailAddress2`|
| `memex:PersonOrOrganization1` | `schema:email` | `memex:EmailAddress1`|
