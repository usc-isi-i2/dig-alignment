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

#### _similar_image_uri_
From column: _Glue_1 / similar_image_ids_Values_
>``` python
return "image/" + getValue("similar_image_ids_Values")
```

#### _role_uri_
From column: _Glue_1 / image_dist_Values_
>``` python
if getValue("similar_image_ids_Values").strip() == '':
    return ''
return uri_from_fields('role_', getValue("similar_image_ids_Values"),getValue("images_id"),getValue("ads_id"))
```

#### _image_dist_clean_values_
From column: _Glue_1 / image_dist_Values_
>``` python
return '{0:.15f}'.format(float(getValue("image_dist_Values")))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _adultservice_uri_ | `uri` | `memex:AdultService1`|
| _image_dist_clean_values_ | `memex:similarityScore` | `schema:Role1`|
| _images_uri_ | `uri` | `schema:ImageObject1`|
| _original_url_ | `schema:targetUrl` | `schema:ImageObject1`|
| _role_uri_ | `uri` | `schema:Role1`|
| _s3_url_ | `schema:url` | `schema:ImageObject1`|
| _similar_image_uri_ | `uri` | `schema:ImageObject2`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:AdultService1` | `schema:image` | `schema:ImageObject1`|
| `schema:ImageObject1` | `schema:isSimilarTo` | `schema:Role1`|
| `schema:Role1` | `schema:isSimilarTo` | `schema:ImageObject2`|