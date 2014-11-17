## ads-sample.json

### PyTransforms
#### _crawl_uri_
From column: _url_
>``` python
return "page/"+get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/processed"
```

#### _featurecollection_uri_
From column: _text_
>``` python
return getValue("crawl_uri")+"/featurecollection"
```

#### _modetime_iso8601_
From column: _modtime_
>``` python
if getValue("email_clean"):
  return iso8601date(getValue("modtime"))
```

#### _email_clean_
From column: _email_
>``` python
return clean_email(getValue("email"))
```

#### _email_clean2_
From column: _email_clean_
>``` python
return clean_email(getValue("email"))
```

#### _email_feature_uri_
From column: _email_clean2_
>``` python
uri = emailaddress_uri(getValue("email"))
if uri:
  return getValue("featurecollection_uri")+"/"+uri
return ''
```

#### _database_id_
From column: _id_
>``` python
if getValue("email_clean"):
  return getValue("id")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _crawl_uri_ | `uri` | `schema:WebPage1`|
| _database_id_ | `memex:databaseId` | `prov:Activity1`|
| _email_clean_ | `memex:emailaddress` | `memex:Feature1`|
| _email_clean2_ | `memex:featureValue` | `memex:Feature1`|
| _email_feature_uri_ | `uri` | `memex:Feature1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _modetime_iso8601_ | `prov:endedAtTime` | `prov:Activity1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:emailaddress`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:emailaddress_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memex.zapto.org/data/software/extractor/ist/version/unknown`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
