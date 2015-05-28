## webpage-sample.json

### PyTransforms
#### _import_time_
From column: _import_time_
>``` python
return iso8601date(getValue("importime"), "%f")
```

#### _cache_uri_
From column: _cache_uri_
>``` python
return "page/"+get_url_hash(getValue("url"))+"/"+getValue("importime")+"/processed"
```

#### _snapshot_uri_
From column: _snapshot_uri_
>``` python
return getHTBaseUrl() + "page/"+get_url_hash(getValue("url"))+"/"+getValue("importime")+"/raw"
```

#### _featurecollection_uri_
From column: _featurecollection_uri_
>``` python
return getValue("cache_uri")+"/featurecollection"
```

#### _website2_
From column: _website / website2_
>``` python
return getValue("values")
```

#### _website_feature_uri_
From column: _website / website_feature_uri_
>``` python
website = getValue("values")
if (len(website)>0):
  return getValue("featurecollection_uri")+"/" + website_uri(website)
return ''
```

#### _body_uri_
From column: _body_uri_
>``` python
if getValue("bodytext"):
  return getValue("cache_uri") + "/body"
return ''
```

#### _title_uri_
From column: _title_uri_
>``` python
if getValue("title"):
  return getValue("cache_uri") + "/title"
return ''
```

#### _age_clean_
From column: _age / age_clean_
>``` python
return clean_age(getValue("values"))
```

#### _age_clean2_
From column: _age / age_clean2_
>``` python
return getValue("age_clean")
```

#### _age_feature_uri_
From column: _age / age_feature_uri_
>``` python
if getValue("age_clean"):
  return getValue("featurecollection_uri")+"/"+age_uri(getValue("age_clean"))
return ''
```

#### _phone_clean_
From column: _phone / phone_clean_
>``` python
return clean_phone(getValue("values"))
```

#### _phone_uri_
From column: _phone / phone_uri_
>``` python
return phone_uri(getValue("phone_clean"))
```

#### _phone_clean1_
From column: _phone / phone_clean1_
>``` python
return getValue("phone_clean")
```

#### _phone_clean2_
From column: _phone / phone_clean2_
>``` python
return getValue("phone_clean")
```

#### _phone_local_
From column: _phone / phone_local_
>``` python
return getLocalPhoneNumber(getValue("phone_clean"))
```

#### _phone_cc_
From column: _phone / phone_cc_
>``` python
return getPhoneCountryCode(getValue("phone_clean"))
```

#### _phone_feature_uri_
From column: _phone / phone_feature_uri_
>``` python
uri = getValue("phone_uri")
if (len(uri)>0):
  return getValue("featurecollection_uri")+"/"+uri
return ''
```

#### _email_clean_
From column: _email / email_clean_
>``` python
return clean_email(getValue("values"))
```

#### _email_clean2_
From column: _email / email_clean2_
>``` python
return clean_email(getValue("values"))
```

#### _email_feature_uri_
From column: _email / email_feature_uri_
>``` python
uri = emailaddress_uri(getValue("values"))
if uri:
  return getValue("featurecollection_uri")+"/"+uri
return ''
```

#### _image_uri_
From column: _images / image_uri_
>``` python
return getHTBaseUrl() + "image/"+get_url_hash(getValue("url"))+"/"+getValue("importime") + "/processed"
```

#### _image_snapshot_uri_
From column: _images / image_snapshot_uri_
>``` python
return getHTBaseUrl() + "image/"+get_url_hash(getValue("url"))+"/"+getValue("importime") + "/raw"
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _age_clean_ | `memex:person_age` | `memex:Feature2`|
| _age_clean2_ | `memex:featureValue` | `memex:Feature2`|
| _age_feature_uri_ | `uri` | `memex:Feature2`|
| _body_uri_ | `uri` | `schema:WebPageElement1`|
| _bodytext_ | `schema:text` | `schema:WebPageElement1`|
| _cache_uri_ | `uri` | `schema:WebPage1`|
| _email_clean_ | `memex:emailaddress` | `memex:Feature4`|
| _email_clean2_ | `memex:featureValue` | `memex:Feature4`|
| _email_feature_uri_ | `uri` | `memex:Feature4`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _image_snapshot_uri_ | `memex:snapshotUri` | `schema:ImageObject1`|
| _image_uri_ | `uri` | `schema:ImageObject1`|
| _imageurl_ | `schema:url` | `schema:ImageObject1`|
| _import_time_ | `memex:dateCrawled` | `schema:WebPage1`|
| _phone_cc_ | `memex:countryDialingCode` | `memex:PhoneNumber1`|
| _phone_clean_ | `memex:phonenumber` | `memex:Feature3`|
| _phone_clean1_ | `memex:featureValue` | `memex:Feature3`|
| _phone_clean2_ | `rdfs:label` | `memex:PhoneNumber1`|
| _phone_feature_uri_ | `uri` | `memex:Feature3`|
| _phone_local_ | `memex:localPhoneNumber` | `memex:PhoneNumber1`|
| _phone_uri_ | `uri` | `memex:PhoneNumber1`|
| _s3imageurl_ | `memex:cacheUrl` | `schema:ImageObject1`|
| _snapshot_uri_ | `memex:snapshotUri` | `schema:WebPage1`|
| _title_ | `schema:text` | `schema:WebPageElement2`|
| _title_uri_ | `uri` | `schema:WebPageElement2`|
| _url_ | `schema:url` | `schema:WebPage1`|
| _values_ | `memex:website` | `memex:Feature1`|
| _website2_ | `memex:featureValue` | `memex:Feature1`|
| _website_feature_uri_ | `uri` | `memex:Feature1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:website`|
| `memex:Feature2` | `memex:featureName` | `xsd:person_age`|
| `memex:Feature3` | `memex:featureName` | `xsd:phonenumber`|
| `memex:Feature3` | `memex:featureObject` | `memex:PhoneNumber1`|
| `memex:Feature4` | `memex:featureName` | `xsd:emailaddress`|
| `memex:FeatureCollection1` | `memex:emailaddress_feature` | `memex:Feature4`|
| `memex:FeatureCollection1` | `memex:person_age_feature` | `memex:Feature2`|
| `memex:FeatureCollection1` | `memex:phonenumber_feature` | `memex:Feature3`|
| `memex:FeatureCollection1` | `memex:website_feature` | `memex:Feature1`|
| `schema:WebPage1` | `memex:hasBodyPart` | `schema:WebPageElement1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
| `schema:WebPage1` | `memex:hasImagePart` | `schema:ImageObject1`|
| `schema:WebPage1` | `memex:hasTitlePart` | `schema:WebPageElement2`|
