## abacuselect-sample.json

### PyTransforms
#### _uri_
From column: _manufacturer_
>``` python
return as_getTextHash(getValue("manufacturer"),getValue("model"))
```

#### _model_clean_
From column: _model_
>``` python
return el_clean_model(getValue("model"))
```

#### _manufacturer_clean_
From column: _manufacturer_
>``` python
return el_clean_manufacturer(getValue("manufacturer"))
```

#### _manufacturer_uri_
From column: _manufacturer_
>``` python
return el_manufacturer_uri(getValue("manufacturer"))
```

#### _product_uri_
From column: _model_
>``` python
return el_product_uri(getValue("model"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _manufacturer_clean_ | `schema:name` | `schema:Organization1`|
| _manufacturer_uri_ | `uri` | `schema:Organization1`|
| _model_clean_ | `schema:mpn` | `schema:Product1`|
| _product_uri_ | `uri` | `schema:Product1`|
| _quantity_ | `schema:inventoryLevel` | `schema:Offer1`|
| _seller_ | `uri` | `schema:Organization2`|
| _uri_ | `uri` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Offer1` | `schema:itemOffered` | `schema:Product1`|
| `schema:Offer1` | `schema:seller` | `schema:Organization2`|
| `schema:Product1` | `schema:manufacturer` | `schema:Organization1`|
