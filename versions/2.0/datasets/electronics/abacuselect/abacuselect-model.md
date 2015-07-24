## abacuselect-sample.json

### PyTransforms
#### _uri_
From column: _manufacturer_
>``` python
return as_getTextHash(getValue("manufacturer"),getValue("model"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _manufacturer_ | `schema:name` | `schema:Organization1`|
| _model_ | `schema:mpn` | `schema:Offer1`|
| _quantity_ | `schema:inventoryLevel` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Offer1` | `schema:seller` | `schema:Organization1`|
