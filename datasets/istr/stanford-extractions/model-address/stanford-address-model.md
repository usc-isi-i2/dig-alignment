## stanford-address-sample.json

### PyTransforms
#### _ad_uri_
From column: _url_
>``` python
return getHTBaseUrl()+"page/"+get_url_hash(getValue("url"))+"/"+getValue("ad_timestamp")+"/processed"
```

#### _featureCollection_uri_
From column: _ad_uri_
>``` python
return getValue("ad_uri")+"/featurecollection"
```

#### _location_clean_
From column: _location_
>``` python
return clean_location(getValue("location"))
```

#### _location_clean2_
From column: _location_clean_
>``` python
return getValue("location_clean")
```

#### _location_clean3_
From column: _location_clean2_
>``` python
return getValue("location_clean")
```

#### _database_id_
From column: _location_clean3_
>``` python
if getValue("location_clean"):
  return getValue("id")
return ''
```

#### _stanford_gentime_iso_
From column: _stanford_gentime_
>``` python
if getValue("location_clean"):
  return iso8601date(getValue("stanford_gentime"))
return ''
```

#### _feature_uri_
From column: _location_
>``` python
lc = getValue("location")
if lc:
  return getValue("featureCollection_uri") + "/" + address_uri(lc,'','')
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ad_uri_ | `uri` | `schema:WebPage1`|
| _database_id_ | `memex:databaseId` | `prov:Activity1`|
| _featureCollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _feature_uri_ | `uri` | `memex:Feature1`|
| _location_clean_ | `memex:featureValue` | `memex:Feature1`|
| _location_clean2_ | `memex:place_postalAddress` | `memex:Feature1`|
| _location_clean3_ | `rdfs:label` | `schema:PostalAddress1`|
| _stanford_gentime_iso_ | `prov:endedAtTime` | `prov:Activity1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:place_postalAddress`|
| `memex:Feature1` | `memex:featureObject` | `schema:PostalAddress1`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:place_postalAddress_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://dig.isi.edu/ht/data/software/extractor/stanford/version/1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
