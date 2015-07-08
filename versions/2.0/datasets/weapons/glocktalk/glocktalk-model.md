## glocktalk-sample.json

### PyTransforms
#### _content_clean_
From column: _posts / content_
>``` python
return atf_body_clean(getValue("content"))
```

#### _iso_date_posted_
From column: _posts / date_posted_
>``` python
date_p = getValue("date_posted").replace("at","")
return iso8601date(date_p,"%b %d, %Y %I:%M %p")
```

#### _post_uri_
From column: _posts / post_id_
>``` python
return atf_article_uri(getValue("url"), getValue("post_id"))
```

#### _user_uri_
From column: _posts / user_id_
>``` python
return glocktalk_user_uri(getValue("user_id"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _content_clean_ | `schema:text` | `schema:WebPageElement2`|
| _iso_date_posted_ | `schema:dateCreated` | `memex:Post1`|
| _post_id_ | `schema:name` | `memex:Identifier2`|
| _post_uri_ | `uri` | `memex:Post1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `memex:Thread1`|
| _topic_id_ | `schema:name` | `memex:Identifier1`|
| _topic_title_ | `schema:text` | `schema:WebPageElement1`|
| _uri_ | `uri` | `memex:Thread1`|
| _url_ | `schema:url` | `memex:Thread1`|
| _user_id_ | `schema:name` | `memex:Identifier3`|
| _user_uri_ | `uri` | `schema:Person1`|
| _username_ | `schema:name` | `schema:Person1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Identifier1` | `memex:hasType` | `xsd:http://dig.isi.edu/weapons/data/thesaurus/identifier/glocktalk/thread`|
| `memex:Identifier2` | `memex:hasType` | `xsd:http://dig.isi.edu/weapons/data/thesaurus/identifier/glocktalk/post`|
| `memex:Identifier3` | `memex:hasType` | `xsd:http://dig.isi.edu/weapons/data/thesaurus/identifier/person/glocktalk`|
| `memex:Post1` | `memex:hasBodyPart` | `schema:WebPageElement2`|
| `memex:Post1` | `memex:identifier` | `memex:Identifier2`|
| `memex:Post1` | `schema:author` | `schema:Person1`|
| `memex:Thread1` | `memex:hasTitlePart` | `schema:WebPageElement1`|
| `memex:Thread1` | `memex:identifier` | `memex:Identifier1`|
| `memex:Thread1` | `schema:publisher` | `schema:Organization1`|
| `memex:Thread1` | `memex:hasPost` | `memex:Post1`|
| `schema:Organization1` | `schema:name` | `xsd:glocktalk.com`|
| `schema:OrganizationRole1` | `schema:memberOf` | `schema:Organization1`|
| `schema:Person1` | `memex:identifier` | `memex:Identifier3`|
| `schema:Person1` | `schema:memberOf` | `schema:OrganizationRole1`|
