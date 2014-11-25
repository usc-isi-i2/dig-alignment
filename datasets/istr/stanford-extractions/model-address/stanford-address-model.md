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

#### _locationslist_
From column: _locations_
>``` python
return splitLocationField(getValue("locations"))
```

#### _location_clean_
From column: _locations2 / Values_
>``` python
return clean_location(getValue("Values"))
```

#### _location_clean2_
From column: _locations2 / location_clean_
>``` python
return getValue("location_clean")
```

#### _location_uri_
From column: _locations2 / location_clean2_
>``` python
return address_uri(getValue("location_clean"), '', '')
```

#### _location_feature_uri_
From column: _locations2 / location_uri_
>``` python
uri = address_uri(getValue("location_clean"), '', '')
if uri:
   return getValue("featureCollection_uri") + "/" + uri
return ''
```

#### _database_id_
From column: _locations2 / location_feature_uri_
>``` python
if getValue("location_clean"):
   return getValue("ID")
return ''
```

#### _stanford_modtime_iso_
From column: _locations2 / stanford_modtime_
>``` python
if getValue("location_clean"):
   return iso8601date(getValue("stanford_modtime"))
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _crawl_uri_ | `uri` | `schema:WebPage1`|
| _database_id_ | `memex:databaseId` | `prov:Activity1`|
| _featureCollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _location_clean_ | `memex:featureValue` | `memex:Feature1`|
| _location_clean2_ | `memex:place_postalAddress` | `memex:Feature1`|
| _location_feature_uri_ | `uri` | `memex:Feature1`|
| _location_uri_ | `uri` | `schema:PostalAddress1`|
| _stanford_modtime_iso_ | `prov:endedAtTime` | `prov:Activity1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:place_postalAddress`|
| `memex:Feature1` | `memex:featureObject` | `schema:PostalAddress1`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:place_postalAddress_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memex.zapto.org/data/software/extractor/stanford/version/0.1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
