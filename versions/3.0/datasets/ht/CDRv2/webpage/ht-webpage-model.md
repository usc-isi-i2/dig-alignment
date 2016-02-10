## hbase_sample_100_karma.jl

### PyTransforms
#### _webpage_uri_
From column: _isi_id_
>``` python
return 'webpage/' + getValue("isi_id")
```

#### _clean_text_
From column: _extractions / text / results / values_
>``` python
return HM.clean_html_tags(getValue("values"))
```

#### _iso_posttime_
From column: _extractions / posttime / results / values_
>``` python
posttime = getValue("values")
if posttime.strip() != '':
    return DM.iso8601date(posttime,'%Y-%m-%d %H:%M:%S')
posttime = getValue("timestamp")
return DM.epoch_to_iso8601(posttime)
```

#### _domain_url_
From column: _url_
>``` python
return SM.get_website_domain_only(getValue("url"))
```

#### _organization_domain_uri_
From column: _domain_url_
>``` python
return 'organization/' + getValue("domain_url")
```

#### _iso_posttime2_
From column: _crawl_data / context / timestamp_
>``` python
ts = getValue("timestamp")
return DM.epoch_to_iso8601(ts)
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _clean_text_ | `schema:description` | `schema:WebPage1`|
| _domain_url_ | `schema:name` | `schema:Organization1`|
| _iso_posttime2_ | `schema:dateCreated` | `schema:WebPage1`|
| _organization_domain_uri_ | `uri` | `schema:Organization1`|
| _url_ | `schema:url` | `schema:WebPage1`|
| _values_ | `schema:name` | `schema:WebPage1`|
| _webpage_uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:WebPage1` | `schema:publisher` | `schema:Organization1`|
