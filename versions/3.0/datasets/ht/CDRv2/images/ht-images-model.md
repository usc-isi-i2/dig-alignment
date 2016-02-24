## images-cdr2-5000.jl

### PyTransforms
#### _image_uri_
From column: _doc_id_
>``` python
return 'image/' + getValue("doc_id")
```

#### _webpage_uri_
From column: _obj_parent_
>``` python
return 'webpage/' + getValue("obj_parent")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _image_uri_ | `uri` | `schema:ImageObject1`|
| _obj_original_url_ | `schema:targetUrl` | `schema:ImageObject1`|
| _obj_stored_url_ | `schema:url` | `schema:ImageObject1`|
| _webpage_uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:WebPage1` | `schema:image` | `schema:ImageObject1`|
