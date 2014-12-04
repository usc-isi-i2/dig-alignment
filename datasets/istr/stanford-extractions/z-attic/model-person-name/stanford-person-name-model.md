## stanford-features-sample.json

### PyTransforms
#### _crawl_uri_
From column: _url_
>``` python
return getCacheBaseUrl()+"page/"+get_url_hash(getValue("url"))+"/"+getValue("ad_timestamp")+"/processed"
```

#### _featureCollection_uri_
From column: _crawl_uri_
>``` python
return getValue("crawl_uri")+"/featurecollection"
```

#### _nameslist_
From column: _names_
>``` python
return splitNameField(getValue("names"))
```

#### _clean_name_
From column: _names2 / Values_
>``` python
return clean_name(getValue("Values"))
```

#### _clean_name2_
From column: _names2 / clean_name_
>``` python
return getValue("clean_name")
```

#### _name_uri_
From column: _names2 / clean_name2_
>``` python
return person_name_uri(getValue("clean_name"))
```

#### _database_id_
From column: _names2 / name_uri_
>``` python
if getValue("clean_name"):
  return getValue("ID")
return ""
```

#### _iso_stanford_modtime_
From column: _names2 / stanford_modtime_
>``` python
if getValue("clean_name"):
   return iso8601date(getValue("stanford_modtime"))
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _clean_name_ | `memex:person_name` | `memex:Feature1`|
| _clean_name2_ | `memex:featureValue` | `memex:Feature1`|
| _crawl_uri_ | `uri` | `schema:WebPage1`|
| _database_id_ | `memex:databaseId` | `prov:Activity1`|
| _featureCollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _iso_stanford_modtime_ | `prov:endedAtTime` | `prov:Activity1`|
| _name_uri_ | `uri` | `memex:Feature1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:person_name`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:person_name_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memex.zapto.org/data/software/extractor/stanford/version/0.1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
