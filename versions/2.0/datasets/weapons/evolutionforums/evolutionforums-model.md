## evolutionforums-sample.json

### PyTransforms
#### _uri_
From column: _url_
>``` python
return atf_thread_uri(getValue("url"))
```

#### _post_uri_
From column: _posts / post_number_
>``` python
return atf_article_uri(getValue("url"), getValue("post_id"))
```

#### _content_clean_
From column: _posts / content_
>``` python
return atf_body_clean(getValue("content"))
```

#### _signature_clean_
From column: _posts / signature_
>``` python
return signature_clean(getValue("signature"))
```

#### _iso_date_posted_
From column: _posts / date_posted_
>``` python
return iso8601date(getValue("date_posted"), "%Y-%m-%d %H:%M:%S")
```

#### _registered_iso_
From column: _posts / Unfold: label / registered / Values_
>``` python
return iso8601date(getValue("Values"), "%Y-%M-%D")
```

#### _from_clean_
From column: _posts / Unfold: label / from / Values_
>``` python
return atf_clean_from_user(getValue("Values"))
```

#### _user_uri_
From column: _posts / user_id_
>``` python
return "person/evolutionforums/" + getValue("user_id")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _content_clean_ | `schema:text` | `schema:WebPageElement3`|
| _from_clean_ | `schema:name` | `schema:Person1`|
| _iso_date_posted_ | `schema:dateCreated` | `memex:Post1`|
| _post_id_ | `schema:name` | `memex:Identifier2`|
| _post_uri_ | `uri` | `memex:Post1`|
| _registered_iso_ | `schema:startDate` | `schema:OrganizationRole1`|
| _signature_clean_ | `schema:text` | `schema:WebPageElement4`|
| _title_ | `schema:text` | `schema:WebPageElement2`|
| _topic_id_ | `schema:name` | `memex:Identifier1`|
| _topic_title_ | `schema:text` | `schema:WebPageElement1`|
| _uri_ | `uri` | `memex:Thread1`|
| _url_ | `schema:url` | `memex:Thread1`|
| _user_id_ | `schema:name` | `memex:Identifier3`|
| _user_uri_ | `uri` | `schema:Person1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Identifier1` | `memex:hasType` | `xsd:http://dig.isi.edu/weapons/data/thesaurus/identifier/evolutionforums/thread`|
| `memex:Identifier2` | `memex:hasType` | `xsd:http://dig.isi.edu/weapons/data/thesaurus/identifier/evolutionforums/post`|
| `memex:Identifier3` | `memex:hasType` | `xsd:http://dig.isi.edu/weapons/data/thesaurus/identifier/person/evolutionforums`|
| `memex:Post1` | `memex:hasBodyPart` | `schema:WebPageElement3`|
| `memex:Post1` | `memex:hasSignaturePart` | `schema:WebPageElement4`|
| `memex:Post1` | `memex:hasTitlePart` | `schema:WebPageElement2`|
| `memex:Post1` | `memex:identifier` | `memex:Identifier2`|
| `memex:Post1` | `schema:author` | `schema:Person1`|
| `memex:Thread1` | `memex:hasTitlePart` | `schema:WebPageElement1`|
| `memex:Thread1` | `memex:identifier` | `memex:Identifier1`|
| `memex:Thread1` | `schema:provider` | `schema:Organization1`|
| `memex:Thread1` | `memex:hasPost` | `memex:Post1`|
| `schema:Organization1` | `schema:name` | `xsd:evolutionforum.com`|
| `schema:OrganizationRole1` | `schema:memberOf` | `schema:Organization1`|
| `schema:Person1` | `memex:identifier` | `memex:Identifier3`|
| `schema:Person1` | `schema:memberOf` | `schema:OrganizationRole1`|
