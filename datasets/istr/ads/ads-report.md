## ads-sample.json

### PyTransforms
#### _crawl_uri_
From column: _url_
>``` python
return getCacheBaseUrl()+"page/"+get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/processed"
```

#### _featurecollection_uri_
From column: _crawl_uri_
>``` python
return getValue("crawl_uri")+"/featurecollection"
```

#### _city2_
From column: _city_
>``` python
return getValue("city")
```

#### _state2_
From column: _state_
>``` python
return getValue("state")
```

#### _country2_
From column: _country_
>``` python
return getValue("country")
```

#### _phone2_
From column: _phone_
>``` python
return getValue("phone")
```

#### _age2_
From column: _age_
>``` python
return getValue("age")
```

#### _website2_
From column: _website_
>``` python
return getValue("website")
```

#### _email2_
From column: _email_
>``` python
return getValue("email")
```

#### _gender2_
From column: _gender_
>``` python
return getValue("gender")
```

#### _snapshot_uri_
From column: _crawl_uri_
>``` python
return getCacheBaseUrl()+"page/"+get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/raw"
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _age_ | `memex:featureValue` | `memex:Feature5`|
| _age2_ | `memex:person_age` | `memex:Feature5`|
| _city_ | `memex:featureValue` | `memex:Feature1`|
| _city2_ | `memex:place_city` | `memex:Feature1`|
| _country_ | `memex:featureValue` | `memex:Feature3`|
| _country2_ | `memex:place_country` | `memex:Feature3`|
| _crawl_uri_ | `uri` | `schema:WebPage1`|
| _email_ | `memex:featureValue` | `memex:Feature7`|
| _email2_ | `memex:emailaddress` | `memex:Feature7`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _gender_ | `memex:featureValue` | `memex:Feature8`|
| _gender2_ | `memex:person_gender` | `memex:Feature8`|
| _phone_ | `memex:featureValue` | `memex:Feature4`|
| _phone2_ | `memex:phonenumber` | `memex:Feature4`|
| _posttime_ | `schema:dateCreated` | `schema:WebPage1`|
| _snapshot_uri_ | `memex:snapshotUri` | `schema:WebPage1`|
| _state_ | `memex:featureValue` | `memex:Feature2`|
| _state2_ | `memex:place_state` | `memex:Feature2`|
| _text_ | `schema:text` | `schema:WebPageElement2`|
| _title_ | `schema:text` | `schema:WebPageElement1`|
| _url_ | `schema:url` | `schema:WebPage1`|
| _website_ | `memex:featureValue` | `memex:Feature6`|
| _website2_ | `memex:website` | `memex:Feature6`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:place_city`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `xsd:http://memexproxy.com/data/software/extractor/ist/ist-attributes-database`|
| `memex:Feature2` | `memex:featureName` | `xsd:place_state`|
| `memex:Feature2` | `prov:wasGeneratedBy` | `xsd:http://memexproxy.com/data/software/extractor/ist/ist-attributes-database`|
| `memex:Feature3` | `memex:featureName` | `xsd:place_country`|
| `memex:Feature3` | `prov:wasGeneratedBy` | `xsd:http://memexproxy.com/data/software/extractor/ist/ist-attributes-database`|
| `memex:Feature4` | `memex:featureName` | `xsd:phonenumber`|
| `memex:Feature4` | `prov:wasGeneratedBy` | `xsd:http://memexproxy.com/data/software/extractor/ist/ist-attributes-database`|
| `memex:Feature5` | `memex:featureName` | `xsd:person_age`|
| `memex:Feature5` | `prov:wasGeneratedBy` | `xsd:http://memexproxy.com/data/software/extractor/ist/ist-attributes-database`|
| `memex:Feature6` | `memex:featureName` | `xsd:website`|
| `memex:Feature6` | `prov:wasGeneratedBy` | `xsd:http://memexproxy.com/data/software/extractor/ist/ist-attributes-database`|
| `memex:Feature7` | `memex:featureName` | `xsd:emailaddress`|
| `memex:Feature7` | `prov:wasGeneratedBy` | `xsd:http://memexproxy.com/data/software/extractor/ist/ist-attributes-database`|
| `memex:Feature8` | `memex:featureName` | `xsd:person_gender`|
| `memex:Feature8` | `prov:wasGeneratedBy` | `xsd:http://memexproxy.com/data/software/extractor/ist/ist-attributes-database`|
| `memex:FeatureCollection1` | `memex:hasFeatures` | `memex:Feature1`|
| `memex:FeatureCollection1` | `memex:hasFeatures` | `memex:Feature2`|
| `memex:FeatureCollection1` | `memex:hasFeatures` | `memex:Feature3`|
| `memex:FeatureCollection1` | `memex:hasFeatures` | `memex:Feature4`|
| `memex:FeatureCollection1` | `memex:hasFeatures` | `memex:Feature5`|
| `memex:FeatureCollection1` | `memex:hasFeatures` | `memex:Feature6`|
| `memex:FeatureCollection1` | `memex:hasFeatures` | `memex:Feature7`|
| `memex:FeatureCollection1` | `memex:hasFeatures` | `memex:Feature8`|
| `schema:WebPage1` | `memex:hasBodyPart` | `schema:WebPageElement2`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
| `schema:WebPage1` | `memex:hasTitlePart` | `schema:WebPageElement1`|
