## sources-sample.json

### PyTransforms
#### _organization_uri_
From column: _name_
>``` python
return organization_uri(getValue("id"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _id_ | `memex:databaseId` | `schema:Organization1`|
| _name_ | `schema:legalName` | `schema:Organization1`|
| _organization_uri_ | `uri` | `schema:Organization1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
