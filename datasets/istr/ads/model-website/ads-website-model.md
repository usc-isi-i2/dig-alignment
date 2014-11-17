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
if getValue("website"):
  return iso8601date(getValue("modtime"))
```

#### _website2_
From column: _website_
>``` python
return getValue("website")
```

#### _website_feature_uri_
From column: _website2_
>``` python
website = getValue("website")
if (len(website)>0):
  return getValue("featurecollection_uri")+"/" + website_uri(website)
return ''
```

#### _database_id_
From column: _modetime_iso8601_
>``` python
if getValue("website"):
  return getValue("id")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _crawl_uri_ | `uri` | `schema:WebPage1`|
| _database_id_ | `memex:databaseId` | `prov:Activity1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _modetime_iso8601_ | `prov:endedAtTime` | `prov:Activity1`|
| _website_ | `memex:website` | `memex:Feature1`|
| _website2_ | `memex:featureValue` | `memex:Feature1`|
| _website_feature_uri_ | `uri` | `memex:Feature1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:website`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:website_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memex.zapto.org/data/software/extractor/ist/version/unknown`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
