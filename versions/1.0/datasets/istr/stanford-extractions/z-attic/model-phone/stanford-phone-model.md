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

#### _phoneslist_
From column: _phones_
>``` python
return splitPhoneField(getValue("phones"))
```

#### _phone_clean_
From column: _phones2 / Values_
>``` python
return clean_phone(getValue("Values"))
```

#### _phone_clean2_
From column: _phones2 / phone_clean_
>``` python
return getValue("phone_clean")
```

#### _phone_uri_
From column: _phones2 / phone_clean2_
>``` python
uri = phone_uri(getValue("phone_clean"))
if uri:
   return getValue("featureCollection_uri") + "/" + uri
```

#### _phone_label_
From column: _phones2 / phone_uri_
>``` python
return getValue("phone_clean")
```

#### _phone_uri2_
From column: _phones2 / phone_label_
>``` python
return phone_uri(getValue("phone_clean"))
```

#### _exchange_uri_
From column: _phones2 / phone_uri2_
>``` python
if getValue("phone_clean"):
  return phoneExchangeUri(getValue("phone_clean"))
```

#### _database_id_
From column: _phones2 / exchange_uri_
>``` python
if getValue("phone_clean"):
  return getValue("ID")
return ''
```

#### _stanford_gentime_iso_
From column: _phones2 / stanford_gentime_
>``` python
if getValue("phone_clean"):
  return iso8601date(getValue("stanford_gentime"))
return ''

```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _crawl_uri_ | `uri` | `schema:WebPage1`|
| _database_id_ | `memex:databaseId` | `prov:Activity1`|
| _exchange_uri_ | `uri` | `schema:Place1`|
| _featureCollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _phone_clean_ | `memex:featureValue` | `memex:Feature1`|
| _phone_clean2_ | `memex:phonenumber` | `memex:Feature1`|
| _phone_label_ | `rdfs:label` | `memex:PhoneNumber1`|
| _phone_uri_ | `uri` | `memex:Feature1`|
| _phone_uri2_ | `uri` | `memex:PhoneNumber1`|
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
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memex.zapto.org/data/software/extractor/stanford/version/0.1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
