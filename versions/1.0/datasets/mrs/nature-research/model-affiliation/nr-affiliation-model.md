## nr-data-sample.json

### PyTransforms
#### _doi_id_
From column: _doi_
>``` python
doi = getValue("doi")
doi = doi.replace("http://dx.doi.org/", "")
return doi
```

#### _uri_
From column: _doi_id_
>``` python
doi = getValue("doi_id")
if doi:
  return "page/" + get_url_hash(doi) + "/processed"
return ''
```

#### _featurecollection_uri_
From column: _uri_
>``` python
return getValue("uri") + "/featurecollection"
```

#### _country_clean_
From column: _affiliations / country_
>``` python
return clean_country(getValue("country"))
```

#### _country_clean2_
From column: _affiliations / country_clean_
>``` python
return getValue("country_clean")
```

#### _country_clean3_
From column: _affiliations / country_clean2_
>``` python
return getValue("country_clean")
```

#### _country_code_
From column: _affiliations / country_clean3_
>``` python
return country_code(getValue("country_clean"))
```

#### _country_uri_
From column: _affiliations / country_code_
>``` python
return country_uri(getValue("country_clean"))
```

#### _feature_uri_
From column: _affiliations / country_clean2_
>``` python
uri = getValue("country_uri")
if uri:
  return getValue("featurecollection_uri") + "/" + uri
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _country_clean_ | `memex:affiliation_country` | `memex:Feature1`|
| _country_clean2_ | `memex:featureValue` | `memex:Feature1`|
| _country_clean3_ | `rdfs:label` | `schema:Country1`|
| _country_code_ | `memex:isoCode` | `schema:Country1`|
| _country_uri_ | `uri` | `schema:Country1`|
| _doi_ | `memex:databaseId` | `prov:Activity1`|
| _feature_uri_ | `uri` | `memex:Feature1`|
| _featurecollection_uri_ | `uri` | `memex:FeatureCollection1`|
| _uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:affiliation_country`|
| `memex:Feature1` | `memex:featureObject` | `schema:Country1`|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:Feature1` | `prov:wasDerivedFrom` | `schema:WebPage1`|
| `memex:FeatureCollection1` | `memex:affiliation_country_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://dig.isi.edu/mrs/data/software/nr/version/0.1`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
