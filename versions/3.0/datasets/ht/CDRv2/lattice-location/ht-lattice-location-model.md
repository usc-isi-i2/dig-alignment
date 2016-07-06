## example2.json

### PyTransforms
#### _city_name_
From column: _extractions / lattice-location / results / context / location / name_
>``` python
n =  getValue("name")
if ',' in n:
    return n.split(',')[0]
return n
```

#### _state_name_
From column: _extractions / lattice-location / results / context / location / city_name_
>``` python
n =  getValue("name")
if ',' in n:
    return n.split(',')[1]
return n
```

#### _a_city_name_
From column: _extractions / lattice-location / results / context / location / name_
>``` python
n = getValueFromNestedColumnByIndex("extractions", "lattice-location/results/context/city/name",0)
if ',' in n:
    return n.split(',')[0]
c_n = getValue('city_name')
if n == '':
    return c_n
return n
```

#### _a_state_name_
From column: _extractions / lattice-location / results / context / location / name_
>``` python
n = getValueFromNestedColumnByIndex("extractions", "lattice-location/results/context/state/name",0)
if ',' in n:
    return n.split(',')[0]
s_n = getValue('state_name')
if n == '':
    return s_n
return n
```

#### _a_country_name_
From column: _extractions / lattice-location / results / context / location / name_
>``` python
n = getValueFromNestedColumnByIndex("extractions", "lattice-location/results/context/country/name",0)
if ',' in n:
    return n.split(',')[0]
c_n = getValue('a_state_name')
if n == '':
    return c_n
return n
```

#### _longitude_
From column: _extractions / lattice-location / results / context / location / centroid_lon_
>``` python
l = getValue("centroid_lon")
if l != '':
    return l
return '181.0'
```

#### _latitude_
From column: _extractions / lattice-location / results / context / location / centroid_lat_
>``` python
l = getValue("centroid_lat")
if l != '':
    return l
return '91.0'
```

#### _key_
From column: _extractions / lattice-location / results / context / location / name_
>``` python
city =  getValue("a_city_name")
state =  getValue("a_state_name")
country =  getValue("a_country_name")
lon = getValue('longitude')
lat = getValue('latitude')
return city + ':' + state + ':' + country + ':' + lon + ':' + lat
```

#### _offer_uri_
From column: __id_
>``` python
return "offer/" + getValue("_id")
```

#### _postal_add_uri_
From column: _offer_uri_
>``` python
return "offer/" + getValue("_id") + "/address"
```

#### _place_uri_
From column: _postal_add_uri_
>``` python
return "offer/" + getValue("_id") + "/place"
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _a_city_name_ | `schema:addressLocality` | `schema:PostalAddress1`|
| _a_country_name_ | `schema:addressCountry` | `schema:PostalAddress1`|
| _a_state_name_ | `schema:addressRegion` | `schema:PostalAddress1`|
| _key_ | `memex:key` | `schema:PostalAddress1`|
| _latitude_ | `schema:latitude` | `schema:GeoCoordinates1`|
| _longitude_ | `schema:longitude` | `schema:GeoCoordinates1`|
| _offer_uri_ | `uri` | `schema:Offer1`|
| _place_uri_ | `uri` | `schema:Place1`|
| _postal_add_uri_ | `uri` | `schema:PostalAddress1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Offer1` | `schema:availableAtOrFrom` | `schema:Place1`|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
| `schema:PostalAddress1` | `schema:geo` | `schema:GeoCoordinates1`|
