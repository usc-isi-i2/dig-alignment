## ads-sample.json

### PyTransforms
#### _crawl_uri_
From column: _url_
>``` python
return "page/"+get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/processed"
```

#### _snapshot_uri_
From column: _crawl_uri_
>``` python
return "http://memex.zapto.org/data/page/"+get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/raw"
```

#### _featurecollection_uri_
From column: _text_
>``` python
return getValue("crawl_uri")+"/featurecollection"
```

#### _address_
From column: _country_
>``` python
return feature_address(getValue("city"), getValue("state"), getValue("country"))
```

#### _address2_
From column: _address_
>``` python
return getValue("address")
```

#### _address_uri_
From column: _country_
>``` python
return address_uri(getValue("city"), getValue("state"), getValue("country"))
```

#### _address_feature_uri_
From column: _address2_
>``` python
uri = getValue("address_uri")
if(len("uri") > 0):
    return getValue("featurecollection_uri")+"/" + uri
```

#### _modtime_iso8601_
From column: _modtime_
>``` python
if getValue("address_uri"):
  return iso8601date(getValue("modtime"))
```

#### _country_uri_
From column: _country_
>``` python
if getValue("country"):
  return "country/"+getValue("country")
```

#### _database_id_
From column: _modtime_iso8601_
>``` python
if getValue("address_uri"):
  return getValue("id")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _address_ | `memex:featureValue` | `memex:Feature1`|
| _address2_ | `memex:postalAddress` | `memex:Feature1`|
| _address_feature_uri_ | `uri` | `memex:Feature1`|
| _address_uri_ | `uri` | `schema:PostalAddress1`|
| _city_ | `schema:addressLocality` | `schema:PostalAddress1`|
| _country_ | `rdfs:label` | `schema:Country1`|
| _country_uri_ | `uri` | `schema:Country1`|
| _crawl_uri_ | `uri` | `schema:WebPage1`|
| _database_id_ | `memex:databaseId` | `prov:Activity1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _modtime_iso8601_ | `prov:endedAtTime` | `prov:Activity1`|
| _snapshot_uri_ | `memex:snapshotUri` | `schema:WebPage1`|
| _state_ | `schema:addressRegion` | `schema:PostalAddress1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:postalAddress`|
| `memex:Feature1` | `memex:featureObject` | `schema:PostalAddress1`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:postalAddress_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memex.zapto.org/data/software/extractor/ist/version/unknown`|
| `schema:PostalAddress1` | `schema:addressCountry` | `schema:Country1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
