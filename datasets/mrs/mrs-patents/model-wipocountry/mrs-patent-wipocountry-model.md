## mrs-patent-data-sample.json

### PyTransforms
#### _country_
From column: _country_
>``` python
return standardize_wipocountry_name(getValue("Publication Number")[0:2])
```

#### _countryValue_
From column: _countryValue_
>``` python
return getValue("country")
```

#### _uri_
From column: _uri_
>``` python
publicationNumber = getValue("Publication Number")
publicationNumber = ''.join(publicationNumber.split())
return "page/" + publicationNumber + "/processed"
```

#### _countryUri_
From column: _countryUri_
>``` python
return getValue("uri") + "/country"
```

#### _featurecollectionUri_
From column: _featurecollectionUri_
>``` python
return getValue("uri") +"/featurecollection"
```

#### _featureUri_
From column: _featureUri_
>``` python
return getValue("featurecollectionUri") + "/country"
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _country_ | `memex:wipo_country_code` | `memex:Feature1`|
| _countryValue_ | `memex:featureValue` | `memex:Feature1`|
| _featureUri_ | `uri` | `memex:Feature1`|
| _featurecollectionUri_ | `uri` | `memex:FeatureCollection1`|
| _uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `memex:FeatureCollection1` | `memex:wipo_country_feature` | `memex:Feature1`|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://dig.isi.edu/mrs/data/api/google`|
| `schema:WebPage1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
