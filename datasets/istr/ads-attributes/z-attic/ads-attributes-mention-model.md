## select unix_timestamp(b.importtime)*1000 as timestamp, b.url, a.* from ads_attributes a join ads b on a.ads_id=b.id  limit 10

### PyTransforms
#### _crawl_uri_
From column: _url_
>``` python
return "crawl/"+get_url_hash(getValue("url"))+"-"+getValue("timestamp")
```

#### _feature_value_
From column: _value_
>``` python
return feature_value(getValue("attribute"), getValue("value"))
```

#### _mentions_uri_
From column: _feature_value_
>``` python
return "mention/"+getValue("feature_value")+"/"+getValue("crawl_uri")
```

#### _mentions_primary_source_
From column: _crawl_uri_
>``` python
return getValue("crawl_uri")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _crawl_uri_ | `uri` | `schema:WebPage1`|
| _extractor_ | `uri` | `owl:Thing2`|
| _feature_value_ | `uri` | `owl:Thing1`|
| _mentions_primary_source_ | `uri` | `owl:Thing3`|
| _mentions_uri_ | `uri` | `memex:Mention1`|
| _url_ | `schema:url` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Mention1` | `memex:feature` | `owl:Thing1`|
| `memex:Mention1` | `prov:hadPrimarySource` | `owl:Thing3`|
| `memex:Mention1` | `prov:wasGeneratedBy` | `owl:Thing2`|
| `schema:WebPage1` | `schema:mentions` | `memex:Mention1`|
