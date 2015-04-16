## evolution_2015-01-16.tsv.jl.json

### PyTransforms
#### _post_id_
From column: _url_
>``` python
m = re.search("http://.*/listings/(\d+)-", getValue("url"))
if m:
    return m.group(1)
else:
    return "0"
```

#### _post_date_
From column: _post_id_
>``` python
m = re.search("http://.*/listings/(?:\d+)-(\d{4}-\d{2}-\d{2})", getValue("url"))
if m:
    return m.group(1)
else:
    return "0"
```

#### _onion_url_
From column: _url_
>``` python
m = re.search("(http://.*.onion/listings)", getValue("url"))
if m:
    return m.group(1)
else:
    return "0"
```

#### _article_uri_
From column: _post_date_
>``` python
return atf_article_uri(getValue("onion_url")+"/"+getValue("post_date"), getValue("post_id"))
```

#### _username2_
From column: _username_
>``` python
return getValue("username")
```

#### _fc_uri_
From column: _article_uri_
>``` python
return atf_fc_uri(getValue("article_uri"))
```

#### _clean_address_
From column: _ships_from_
>``` python
return clean_address("", "", getValue("ships_from"), ",")
```

#### _clean_address2_
From column: _clean_address_
>``` python
return getValue("clean_address")
```

#### _dateCreated_
From column: _post_date_
>``` python
return atf_date_created(getValue("post_date"))
```

#### _joined_weapons_
From column: _stock_
>``` python
return get_weapons(getValue("description"), getValue("title"), getValue("stock"))
```

#### _weapons2_
From column: _weapons / Values_
>``` python
return getValue("Values")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `memex:weaponsMentioned` | `memex:Feature3`|
| _article_uri_ | `uri` | `schema:Article1`|
| _clean_address_ | `memex:featureValue` | `memex:Feature2`|
| _clean_address2_ | `memex:place_postalAddress` | `memex:Feature2`|
| _dateCreated_ | `schema:dateCreated` | `schema:Article1`|
| _description_ | `schema:text` | `schema:WebPageElement2`|
| _fc_uri_ | `uri` | `memex:FeatureCollection1`|
| _post_id_ | `rdfs:label` | `memex:Identifier1`|
| _title_ | `schema:text` | `schema:WebPageElement1`|
| _username_ | `memex:featureValue` | `memex:Feature1`|
| _username2_ | `memex:person_username` | `memex:Feature1`|
| _weapons2_ | `memex:featureValue` | `memex:Feature3`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:person_username`|
| `memex:Feature2` | `memex:featureName` | `xsd:place_postalAddress`|
| `memex:Feature3` | `memex:featureName` | `xsd:weapons_mentioned`|
| `memex:FeatureCollection1` | `memex:person_username_feature` | `memex:Feature1`|
| `memex:FeatureCollection1` | `memex:place_postalAddress_feature` | `memex:Feature2`|
| `memex:FeatureCollection1` | `memex:weaponsMentioned_feature` | `memex:Feature3`|
| `memex:Identifier1` | `memex:hasType` | `xsd:http://dig.isi.edu/data/thesauri/identifiertype/postid`|
| `schema:Article1` | `memex:hasBodyPart` | `schema:WebPageElement2`|
| `schema:Article1` | `memex:hasIdentifier` | `memex:Identifier1`|
| `schema:Article1` | `memex:hasTitlePart` | `schema:WebPageElement1`|
