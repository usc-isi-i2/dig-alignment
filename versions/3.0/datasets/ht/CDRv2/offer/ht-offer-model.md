## cdr_with_name.jl

### PyTransforms
#### _offer_uri_
From column: _isi_id_
>``` python
return "offer/" + getValue("isi_id")
```

#### _iso_posttime2_
From column: _crawl_data / context / timestamp_
>``` python
return DM.epoch_to_iso8601(getValue("timestamp"))
```

#### _clean_city_
From column: _extractions / city / results / values_
>``` python
return HM.remove_junk(LM.clean_location(getValue("values")))
```

#### _clean_state_
From column: _extractions / state / results / values_
>``` python
return HM.remove_junk(LM.clean_location(getValue("values")))
```

#### _postal_add_uri_
From column: _offer_uri_
>``` python
return "offer/" + getValue("isi_id") + "/address"
```

#### _place_uri_
From column: _offer_uri_
>``` python
return "offer/" + getValue("isi_id") + "/place"
```

#### _clean_price_name_
From column: _extractions / rate / results / values_
>``` python
x = getValue("values").strip()
if x != "":
  return SM.clean_price_name(getValue("values"))
return ""
```

#### _clean_price_
From column: _extractions / rate / results / values_
>``` python
return SM.get_price(getValue("values"))
```

#### _clean_duration_
From column: _extractions / rate / results / values_
>``` python
return SM.calculate_minutes(getValue("values"))
```

#### _clean_unit_
From column: _extractions / rate / results / values_
>``` python
return "MIN"
```

#### _rate_uri_
From column: _extractions / rate / results / clean_price_name_
>``` python
x = getValue('clean_price_name')
if x != '':
  return "price/" + x
return ''
```

#### _iso_crawltime_
From column: _extractions / posttime / results / values_
>``` python
return getValueFromNestedColumnByIndex("crawl_data", "context/iso_posttime2",0)
```

#### _iso_posttime_
From column: _extractions / posttime / results / values_
>``` python
posttime = getValue("values")
if posttime.strip() != '':
    return DM.iso8601date(posttime)
return ''
```

#### _iso_finaltime_
From column: _extractions / posttime / results / iso_crawltime_
>``` python
posttime = getValue("iso_posttime").strip()
if posttime != '':
    return posttime
return getValue("iso_crawltime")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _clean_city_ | `schema:addressLocality` | `schema:PostalAddress1`|
| _clean_duration_ | `schema:billingIncrement` | `schema:PriceSpecification1`|
| _clean_price_ | `schema:price` | `schema:PriceSpecification1`|
| _clean_price_name_ | `schema:name` | `schema:PriceSpecification1`|
| _clean_state_ | `schema:addressRegion` | `schema:PostalAddress1`|
| _clean_unit_ | `schema:unitCode` | `schema:PriceSpecification1`|
| _iso_finaltime_ | `schema:validFrom` | `schema:Offer1`|
| _offer_uri_ | `uri` | `schema:Offer1`|
| _place_uri_ | `uri` | `schema:Place1`|
| _postal_add_uri_ | `uri` | `schema:PostalAddress1`|
| _rate_uri_ | `uri` | `schema:PriceSpecification1`|
| _values_ | `schema:title` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Offer1` | `schema:availableAtOrFrom` | `schema:Place1`|
| `schema:Offer1` | `schema:priceSpecification` | `schema:PriceSpecification1`|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
