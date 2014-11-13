## select concat(t.title, "") as clean_title, a.* from deobf_title t, ads a where a.id=t.id limit 50

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


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
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
| `memex:FeatureCollection1` | `memex:text_title_clean_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memex.zapto.org/data/software/deobfuscator/isi/version/0.1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
