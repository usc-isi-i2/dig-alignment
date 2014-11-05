## ads-sample.json

### PyTransforms
#### _crawl_uri_
From column: _url_
>``` python
return "page/"+get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/processed"
```

#### _snapshot_uri_
From column: _crawl_uri_
>``` python
return "page/"+get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/raw"
```

#### _featurecollection_uri_
From column: _text_
>``` python
return getValue("crawl_uri")+"/featurecollection"
```

#### _age_clean_
From column: _age_
>``` python
return clean_age(getValue("age"))
```

#### _age_clean2_
From column: _age_clean_
>``` python
return getValue("age_clean")
```

#### _age_feature_uri_
From column: _age_clean2_
>``` python
return age_uri(getValue("age"))
```

#### _modtime_iso8601_
From column: _modtime_
>``` python
return iso8601date(getValue("modtime"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _age_clean_ | `memex:person_age` | `memex:Feature1`|
| _age_clean2_ | `memex:featureValue` | `memex:Feature1`|
| _age_feature_uri_ | `uri` | `memex:Feature1`|
| _crawl_uri_ | `uri` | `schema:WebPage1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _modtime_iso8601_ | `prov:endedAtTime` | `prov:Activity1`|
| _snapshot_uri_ | `memex:snapshotUri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureValue` | `xsd:person_age`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:person_age_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memexproxy.com/data/software/extractor/ist/version/unknown`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
