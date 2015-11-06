## ads-images-map.json

### PyTransforms
#### _images_uri_
From column: _images_id_
>``` python
return "image/" + getValue("images_id")
```

#### _adultservice_uri_
From column: _ads_id_
>``` python
return genericUri("","",getValue("ads_url").strip()) + "adultservice"
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _adultservice_uri_ | `uri` | `memex:AdultService1`|
| _images_uri_ | `uri` | `schema:ImageObject1`|
| _original_url_ | `schema:targetUrl` | `schema:ImageObject1`|
| _s3_url_ | `schema:url` | `schema:ImageObject1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:AdultService1` | `schema:image` | `schema:ImageObject1`|
