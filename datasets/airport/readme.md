## Airport Data
This dataset contains information about airport codes that we use to map backpage market codes to city names and latitude/longitude.

Downloaded `x-airports.csv` from from http://openflights.org/data.html

### PyTransforms
#### _placeUri_
From column: _DST Code_
>``` python
return "iata/"+getValue("IATA/FAA").lower()
```

#### _postalAddressUri_
From column: _placeUri_
>``` python
return "iata/"+getValue("IATA/FAA").lower()+"/postaladdress"
```

#### _countryUri_
From column: _Country_
>``` python
return "country/"+countryUri(getValue("Country"))
```

#### _geoURI_
From column: _Longitude_
>``` python
return getValue("placeUri").lower()+"/geo"
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _City_ | `schema:addressLocality` | `schema:PostalAddress1`|
| _Country_ | `rdfs:label` | `schema:Country1`|
| _Latitude_ | `schema:latitude` | `schema:GeoCoordinates1`|
| _Longitude_ | `schema:longitude` | `schema:GeoCoordinates1`|
| _countryUri_ | `uri` | `schema:Country1`|
| _geoURI_ | `uri` | `schema:GeoCoordinates1`|
| _placeUri_ | `uri` | `schema:Place1`|
| _postalAddressUri_ | `uri` | `schema:PostalAddress1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
| `schema:Place1` | `schema:geo` | `schema:GeoCoordinates1`|
| `schema:PostalAddress1` | `schema:addressCountry` | `schema:Country1`|