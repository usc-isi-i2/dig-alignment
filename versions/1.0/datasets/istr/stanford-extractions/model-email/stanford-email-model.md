## stanford-email-sample.json

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

#### _email_clean_
From column: _email_
>``` python
return clean_email(getValue("email"))
```

#### _email_clean2_
From column: _email_clean_
>``` python
return getValue("email_clean")
```

#### _feature_uri_
From column: _email_
>``` python
uri = emailaddress_uri(getValue("email"))
if uri:
  return getValue("featureCollection_uri") + "/" + uri
return ''
```

#### _database_id_
From column: _email_clean2_
>``` python
if getValue("email_clean"):
  return getValue("id")
return ''
```

#### _stanford_gentime_iso_
From column: _stanford_gentime_
>``` python
if getValue("email_clean"):
  return iso8601date(getValue("stanford_gentime"))
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ad_uri_ | `uri` | `schema:WebPage1`|
| _database_id_ | `memex:databaseId` | `prov:Activity1`|
| _email_clean_ | `memex:emailaddress` | `memex:Feature1`|
| _email_clean2_ | `memex:featureValue` | `memex:Feature1`|
| _featureCollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _feature_uri_ | `uri` | `memex:Feature1`|
| _stanford_gentime_iso_ | `prov:endedAtTime` | `prov:Activity1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:emailaddress`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:emailaddress_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://dig.isi.edu/ht/data/software/extractor/stanford/version/1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
