## stanford-features-sample.json

### PyTransforms
#### _crawl_url_
From column: _url_
>``` python
return "page/"+get_url_hash(getValue("url"))+"/"+getValue("ad_timestamp") + "/processed"
```

#### _namelist_
From column: _names_
>``` python
return splitNameField(getValue("names"))
```

#### _phonelist_
From column: _phones_
>``` python
return splitPhoneField(getValue("phones"))
```

#### _locationlist_
From column: _locations_
>``` python
return splitLocationField(getValue("locations"))
```

#### _featurecollection_uri_
From column: _crawl_url_
>``` python
return getValue("crawl_url")+"/featurecollection"
```

#### _names_values2_
From column: _names_values / Values_
>``` python
return getValue("Values")
```

#### _phone_values2_
From column: _phones_values / Values_
>``` python
return getValue("Values")
```

#### _locations_values2_
From column: _locations_values / Values_
>``` python
return getValue("Values")
```

#### _Values_
From column: _phones_values / Values_
>``` python
return clean_phone(getValue("Values"))
```

#### _phone_values3_
From column: _phones_values / phone_values2_
>``` python
return phone_uri(getValue("Values"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `memex:featureValue` | `memex:Feature1`|
| _Values_ | `memex:featureValue` | `memex:Feature2`|
| _Values_ | `memex:featureValue` | `memex:Feature3`|
| _crawl_url_ | `uri` | `schema:WebPage1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _locations_values2_ | `memex:place_name` | `memex:Feature3`|
| _names_values2_ | `memex:person_name` | `memex:Feature1`|
| _phone_values2_ | `memex:phonenumber` | `memex:Feature2`|
| _phone_values3_ | `uri` | `memex:PhoneNumber1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:person_name`|
| `memex:Feature1` | `prov:generatedAtTime` | `xsd:2014-10-12`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `xsd:http://memexproxy.com/data/software/extractor/stanford/0.1`|
| `memex:Feature2` | `memex:featureName` | `xsd:phonenumber`|
| `memex:Feature2` | `memex:featureObject` | `memex:PhoneNumber1`|
| `memex:Feature2` | `prov:generatedAtTime` | `xsd:2014-10-12`|
| `memex:Feature2` | `prov:wasGeneratedBy` | `xsd:http://memexproxy.com/data/software/extractor/stanford/0.1`|
| `memex:Feature3` | `memex:featureName` | `xsd:place_name`|
| `memex:Feature3` | `prov:generatedAtTime` | `xsd:2014-10-12`|
| `memex:Feature3` | `prov:wasGeneratedBy` | `xsd:http://memexproxy.com/data/software/extractor/stanford/0.1`|
| `memex:FeatureCollection1` | `memex:hasFeatures` | `memex:Feature1`|
| `memex:FeatureCollection1` | `memex:hasFeatures` | `memex:Feature2`|
| `memex:FeatureCollection1` | `memex:hasFeatures` | `memex:Feature3`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
