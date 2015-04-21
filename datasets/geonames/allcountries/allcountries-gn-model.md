## connecticut_test_order_100.csv

### PyTransforms
#### _place_uri_
From column: _geonameid_
>``` python
return gn_place_uri(getValue("geonameid"),getValue("fcode"),getValue("country"),getValue("admin1"),getValue("admin2"))
```

#### _place_identifier_uri_
From column: _geonameid_
>``` python
return gn_place_identifier_uri(getValue("geonameid"))
```

#### _place_class_
From column: _fcode_
>``` python
return fcode_to_class(getValue("fclass"),getValue("fcode"))
```

#### _country_uri_
From column: _country_
>``` python
return gn_country_uri(getValue("country"))
```

#### _State1stDiv_uri_
From column: _admin1_
>``` python
return gn_State1stDiv_uri(getValue("country"),getValue("admin1"))
```

#### _CountyProvince2ndDiv_uri_
From column: _admin2_
>``` python
return gn_CountyProvince2ndDiv_uri(getValue("country"),getValue("admin1"),getValue("admin2"))
```

#### _place_spacetimevolume_uri_
From column: _geonameid_
>``` python
return gn_place_spacetimevolume_uri(getValue("place_uri"))
```

#### _PointGeometry_uri_
From column: _place_uri_
>``` python
return gn_pointgeometry_uri(getValue("place_uri"))
```

#### _GeoJson_
From column: _latitude_
>``` python
return gn_geojson(getValue("latitude"),getValue("longitude"))
```

#### _alternate_names_uri_
From column: _alternatenames_split / Values_
>``` python
return gn_name_uri(getValue("geonameid"),getValue("Values"))
```

#### _name_uri_
From column: _name_
>``` python
return gn_name_uri(getValue("geonameid"),getValue("name"))
```

#### _nametype_
From column: _name_uri_
>``` python
return gn_nametype("DefaultName")
```

#### _AlternatenamesType_
From column: _alternatenames_split_
>``` python
return gn_nametype("AlternateName")
```

#### _CountryCodeConcept_uri_
From column: _country_uri_
>``` python
return gn_countrycodeconcept_uri(getValue("country"))
```

#### _lat_lon_
From column: _longitude_
>``` python
return getValue("latitude")+"|"+getValue("longitude")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AlternatenamesType_ | `uri` | `skos:Concept2`|
| _CountryCodeConcept_uri_ | `uri` | `skos:Concept3`|
| _CountyProvince2ndDiv_uri_ | `uri` | `memex:CountyProvince2ndDiv1`|
| _GeoJson_ | `memex:asGeoJson` | `memex:PointGeometry1`|
| _State1stDiv_uri_ | `uri` | `memex:State1stDiv1`|
| _Values_ | `memex:claims` | `memex:PointGeometry1`|
| _Values_ | `rdfs:label` | `memex:Name2`|
| _country_uri_ | `uri` | `memex:Country1`|
| _geonameid_ | `rdfs:label` | `memex:Identifier1`|
| _name_ | `rdfs:label` | `memex:Name1`|
| _place_class_ | `km-dev:columnSubClassOfLink` | `memex:Place1`|
| _place_identifier_uri_ | `uri` | `memex:Identifier1`|
| _place_spacetimevolume_uri_ | `uri` | `memex:SpaceTimeVolume1`|
| _place_uri_ | `uri` | `memex:Place1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Country1` | `memex:hasType` | `skos:Concept3`|
| `memex:Name1` | `memex:hasType` | `xsd:http://dig.isi.edu/gazetteer/data/SKOS/NameTypes/DefaultName`|
| `memex:Name2` | `memex:hasType` | `skos:Concept2`|
| `memex:Place1` | `memex:fallsWithinCountry` | `memex:Country1`|
| `memex:Place1` | `memex:fallsWithinCountyProvince2ndDiv` | `memex:CountyProvince2ndDiv1`|
| `memex:Place1` | `memex:fallsWithinState1stDiv` | `memex:State1stDiv1`|
| `memex:Place1` | `memex:hasSpaceTimeVolume` | `memex:SpaceTimeVolume1`|
| `memex:Place1` | `memex:hasIdentifier` | `memex:Identifier1`|
| `memex:Place1` | `memex:hasName` | `memex:Name1`|
| `memex:Place1` | `memex:hasName` | `memex:Name2`|
| `memex:SpaceTimeVolume1` | `memex:hasGeometry` | `memex:PointGeometry1`|
