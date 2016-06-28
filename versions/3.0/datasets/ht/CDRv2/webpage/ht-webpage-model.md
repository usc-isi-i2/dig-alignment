## cdr_for_webpage.jl

### PyTransforms
#### _clean_text_
From column: _extractions / text / results / values_
>``` python
return HM.clean_html_tags(getValue("values"))
```

#### _clean_title_
From column: _extractions / title / results / values_
>``` python
return HM.clean_html_tags(getValue("values"))
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

#### _webpage_uri_
From column: _isi_id_
>``` python
return 'webpage/' + getValue("isi_id")
```

#### _posttime_extraction_
From column: _crawl_data / context / timestamp_
>``` python
return getValueFromNestedColumnByIndex("extractions", "posttime/results/values",0)
```

#### _date_created_
From column: _crawl_data / context / timestamp_
>``` python
return DM.date_created(getValue("posttime_extraction"), getValue("timestamp"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _clean_text_ | `schema:description` | `schema:WebPage1`|
| _clean_title_ | `schema:name` | `schema:WebPage1`|
| _date_created_ | `schema:dateCreated` | `schema:WebPage1`|
| _domain_url_ | `schema:name` | `schema:Organization1`|
| _organization_domain_uri_ | `uri` | `schema:Organization1`|
| _url_ | `schema:url` | `schema:WebPage1`|
| _webpage_uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:WebPage1` | `schema:publisher` | `schema:Organization1`|
