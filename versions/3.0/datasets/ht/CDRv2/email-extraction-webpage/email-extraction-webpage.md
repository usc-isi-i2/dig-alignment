## email_sample.jl

### PyTransforms
#### _webpage_uri_
From column: _doc_id_
>``` python
return 'webpage/' + getValue("doc_id")
```

#### _title_emails_uri_
From column: _title_emails / values_
>``` python
return UM.email_uri(getValue("values"))
```

#### _text_emails_uri_
From column: _text_emails / values_
>``` python
return UM.email_uri(getValue("values"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _text_emails_uri_ | `uri` | `memex:EmailAddress1`|
| _title_emails_uri_ | `uri` | `memex:EmailAddress2`|
| _values_ | `schema:name` | `memex:EmailAddress2`|
| _values_ | `schema:name` | `memex:EmailAddress1`|
| _webpage_uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:WebPage1` | `schema:mentions` | `memex:EmailAddress1`|
| `schema:WebPage1` | `schema:mentions` | `memex:EmailAddress2`|
