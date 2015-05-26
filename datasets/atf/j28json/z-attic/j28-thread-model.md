## j28-labeled-sample.json

### PyTransforms
#### _sourceName_
From column: _originalfile_
>``` python
return j28SourceName(getValue("originalfile"))
```

#### _siteRoot_
From column: _sourceName_
>``` python
return j28SiteRoot(getValue("sourceName"))
```

#### _threadLinkAbsolute_
From column: _thread_link_
>``` python
return j28ThreadLinkAbsolute(getValue("siteRoot"), getValue("thread_link"))
```

#### _threadUri_
From column: _threadLinkAbsolute_
>``` python
return j28ThreadUri(getValue("threadLinkAbsolute"))
```

#### _postUri_
From column: _link_
>``` python
return j28PostUri(getValue("link"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _postUri_ | `uri` | `memex:Post1`|
| _threadUri_ | `uri` | `memex:Thread1`|
| _thread_id_ | `rdfs:label` | `memex:Identifier1`|
| _thread_name_ | `schema:text` | `schema:WebPageElement1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Thread1` | `memex:hasIdentifier` | `memex:Identifier1`|
| `memex:Thread1` | `memex:hasPost` | `memex:Post1`|
| `memex:Thread1` | `memex:hasTitlePart` | `schema:WebPageElement1`|
