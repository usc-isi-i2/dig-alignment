## sample.jl

### PyTransforms
#### _image_uri_
From column: _image_sha1_
>``` python
return getValue("image_sha1")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `uri` | `schema:WebPage1`|
| _image_sha1_ | `memex:identifier` | `schema:ImageObject1`|
| _image_uri_ | `uri` | `schema:ImageObject1`|
| _s3_url_ | `schema:url` | `schema:ImageObject1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:ImageObject1` | `memex:isImagePartOf` | `schema:WebPage1`|
| `schema:WebPage1` | `memex:hasImagePart` | `schema:ImageObject1`|
