## sample.jl

### PyTransforms
#### _image_uri_
From column: _image_sha1_
>``` python
return getValue("image_sha1")
```

#### _webpage_uri_
From column: _obj_parent_ids / Values_
>``` python
return "webpage/" + getValue("Values")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _image_sha1_ | `memex:identifier` | `schema:ImageObject1`|
| _image_uri_ | `uri` | `schema:ImageObject1`|
| _s3_url_ | `schema:url` | `schema:ImageObject1`|
| _webpage_uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:ImageObject1` | `memex:isImagePartOf` | `schema:WebPage1`|
| `schema:WebPage1` | `memex:hasImagePart` | `schema:ImageObject1`|
