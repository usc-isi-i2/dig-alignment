## add-attributes-sample-100.json

### PyTransforms
#### _crawl_uri_
From column: _url_
>``` python
return getHTBaseUrl()+"page/"+get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/processed"
```

#### _feature_collection_property_
From column: _attribute_
>``` python
fn = feature_name(getValue("attribute"))
if fn:
   return "http://memexproxy.com/ontology/"+ fn + "_feature"
```

#### _feature_name_
From column: _value_
>``` python
return feature_name(getValue("attribute"))
```

#### _feature_name_property_
From column: _feature_name_
>``` python
fn = feature_name(getValue("attribute"))
if fn:
   return "http://memexproxy.com/ontology/"+fn
return ''
```

#### _feature_value_
From column: _feature_name_property_
>``` python
return feature_value(getValue("attribute"), getValue("value"))
```

#### _feature_value2_
From column: _feature_value_
>``` python
return getValue("feature_value")
```

#### _featurecollection_uri_
From column: _crawl_uri_
>``` python
return getValue("crawl_uri")+"/featurecollection"
```

#### _modtime_iso_
From column: _modtime_
>``` python
modtime = feature_mod_time(getValue("feature_name"), getValue("feature_value"), getValue("modtime"))
if modtime:
   return iso8601date(modtime)
return ''
```

#### _database_id_
From column: _modtime_iso_
>``` python
modtime = getValue("modtime_iso")
if modtime:
  return getValue("id")
return ''
```

#### _feature_uri_
From column: _feature_value2_
>``` python
uri = getValue("feature_base_uri")
if uri:
   return getValue("featurecollection_uri") + "/" + uri
return ''
```

#### _feature_base_uri_
From column: _feature_value2_
>``` python
return feature_uri(getValue("feature_name"), getValue("feature_value"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _crawl_uri_ | `uri` | `schema:WebPage1`|
| _database_id_ | `memex:databaseId` | `prov:Activity1`|
| _feature_collection_property_ | `km-dev:objectPropertySpecialization` | `memex:FeatureCollection1`|
| _feature_name_ | `memex:featureName` | `memex:Feature1`|
| _feature_name_property_ | `km-dev:dataPropertyOfColumnLink` | `memex:Feature1`|
| _feature_uri_ | `uri` | `memex:Feature1`|
| _feature_value_ | `memex:featureValue` | `memex:Feature1`|
| _feature_value2_ | `memex:featureValue` | `memex:Feature1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _modtime_iso_ | `prov:endedAtTime` | `prov:Activity1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:hasFeatures` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://dig.isi.edu/ht/data/software/extractor/ist/attributes/version/unknown`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
