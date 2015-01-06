## ads-addresses-sample.json

### PyTransforms
#### _crawl_uri_
From column: _url_
>``` python
return "page/"+get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/processed"
```

#### _featurecollection_uri_
From column: _text_
>``` python
return getValue("crawl_uri")+"/featurecollection"
```

#### _modetime_iso8601_
From column: _modtime_
>``` python
if getValue("address_uri"):
  return iso8601date(getValue("modtime"))
return ''
```

#### _city_clean_
From column: _city_
>``` python
return clean_city(getValue("city"))
```

#### _country_clean_
From column: _country_
>``` python
return clean_country(getValue("country"))
```

#### _country_code_
From column: _country_clean_
>``` python
return country_code(getValue("country"))
```

#### _state_clean_
From column: _country_clean_
>``` python
country = getValue("country_code")
state = getValue("state")
if len(state) == 0 and (country == "US" or country == "CA"):
   state = getValue("region")
return clean_state(state, country)
```

#### _country_uri_
From column: _country_clean_
>``` python
return country_uri(getValue("country"))
```

#### _address_
From column: _state_clean_
>``` python
return feature_address(getValue("city_clean"), getValue("state_clean"), getValue("country_clean"))
```

#### _address2_
From column: _address_
>``` python
return getValue("address")
```

#### _address_uri_
From column: _address2_
>``` python
return address_uri(getValue("city_clean"), getValue("state_clean"), getValue("country_clean"))
```

#### _feature_uri_
From column: _address_uri_
>``` python
uri = getValue("address_uri")
if(len("uri") > 0):
    return getValue("featurecollection_uri")+"/" + uri
return ''
```

#### _database_id_
From column: _modetime_iso8601_
>``` python
if getValue("address_uri"):
  return getValue("id")
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _address_ | `memex:featureValue` | `memex:Feature1`|
| _address2_ | `memex:place_postalAddress` | `memex:Feature1`|
| _address_uri_ | `uri` | `schema:PostalAddress1`|
| _city_clean_ | `schema:addressLocality` | `schema:PostalAddress1`|
| _country_clean_ | `rdfs:label` | `schema:Country1`|
| _country_code_ | `memex:isoCode` | `schema:Country1`|
| _country_uri_ | `uri` | `schema:Country1`|
| _crawl_uri_ | `uri` | `schema:WebPage1`|
| _database_id_ | `memex:databaseId` | `prov:Activity1`|
| _feature_uri_ | `uri` | `memex:Feature1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _modetime_iso8601_ | `prov:endedAtTime` | `prov:Activity1`|
| _state_clean_ | `schema:addressRegion` | `schema:PostalAddress1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:place_postalAddress`|
| `memex:Feature1` | `memex:featureObject` | `schema:PostalAddress1`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:place_postalAddress_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://memex.zapto.org/data/software/extractor/ist/version/unknown`|
| `schema:PostalAddress1` | `schema:addressCountry` | `schema:Country1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
