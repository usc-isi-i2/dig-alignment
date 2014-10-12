## x-stanford-extractions-with-modtime-and-url.tsv

### PyTransforms
#### _crawl_url_
From column: _url_
>``` python
return generateUri(getValue("modtime"), getValue("url"))
```

#### _nameslist_
From column: _names_
>``` python
return splitNameField(getValue("names"))
```

#### _phoneslist_
From column: _phones_
>``` python
return splitPhoneField(getValue("phones"))
```

#### _locationslist_
From column: _locations_
>``` python
return splitLocationField(getValue("locations"))
```

#### _name_feature_value_
From column: _names_values / Values_
>``` python
return "name/%s" % (getValue("Values"))
```

#### _phone_feature_value_
From column: _phones_values / Values_
>``` python
return "phone/%s" % (getValue("Values"))
```

#### _location_feature_value_
From column: _locations_values / Values_
>``` python
return "location/%s" % (getValue("Values"))
```

#### _name_mentions_uri_
From column: _names_values / name_feature_value_
>``` python
return "mention/%s/%s" % (getValue("name_feature_value"), getValue("crawl_url"))
```

#### _phone_mentions_uri_
From column: _phones_values / phone_feature_value_
>``` python
return "mention/%s/%s" % (getValue("phone_feature_value"), getValue("crawl_url"))
```

#### _location_mentions_uri_
From column: _locations_values / location_feature_value_
>``` python
return "mention/%s/%s" % (getValue("location_feature_value"), getValue("crawl_url"))
```

#### _extractor_
From column: _id_
>``` python
return "extractor/stanford/0.1"
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _crawl_url_ | `uri` | `schema:WebPage1`|
| _location_feature_value_ | `uri` | `owl:Thing3`|
| _location_mentions_uri_ | `uri` | `memex:Mention3`|
| _name_feature_value_ | `uri` | `owl:Thing1`|
| _name_mentions_uri_ | `uri` | `memex:Mention1`|
| _phone_feature_value_ | `uri` | `owl:Thing2`|
| _phone_mentions_uri_ | `uri` | `memex:Mention2`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Mention1` | `memex:feature` | `owl:Thing1`|
| `memex:Mention1` | `prov:wasGeneratedBy` | `xsd:http://memexproxy.com/data/extractor/stanford/0.1`|
| `memex:Mention2` | `memex:feature` | `owl:Thing2`|
| `memex:Mention2` | `prov:wasGeneratedBy` | `xsd:http://memexproxy.com/data/extractor/stanford/0.1`|
| `memex:Mention3` | `memex:feature` | `owl:Thing3`|
| `memex:Mention3` | `prov:wasGeneratedBy` | `xsd:http://memexproxy.com/data/extractor/stanford/0.1`|
| `schema:WebPage1` | `schema:mentions` | `memex:Mention2`|
| `schema:WebPage1` | `schema:mentions` | `memex:Mention3`|
| `schema:WebPage1` | `schema:mentions` | `memex:Mention1`|
