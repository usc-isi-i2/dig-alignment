## select unix_timestamp(a.importtime)*1000 as timestamp, a.* from ads a where a.id=1405

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

#### _phone_clean_
From column: _phone_
>``` python
return clean_phone(getValue("phone"))
```

#### _phone_uri_
From column: _phone_clean_
>``` python
return phone_uri(getValue("phone_clean"))
```

#### _phone_clean1_
From column: _phone_clean_
>``` python
return getValue("phone_clean")
```

#### _phone_feature_uri_
From column: _featurecollection_uri_
>``` python
uri = getValue("phone_uri")
if (len(uri)>0):
  return getValue("featurecollection_uri")+"/"+uri
return ''
```

#### _modetime_iso8601_
From column: _modtime_
>``` python
return iso8601date(getValue("modtime"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _crawl_uri_ | `uri` | `schema:WebPage1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _modetime_iso8601_ | `prov:endedAtTime` | `prov:Activity1`|
| _phone_clean_ | `memex:phonenumber` | `memex:Feature1`|
| _phone_clean1_ | `memex:featureValue` | `memex:Feature1`|
| _phone_feature_uri_ | `uri` | `memex:Feature1`|
| _phone_uri_ | `uri` | `memex:PhoneNumber1`|
| _snapshot_uri_ | `memex:snapshotUri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:phonenumber`|
| `memex:Feature1` | `memex:featureObject` | `memex:PhoneNumber1`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:phonenumber_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memexproxy.com/data/software/extractor/ist/version/unknown`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
