## sample.jl

### PyTransforms

### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `uri` | `schema:WebPage1`|
| _all_cdr_ids_ | `schema:name` | `memex:Identifier1`|
| _image_sha1_ | `uri` | `schema:ImageObject1`|
| _s3_url_ | `schema:url` | `schema:ImageObject1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Identifier1` | `memex:hasType` | `xsd:cdr_id`|
| `schema:ImageObject1` | `memex:identifier` | `memex:Identifier1`|
| `schema:ImageObject1` | `memex:isImagePartOf` | `schema:WebPage1`|
| `schema:WebPage1` | `memex:hasImagePart` | `schema:ImageObject1`|
