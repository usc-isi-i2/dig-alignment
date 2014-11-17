## add-attributes-sample-100.json

### PyTransforms
#### _feature_name_
From column: _attribute_
>``` python
return feature_name(getValue("attribute"))
```

#### _feature_value_
From column: _value_
>``` python
return feature_value(getValue("attribute"), getValue("value"))
```

#### _feature_uri_
From column: _feature_value_
>``` python
return feature_uri(getValue("feature_name"), getValue("feature_value"))
```

#### _feature_value2_
From column: _feature_uri_
>``` python
return getValue("feature_value")
```

#### _rate_price_
From column: _feature_value2_
>``` python
return rate_price(getValue("feature_value"))
```

#### _rate_duration_
From column: _rate_price_
>``` python
return rate_duration(getValue("feature_value"))
```

#### _rate_unit_
From column: _rate_duration_
>``` python
return rate_unit(getValue("feature_value"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _feature_name_ | `memex:featureName` | `memex:Feature1`|
| _feature_uri_ | `uri` | `memex:Feature1`|
| _feature_value_ | `memex:featureValue` | `memex:Feature1`|
| _feature_value2_ | `rdfs:label` | `memex:ServiceRate1`|
| _rate_duration_ | `schema:billingIncrement` | `memex:ServiceRate1`|
| _rate_price_ | `schema:price` | `memex:ServiceRate1`|
| _rate_unit_ | `schema:unitCode` | `memex:ServiceRate1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureObject` | `memex:ServiceRate1`|
| `memex:ServiceRate1` | `schema:priceCurrency` | `xsd:USD`|
