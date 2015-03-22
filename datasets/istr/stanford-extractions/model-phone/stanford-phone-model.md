## stanford-phone-sample.json

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

#### _phone_clean_
From column: _phone_
>``` python
return clean_phone(getValue("phone"))
```

#### _phone_clean2_
From column: _phone_clean_
>``` python
return getValue("phone_clean")
```

#### _phone_uri_
From column: _phone_clean2_
>``` python
return phone_uri(getValue("phone_clean"))
```

#### _feature_uri_
From column: _phone_uri_
>``` python
uri = getValue("phone_uri")
if uri:
  return getValue("featureCollection_uri") + "/" + uri
return ''
```

#### _phone_clean3_
From column: _phone_clean2_
>``` python
return getValue("phone_clean")
```

#### _exchange_uri_
From column: _phone_uri_
>``` python
if getValue("phone_clean"):
  return phoneExchangeUri(getValue("phone_clean"))
return ''
```

#### _database_id_
From column: _feature_uri_
>``` python
if getValue("phone_clean"):
  return getValue("id")
return ''
```

#### _stanford_gentime_iso_
From column: _stanford_gentime_
>``` python
if getValue("phone_clean"):
  return iso8601date(getValue("stanford_gentime"))
return ''
```

#### _phone_cc_
From column: _phone_clean3_
>``` python
return getPhoneCountryCode(getValue("phone_clean"))
```

#### _phone_localnum_
From column: _phone_cc_
>``` python
return getLocalPhoneNumber(getValue("phone_clean"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ad_uri_ | `uri` | `schema:WebPage1`|
| _database_id_ | `memex:databaseId` | `prov:Activity1`|
| _exchange_uri_ | `uri` | `schema:Place1`|
| _featureCollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _feature_uri_ | `uri` | `memex:Feature1`|
| _phone_cc_ | `memex:countryDialingCode` | `memex:PhoneNumber1`|
| _phone_clean_ | `memex:phonenumber` | `memex:Feature1`|
| _phone_clean2_ | `memex:featureValue` | `memex:Feature1`|
| _phone_clean3_ | `rdfs:label` | `memex:PhoneNumber1`|
| _phone_localnum_ | `memex:localPhoneNumber` | `memex:PhoneNumber1`|
| _phone_uri_ | `uri` | `memex:PhoneNumber1`|
| _stanford_gentime_iso_ | `prov:endedAtTime` | `prov:Activity1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:phonenumber`|
| `memex:Feature1` | `memex:featureObject` | `memex:PhoneNumber1`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:phonenumber_feature` | `memex:Feature1`|
| `memex:PhoneNumber1` | `schema:location` | `schema:Place1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://dig.isi.edu/ht/data/software/extractor/stanford/version/1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
