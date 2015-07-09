## ar15-sample.json

### PyTransforms
#### _content_clean_
From column: _posts / content_
>``` python
return atf_body_clean(getValue("content"))
```

#### _post_uri_
From column: _posts / post_id_
>``` python
postid = getValue("post_id")
if postid.strip() != '':
    return atf_article_uri(getValue("url"), getValue("post_id"))
else:
    return ''
```

#### _user_uri_
From column: _posts / user_id_
>``` python
return ar15_user_uri(getValue("user_id"))
```

#### _signature_clean_
From column: _posts / signature_
>``` python
return signature_clean(getValue("signature"))
```

#### _iso_date_posted_
From column: _posts / date_posted_
>``` python
return iso8601date(getValue("date_posted"),"%m/%d/%Y %I:%M:%S %p %Z")
```

#### _location_uri_
From column: _posts / location_
>``` python
return postal_address_uri(getValue("location"))
```

#### _joined_iso_
From column: _posts / Joined_
>``` python
return translate_date(getValue("Joined"), "%b %Y", "%Y-%m")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Feedback_ | `schema:ratingValue` | `schema:AggregateRating1`|
| _Posts_ | `memex:activityCount` | `schema:OrganizationRole1`|
| _content_clean_ | `schema:text` | `schema:WebPageElement2`|
| _iso_date_posted_ | `schema:dateCreated` | `memex:Post1`|
| _joined_iso_ | `schema:startDate` | `schema:OrganizationRole1`|
| _location_ | `schema:name` | `schema:PostalAddress1`|
| _location_uri_ | `uri` | `schema:Place1`|
| _post_id_ | `schema:name` | `memex:Identifier2`|
| _post_uri_ | `uri` | `memex:Post1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `memex:Thread1`|
| _signature_clean_ | `schema:text` | `schema:WebPageElement3`|
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
| `memex:Identifier1` | `memex:hasType` | `xsd:http://dig.isi.edu/weapons/data/thesaurus/identifier/ar15/thread`|
| `memex:Identifier2` | `memex:hasType` | `xsd:http://dig.isi.edu/weapons/data/thesaurus/identifier/ar15/post`|
| `memex:Identifier3` | `memex:hasType` | `xsd:http://dig.isi.edu/weapons/data/thesaurus/identifier/person/ar15`|
| `memex:Post1` | `memex:hasBodyPart` | `schema:WebPageElement2`|
| `memex:Post1` | `memex:hasSignaturePart` | `schema:WebPageElement3`|
| `memex:Post1` | `memex:identifier` | `memex:Identifier2`|
| `memex:Post1` | `schema:author` | `schema:Person1`|
| `memex:Thread1` | `memex:hasTitlePart` | `schema:WebPageElement1`|
| `memex:Thread1` | `memex:identifier` | `memex:Identifier1`|
| `memex:Thread1` | `schema:publisher` | `schema:Organization1`|
| `memex:Thread1` | `memex:hasPost` | `memex:Post1`|
| `schema:Organization1` | `schema:name` | `xsd:ar15.com`|
| `schema:OrganizationRole1` | `schema:aggregateRating` | `schema:AggregateRating1`|
| `schema:OrganizationRole1` | `schema:memberOf` | `schema:Organization1`|
| `schema:Person1` | `memex:identifier` | `memex:Identifier3`|
| `schema:Person1` | `schema:location` | `schema:Place1`|
| `schema:Person1` | `schema:memberOf` | `schema:OrganizationRole1`|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
