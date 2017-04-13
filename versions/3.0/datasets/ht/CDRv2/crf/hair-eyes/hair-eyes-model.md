## sample.jl

### PyTransforms
#### _adultservice_uri_
From column: _url_
>``` python
return 'adultservice/' + SM.sha1_hash(getValue("url").strip())
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _adultservice_uri_ | `uri` | `memex:AdultService1`|
| _eyeColor_agg_ | `memex:eyeColor` | `memex:AdultService1`|
| _hairType_agg_ | `memex:hairColor` | `memex:AdultService1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
