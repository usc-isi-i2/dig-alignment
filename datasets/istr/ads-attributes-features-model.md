## select unix_timestamp(b.importtime)*1000 as timestamp, b.url, a.* from ads_attributes a join ads b on a.ads_id=b.id  limit 10

### PyTransforms
#### _crawl_uri_
From column: _url_
>``` python
return "crawl/"+get_url_hash(getValue("url"))+"-"+getValue("timestamp")
```

#### _feature_name_
From column: _attribute_
>``` python
return feature_name(getValue("attribute"))
```

#### _featurecollection_uri_
From column: _crawl_uri_
>``` python
return getValue("crawl_uri")+"/featurecollection"
```

#### _feature_value_
From column: _value_
>``` python
return feature_value(getValue("attribute"), getValue("value"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _crawl_uri_ | `uri` | `schema:WebPage1`|
| _feature_name_ | `uri` | `skos:Concept1`|
| _feature_value_ | `memex:featureValue` | `memex:Feature1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `skos:Concept1`|
| `memex:FeatureCollection1` | `memex:hasFeatures` | `memex:Feature1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
