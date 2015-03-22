## sortera-sample.json

### PyTransforms
#### _cache_uri_
From column: _urls / url_
>``` python
return getCacheBaseUrl()+"page/"+get_url_hash(getValue("url"))+"/processed"
```

#### _snapshot_uri_
From column: _urls / cache_uri_
>``` python
return getCacheBaseUrl()+"page/"+get_url_hash(getValue("url"))+"/raw"
```

#### _featurecollection_uri_
From column: _urls / snapshot_uri_
>``` python
return getValue("cache_uri") + "/featurecollection"
```

#### _clean_location_
From column: _urls / auto_features / LOCATION / values_
>``` python
return clean_location(getValue("values"))
```

#### _clean_location2_
From column: _urls / auto_features / LOCATION / clean_location_
>``` python
return getValue("clean_location")
```

#### _loc_uri_
From column: _urls / auto_features / LOCATION / clean_location2_
>``` python
uri = place_location_uri(getValue("clean_location"))
if uri:
  return getValue("featurecollection_uri") + "/" + uri
return ''
```

#### _clean_org_
From column: _urls / auto_features / ORGANIZATION / values_
>``` python
return clean_organization(getValue("values"))
```

#### _clean_org2_
From column: _urls / auto_features / ORGANIZATION / clean_org_
>``` python
return getValue("clean_org")
```

#### _org_uri_
From column: _urls / auto_features / ORGANIZATION / clean_org2_
>``` python
uri = organization_name_uri(getValue("clean_org"))
if uri:
  return getValue("featurecollection_uri") + "/" + uri
return ''
```

#### _name_clean_
From column: _urls / auto_features / PERSON / values_
>``` python
return clean_name(getValue("values"))
```

#### _name_clean2_
From column: _urls / auto_features / PERSON / name_clean_
>``` python
return getValue("name_clean")
```

#### _name_uri_
From column: _urls / auto_features / PERSON / name_clean2_
>``` python
uri = person_name_uri(getValue("name_clean"))
if uri:
  return getValue("featurecollection_uri") + "/" + uri
return ''
```

#### _email_clean_
From column: _urls / auto_features / email / values_
>``` python
return clean_email(getValue("values"))
```

#### _email_clean2_
From column: _urls / auto_features / email / email_clean_
>``` python
return getValue("email_clean")
```

#### _email_uri_
From column: _urls / auto_features / email / email_clean2_
>``` python
uri = emailaddress_uri(getValue("email_clean"))
if uri:
  return getValue("featurecollection_uri") + "/" + uri
return ''
```

#### _website_clean_
From column: _urls / auto_features / website / values_
>``` python
return clean_website(getValue("values"))
```

#### _website_clean2_
From column: _urls / auto_features / website / website_clean_
>``` python
return getValue("website_clean")
```

#### _website_uri_
From column: _urls / auto_features / website / website_clean2_
>``` python
uri = website_uri(getValue("website_clean"))
if uri:
  return getValue("featurecollection_uri") + "/" + uri
return ''
```

#### _phone_clean_
From column: _urls / auto_features / phone / values_
>``` python
return clean_phone(getValue("values"))
```

#### _phone_clean2_
From column: _urls / auto_features / phone / phone_clean_
>``` python
return getValue("phone_clean")
```

#### _phone_uri_
From column: _urls / auto_features / phone / phone_clean2_
>``` python
return phone_uri(getValue("phone_clean"))
```

#### _phone_feature_uri_
From column: _urls / auto_features / phone / phone_uri_
>``` python
uri = getValue("phone_uri")
if uri:
  return getValue("featurecollection_uri") + "/" + uri
return ''
```

#### _phone_clean3_
From column: _urls / auto_features / phone / phone_feature_uri_
>``` python
return getValue("phone_clean")
```

#### _exchange_uri_
From column: _urls / auto_features / phone / phone_clean3_
>``` python
if getValue("phone_clean"):
  return phoneExchangeUri(getValue("phone_clean"))
return ''
```

#### _misc2_
From column: _urls / auto_features / MISC / values_
>``` python
return getValue("values")
```

#### _misc_uri_
From column: _urls / auto_features / MISC / misc2_
>``` python
if getValue("values"):
  return getValue("featurecollection_uri") + "/misc"
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _cache_uri_ | `uri` | `schema:WebPage1`|
| _clean_location_ | `memex:featureValue` | `memex:Feature1`|
| _clean_location2_ | `memex:place_location` | `memex:Feature1`|
| _clean_org_ | `memex:featureValue` | `memex:Feature2`|
| _clean_org2_ | `memex:organization` | `memex:Feature2`|
| _email_clean_ | `memex:featureValue` | `memex:Feature4`|
| _email_clean2_ | `memex:emailaddress` | `memex:Feature4`|
| _email_uri_ | `uri` | `memex:Feature4`|
| _exchange_uri_ | `uri` | `schema:Place1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _loc_uri_ | `uri` | `memex:Feature1`|
| _misc2_ | `memex:misc` | `memex:Feature7`|
| _misc_uri_ | `uri` | `memex:Feature7`|
| _name_clean_ | `memex:featureValue` | `memex:Feature3`|
| _name_clean2_ | `memex:person_name` | `memex:Feature3`|
| _name_uri_ | `uri` | `memex:Feature3`|
| _org_uri_ | `uri` | `memex:Feature2`|
| _phone_clean_ | `memex:featureValue` | `memex:Feature6`|
| _phone_clean2_ | `memex:phonenumber` | `memex:Feature6`|
| _phone_clean3_ | `rdfs:label` | `memex:PhoneNumber1`|
| _phone_feature_uri_ | `uri` | `memex:Feature6`|
| _phone_uri_ | `uri` | `memex:PhoneNumber1`|
| _snapshot_uri_ | `memex:snapshotUri` | `schema:WebPage1`|
| _url_ | `schema:url` | `schema:WebPage1`|
| _values_ | `memex:featureValue` | `memex:Feature7`|
| _website_clean_ | `memex:featureValue` | `memex:Feature5`|
| _website_clean2_ | `memex:website` | `memex:Feature5`|
| _website_uri_ | `uri` | `memex:Feature5`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:place_location`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:Feature2` | `memex:featureName` | `xsd:organization`|
| `memex:Feature2` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature2` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:Feature3` | `memex:featureName` | `xsd:person_name`|
| `memex:Feature3` | `prov:wasAttributedTo` | `prov:Activity1`|
| `memex:Feature3` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:Feature4` | `memex:featureName` | `xsd:emailaddress`|
| `memex:Feature4` | `prov:wasAttributedTo` | `prov:Activity1`|
| `memex:Feature4` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:Feature5` | `memex:featureName` | `xsd:website`|
| `memex:Feature5` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:Feature5` | `prov:wasAttributedTo` | `prov:Activity1`|
| `memex:Feature6` | `memex:featureName` | `xsd:phonenumber`|
| `memex:Feature6` | `memex:featureObject` | `memex:PhoneNumber1`|
| `memex:Feature6` | `prov:wasAttributedTo` | `prov:Activity1`|
| `memex:Feature6` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:Feature7` | `memex:featureName` | `xsd:misc`|
| `memex:Feature7` | `prov:wasAttributedTo` | `prov:Activity1`|
| `memex:Feature7` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:emailaddress_feature` | `memex:Feature4`|
| `memex:FeatureCollection1` | `memex:misc_feature` | `memex:Feature7`|
| `memex:FeatureCollection1` | `memex:organization_feature` | `memex:Feature2`|
| `memex:FeatureCollection1` | `memex:person_name_feature` | `memex:Feature3`|
| `memex:FeatureCollection1` | `memex:phonenumber_feature` | `memex:Feature6`|
| `memex:FeatureCollection1` | `memex:place_location_feature` | `memex:Feature1`|
| `memex:FeatureCollection1` | `memex:website_feature` | `memex:Feature5`|
| `memex:PhoneNumber1` | `schema:location` | `schema:Place1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memex.zapto.org/data/software/extractor/sotera/version/0.1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
