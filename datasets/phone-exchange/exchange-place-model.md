## exchange-sample.json

### PyTransforms
#### _exchangeUri_
From column: _exchange_id_
>``` python
return "exchange/"+getValue("exchange_id")
```

#### _city_name_
From column: _exchange_rc_
>``` python
return toTitleCaseIfUpper(getValue("exchange_rc"))
```

#### _postalAddressUri_
From column: _exchange_rc_
>``` python
return getValue("exchangeUri")+"/postaladdress"
```

#### _geoUri_
From column: _exchange_rc_lon_
>``` python
return getValue("exchangeUri")+"/geo"
```

#### _stateUri_
From column: _exchange_region_
>``` python
return "place/state/"+getValue("exchange_region").lower().strip()
```

#### _place_label_
From column: _city_name_
>``` python
return getValue("city_name")+", "+getValue("areacode_adm1_name")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _areacode_adm1_name_ | `schema:addressRegion` | `schema:PostalAddress1`|
| _city_name_ | `schema:addressLocality` | `schema:PostalAddress1`|
| _exchangeUri_ | `uri` | `schema:Place1`|
| _exchange_rc_lat_ | `schema:latitude` | `schema:GeoCoordinates1`|
| _exchange_rc_lon_ | `schema:longitude` | `schema:GeoCoordinates1`|
| _geoUri_ | `uri` | `schema:GeoCoordinates1`|
| _place_label_ | `rdfs:label` | `schema:Place1`|
| _postalAddressUri_ | `uri` | `schema:PostalAddress1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
| `schema:Place1` | `schema:geo` | `schema:GeoCoordinates1`|
