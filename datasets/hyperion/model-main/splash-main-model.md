## splash.json

### PyTransforms
#### _cache_uri_
From column: _timestamp_
>``` python
return getCacheBaseUrl()+"page/"+get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/processed"
```

#### _snapshot_uri_
From column: _cache_uri_
>``` python
return getCacheBaseUrl()+"page/"+get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/raw"
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _cache_uri_ | `uri` | `schema:WebPage1`|
| _category_ | `schema:category` | `schema:Organization1`|
| _extractedText_ | `schema:text` | `schema:WebPageElement1`|
| _language_ | `schema:inLanguage` | `schema:WebPage1`|
| _rawHTMLURL_ | `memex:cacheUrl` | `schema:WebPage1`|
| _rawImageURL_ | `memex:cacheUrl` | `schema:ImageObject1`|
| _resource_ | `rdfs:label` | `schema:Organization1`|
| _snapshot_uri_ | `memex:snapshotUri` | `schema:WebPage1`|
| _url_ | `schema:url` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:WebPage1` | `memex:hasBodyPart` | `schema:WebPageElement1`|
| `schema:WebPage1` | `memex:hasImagePart` | `schema:ImageObject1`|
| `schema:WebPage1` | `schema:provider` | `schema:Organization1`|
