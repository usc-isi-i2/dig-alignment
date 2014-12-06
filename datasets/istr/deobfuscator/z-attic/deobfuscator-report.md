## select unix_timestamp(a.importtime)*1000 as timestamp, concat(t.title, "") as clean_title, concat(b.body, "") as clean_body, a.* from ads a join deobf_title t on a.id=t.id join deobf_body b on a.id=b.id limit 50

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
return iso8601date(getValue("modtime"))
```

#### _clean_title2_
From column: _clean_title_
>``` python
return getValue("clean_title")
```

#### _database_id_
From column: _modetime_iso8601_
>``` python
if getValue("clean_title"):
    return getValue("id")
else:
    return ""
```

#### _clean_body2_
From column: _clean_body_
>``` python
return getValue("clean_body")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _clean_body_ | `memex:text_body_clean` | `memex:Feature2`|
| _clean_body2_ | `memex:featureValue` | `memex:Feature2`|
| _clean_title_ | `memex:text_title_clean` | `memex:Feature1`|
| _clean_title2_ | `memex:featureValue` | `memex:Feature1`|
| _crawl_uri_ | `uri` | `schema:WebPage1`|
| _database_id_ | `memex:databaseId` | `prov:Activity1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _modetime_iso8601_ | `prov:endedAtTime` | `prov:Activity1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:text_title_clean`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:Feature2` | `memex:featureName` | `xsd:body_title_clean`|
| `memex:FeatureCollection1` | `memex:text_title_clean_feature` | `memex:Feature1`|
| `memex:FeatureCollection1` | `memex:website_feature` | `memex:Feature2`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memex.zapto.org/data/software/deobfuscator/isi/version/0.1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
