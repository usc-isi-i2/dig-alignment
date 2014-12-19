## stanford-names-sample.json

### PyTransforms
#### _ad_uri_
From column: _url_
>``` python
return getCacheBaseUrl()+"page/"+get_url_hash(getValue("url"))+"/"+getValue("ad_timestamp")+"/processed"
```

#### _featureCollection_uri_
From column: _ad_uri_
>``` python
return getValue("ad_uri")+"/featurecollection"
```

#### _name_clean_
From column: _name_
>``` python
return clean_name(getValue("name"))
```

#### _feature_uri_
From column: _name_clean_
>``` python
uri = person_name_uri(getValue("name_clean"))
if uri:
  return getValue("featureCollection_uri") + "/" + uri
return ''
```

#### _database_id_
From column: _feature_uri_
>``` python
if(getValue("name_clean")):
 return getValue("id")
return ''
```

#### _stanford_gentime_iso_
From column: _stanford_gentime_
>``` python
if getValue("name_clean"):
  return iso8601date(getValue("stanford_gentime"))
return ''
```

#### _name_clean2_
From column: _name_clean_
>``` python
return getValue("name_clean")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ad_uri_ | `uri` | `schema:WebPage1`|
| _database_id_ | `memex:databaseId` | `prov:Activity1`|
| _featureCollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _feature_uri_ | `uri` | `memex:Feature1`|
| _name_clean_ | `memex:person_name` | `memex:Feature1`|
| _name_clean2_ | `memex:featureValue` | `memex:Feature1`|
| _stanford_gentime_iso_ | `prov:endedAtTime` | `prov:Activity1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:person_name`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:person_name_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memex.zapto.org/data/software/extractor/stanford/version/1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
