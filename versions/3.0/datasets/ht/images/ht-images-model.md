## ht-cdr2-images.jl

### PyTransforms
#### _image_uri_
From column: __id_
>``` python
return "image/" + getValue("_id")
```

#### _adultservice_uri_
From column: __source / _parent_
>``` python
return "adultservice/" + getValue("_parent")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _adultservice_uri_ | `uri` | `memex:AdultService1`|
| _image_uri_ | `uri` | `schema:ImageObject1`|
| _obj_original_url_ | `schema:targetUrl` | `schema:ImageObject1`|
| _obj_stored_url_ | `schema:url` | `schema:ImageObject1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:AdultService1` | `schema:image` | `schema:ImageObject1`|
