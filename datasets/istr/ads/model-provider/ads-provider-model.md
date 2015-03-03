## ads-sample.json

### PyTransforms
#### _uri_
From column: _url_
>``` python
return "page/"+get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/processed"
```

#### _featurecollection_uri_
From column: _uri_
>``` python
return getValue("uri")+"/featurecollection"
```

#### _source_name_
From column: _sources_id_
>``` python
return getWebsiteDomain(getValue("url"))
```

#### _source_name2_
From column: _source_name_
>``` python
return getValue("source_name")
```

#### _feature_uri_
From column: _source_name2_
>``` python
uri = provider_uri(getValue("source_name"))
if uri:
  return getValue("featurecollection_uri") + "/" + uri
return ''
```

#### _modtime_iso_
From column: _sources_id_
>``` python
if getValue("source_name"):
  return iso8601date(getValue("modtime"))
return ''
```

#### _database_id_
From column: _modtime_iso_
>``` python
if getValue("source_name"):
  return getValue("id")
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _database_id_ | `memex:databaseId` | `prov:Activity1`|
| _feature_uri_ | `uri` | `memex:Feature1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _modtime_iso_ | `prov:endedAtTime` | `prov:Activity1`|
| _source_name_ | `memex:featureValue` | `memex:Feature1`|
| _source_name2_ | `memex:provider_name` | `memex:Feature1`|
| _uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:provider_name`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:provider_name_feature` | `memex:Feature1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
