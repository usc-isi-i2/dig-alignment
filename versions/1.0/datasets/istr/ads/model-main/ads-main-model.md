## ads-sample.json

### PyTransforms
#### _cache_uri_
From column: _url_
>``` python
return "page/"+get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/processed"
```

#### _snapshot_uri_
From column: _cache_uri_
>``` python
return getHTBaseUrl() + "page/"+get_url_hash(getValue("url"))+"/"+getValue("timestamp")+"/raw"
```

#### _posttime_iso_
From column: _posttime_
>``` python
return iso8601date(getValue("posttime"))
```

#### _sources_uri_
From column: _sources_id_
>``` python
return organization_uri(getValue("sources_id"))
```

#### _title_uri_
From column: _title_
>``` python
if getValue("title"):
  return getValue("cache_uri") + "/title"
return ''
```

#### _body_uri_
From column: _text_
>``` python
if getValue("text"):
  return getValue("cache_uri") + "/body"
return ''
```

#### _import_time_
From column: _timestamp_
>``` python
return iso8601date(getValue("timestamp"), "%f")
```

#### _dateMostLikelyCreated_
From column: _posttime_iso_
>``` python
posttime = getValue("posttime_iso")
if posttime:
  return posttime
return getValue("import_time")
```

#### _modtime_iso_
From column: _modtime_
>``` python
return iso8601date(getValue("modtime"))
```

#### _title_hash_
From column: _title_
>``` python
return getTextHash(getValue("title"))
```

#### _body_hash_
From column: _text_
>``` python
return getTextHash(getValue("text"))
```

#### _webpage_hash_
From column: _body_uri_
>``` python
return getValue("title_hash") + "_" +  getValue("body_hash")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _body_hash_ | `memex:textChecksum` | `schema:WebPageElement2`|
| _body_uri_ | `uri` | `schema:WebPageElement2`|
| _cache_uri_ | `uri` | `schema:WebPage1`|
| _dateMostLikelyCreated_ | `memex:dateMostLikelyCreated` | `schema:WebPage1`|
| _id_ | `rdfs:label` | `memex:Identifier1`|
| _import_time_ | `memex:dateCrawled` | `schema:WebPage1`|
| _modtime_iso_ | `schema:dateModified` | `schema:WebPage1`|
| _posttime_iso_ | `schema:dateCreated` | `schema:WebPage1`|
| _snapshot_uri_ | `memex:snapshotUri` | `schema:WebPage1`|
| _sources_uri_ | `uri` | `schema:Organization1`|
| _text_ | `schema:text` | `schema:WebPageElement2`|
| _title_ | `schema:text` | `schema:WebPageElement1`|
| _title_hash_ | `memex:textChecksum` | `schema:WebPageElement1`|
| _title_uri_ | `uri` | `schema:WebPageElement1`|
| _url_ | `schema:url` | `schema:WebPage1`|
| _webpage_hash_ | `memex:textChecksum` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Identifier1` | `memex:hasType` | `xsd:http://dig.isi.edu/ht/data/thesaurus/identifier/ht-database`|
| `schema:WebPage1` | `memex:hasBodyPart` | `schema:WebPageElement2`|
| `schema:WebPage1` | `memex:hasIdentifier` | `memex:Identifier1`|
| `schema:WebPage1` | `memex:hasTitlePart` | `schema:WebPageElement1`|
| `schema:WebPage1` | `schema:provider` | `schema:Organization1`|
