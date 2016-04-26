## sample.jl

### PyTransforms
#### _image1_sha1_
From column: _sha1_pair_
>``` python
return getValue("sha1_pair").split('-')[0]
```

#### _image2_sha1_
From column: _image1_sha1_
>``` python
return getValue("sha1_pair").split('-')[1]
```

#### _image1_uri_
From column: _image1_sha1_
>``` python
return getValue("image1_sha1")
```

#### _role_uri_
From column: _image1_uri_
>``` python
return getValue("image1_sha1") + "/role"
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _dist_ | `memex:similarityScore` | `schema:Role1`|
| _image1_sha1_ | `memex:identifier` | `schema:ImageObject1`|
| _image1_uri_ | `uri` | `schema:ImageObject1`|
| _image2_sha1_ | `memex:similarImageId` | `schema:Role1`|
| _role_uri_ | `uri` | `schema:Role1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:ImageObject1` | `memex:similarImageId` | `schema:Role1`|
