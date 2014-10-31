## images-sample.json

### PyTransforms
#### _ad_crawl_uri_
From column: _ad_url_
>``` python
return getCacheBaseUrl()+"page/"+get_url_hash(getValue("ad_url"))+"/"+getValue("ad_timestamp")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ad_crawl_uri_ | `uri` | `schema:WebPage1`|
| _importtime_ | `prov:generatedAtTime` | `schema:ImageObject1`|
| _location_ | `uri` | `schema:ImageObject1`|
| _url_ | `schema:url` | `schema:ImageObject1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:WebPage1` | `memex:hasImagePart` | `schema:ImageObject1`|
