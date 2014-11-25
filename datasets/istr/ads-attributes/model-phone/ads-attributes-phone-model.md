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
return getValue("featurecollection_uri") + "/" + feature_uri(getValue("feature_name"), getValue("feature_value"))
```

#### _phone_value_
From column: _feature_uri_
>``` python
return getValue("feature_value")
```

#### _phone_uri_
From column: _phone_value_
>``` python
return phone_uri(getValue("phone_value"))
```

#### _exchange_uri_
From column: _phone_uri_
>``` python
ph = getValue("phone_value")
if ph:
  return phoneExchangeUri(ph)
return ''
```

#### _featurecollection_uri_
From column: _url_
>``` python
return "http://memex.zapto.org/data/page/" +get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/raw/featurecollection"
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _exchange_uri_ | `uri` | `schema:Place1`|
| _feature_name_ | `memex:featureName` | `memex:Feature1`|
| _feature_uri_ | `uri` | `memex:Feature1`|
| _feature_value_ | `memex:featureValue` | `memex:Feature1`|
| _phone_uri_ | `uri` | `memex:PhoneNumber1`|
| _phone_value_ | `rdfs:label` | `memex:PhoneNumber1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureObject` | `memex:PhoneNumber1`|
| `memex:PhoneNumber1` | `schema:location` | `schema:Place1`|
