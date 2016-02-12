## ht-cdr2-ads-500.jl

### PyTransforms
#### _iso_posttime_
From column: _extractions / posttime / results / values_
>``` python
posttime = getValue("values")
if posttime.strip() != '':
    return DM.iso8601date(posttime,'%Y-%m-%d %H:%M:%S')
posttime = getValue("timestamp")
return DM.epoch_to_iso8601(posttime)
```

#### _offer_uri_
From column: _isi_id_
>``` python
return "offer/" + getValue("isi_id")
```

#### _clean_country_
From column: _extractions / country / results / values_
>``` python
return LM.clean_country(getValue("values"))
```

#### _clean_state_
From column: _extractions / state / results / values_
>``` python
return getValue("values").title()
```

#### _clean_city_
From column: _extractions / Glue_1 / Glue_1 / extractions_Glue_1_extractions_region_results_values_
>``` python
clean_city = getValue("extractions_Glue_1_extractions_region_results_values")
if clean_city.strip() != '':
    return clean_city.title()
clean_city = getValue("extractions_Glue_1_extractions_city_results_values")
if ',' in clean_city:
    city = clean_city.split(',')[0]
    return city
else:
    return clean_city
```

#### _postaladdress_uri_
From column: _extractions / Glue_2 / Glue_1 / extractions_Glue_2_extractions_state_results_clean_state_
>``` python
state = getValue("extractions_Glue_2_extractions_state_results_clean_state")
city = getValue("extractions_Glue_2_extractions_Glue_1_Glue_1_clean_city")
country = getValue("extractions_Glue_2_extractions_country_results_clean_country")
uri =  UM.uri_from_fields('/address/',city,state,country)
if uri == '':
    return ''
return getValue('offer_uri') + uri

```

#### _place_uri_
From column: _extractions / Glue_2 / Glue_1 / postaladdress_uri_
>``` python
place_uri=getValue('postaladdress_uri')
if place_uri.strip() == '':
    return ''
return  place_uri + '/place'
```

#### _clean_rate_
From column: _extractions / rate30 / results / value_
>``` python
return SM.clean_rate30(getValue("value"))
```

#### _price_rate30_
From column: _extractions / rate30 / results / clean_rate_
>``` python
return SM.rate_price(getValue("clean_rate"))
```

#### _duration_rate30_
From column: _extractions / rate30 / results / price_rate30_
>``` python
return SM.rate_duration(getValue("clean_rate"))
```

#### _unit_rate30_
From column: _extractions / rate30 / results / duration_rate30_
>``` python
return SM.rate_unit(getValue("clean_rate"))
```

#### _uri_rate30_
From column: _extractions / rate30 / results / unit_rate30_
>``` python
price = getValue("clean_rate")
if price.strip() == '':
    return ''
return 'pricespecification/' + price
```

#### _clean_rate60_
From column: _extractions / rate60 / results / value_
>``` python
return SM.clean_rate60(getValue("value"))
```

#### _price_rate60_
From column: _extractions / rate60 / results / clean_rate60_
>``` python
return SM.rate_price(getValue("clean_rate60"))
```

#### _duration_rate60_
From column: _extractions / rate60 / results / price_rate60_
>``` python
return SM.rate_duration(getValue("clean_rate60"))
```

#### _unit_rate60_
From column: _extractions / rate60 / results / duration_rate60_
>``` python
return SM.rate_unit(getValue("clean_rate60"))
```

#### _uri_rate60_
From column: _extractions / rate60 / results / unit_rate60_
>``` python
price = getValue("clean_rate60")
if price.strip() == '':
    return ''
return 'pricespecification/' + price
```

#### _clean_rate15_
From column: _extractions / rate15 / results / value_
>``` python
return SM.clean_rate15(getValue("value"))
```

#### _price_rate15_
From column: _extractions / rate15 / results / clean_rate15_
>``` python
return SM.rate_price(getValue("clean_rate15"))
```

#### _duration_rate15_
From column: _extractions / rate15 / results / price_rate15_
>``` python
return SM.rate_duration(getValue("clean_rate15"))
```

#### _unit_rate15_
From column: _extractions / rate15 / results / duration_rate15_
>``` python
return SM.rate_unit(getValue("clean_rate15"))
```

#### _uri_rate15_
From column: _extractions / rate15 / results / unit_rate15_
>``` python
price = getValue("clean_rate15")
if price == '':
    return ''
return 'pricespecification/' + price
```

#### _geo_uri_
From column: _extractions / Glue_3 / Glue_1 / extractions_Glue_3_extractions_latitude_results_values_
>``` python
longitude =  getValue("extractions_Glue_3_extractions_longitude_results_values")
latitude = getValue("extractions_Glue_3_extractions_latitude_results_values")
if longitude != '' and latitude != '':
    return 'geo/' + longitude + '-' + latitude
return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _clean_city_ | `schema:addressLocality` | `schema:PostalAddress1`|
| _clean_country_ | `schema:addressCountry` | `schema:PostalAddress1`|
| _clean_rate_ | `schema:name` | `schema:PriceSpecification3`|
| _clean_rate15_ | `schema:name` | `schema:PriceSpecification1`|
| _clean_rate60_ | `schema:name` | `schema:PriceSpecification2`|
| _clean_state_ | `schema:addressRegion` | `schema:PostalAddress1`|
| _duration_rate15_ | `schema:billingIncrement` | `schema:PriceSpecification1`|
| _duration_rate30_ | `schema:billingIncrement` | `schema:PriceSpecification3`|
| _duration_rate60_ | `schema:billingIncrement` | `schema:PriceSpecification2`|
| _extractions_Glue_3_extractions_latitude_results_values_ | `schema:latitude` | `schema:GeoCoordinates1`|
| _extractions_Glue_3_extractions_longitude_results_values_ | `schema:longitude` | `schema:GeoCoordinates1`|
| _geo_uri_ | `uri` | `schema:GeoCoordinates1`|
| _iso_posttime_ | `schema:validFrom` | `schema:Offer1`|
| _offer_uri_ | `uri` | `schema:Offer1`|
| _place_uri_ | `uri` | `schema:Place1`|
| _postaladdress_uri_ | `uri` | `schema:PostalAddress1`|
| _price_rate15_ | `schema:price` | `schema:PriceSpecification1`|
| _price_rate30_ | `schema:price` | `schema:PriceSpecification3`|
| _price_rate60_ | `schema:price` | `schema:PriceSpecification2`|
| _unit_rate15_ | `schema:unitCode` | `schema:PriceSpecification1`|
| _unit_rate30_ | `schema:unitCode` | `schema:PriceSpecification3`|
| _unit_rate60_ | `schema:unitCode` | `schema:PriceSpecification2`|
| _uri_rate15_ | `uri` | `schema:PriceSpecification1`|
| _uri_rate30_ | `uri` | `schema:PriceSpecification3`|
| _uri_rate60_ | `uri` | `schema:PriceSpecification2`|
| _values_ | `schema:title` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Offer1` | `schema:availableAtOrFrom` | `schema:Place1`|
| `schema:Offer1` | `schema:priceSpecification` | `schema:PriceSpecification1`|
| `schema:Offer1` | `schema:priceSpecification` | `schema:PriceSpecification2`|
| `schema:Offer1` | `schema:priceSpecification` | `schema:PriceSpecification3`|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
| `schema:Place1` | `schema:geo` | `schema:GeoCoordinates1`|
