## sample.json

### PyTransforms
#### _patent_nos_
From column: __source / crawl_data / mentions-patents / values_
>``` python
return clean_patent_number(getValue("values"))
```

#### _patent_uri_
From column: __source / crawl_data / mentions-patents / patent_nos_
>``` python
return pt_patent_uri(getValue("patent_nos"))
```

#### _date_filed_iso_
From column: __source / crawl_data / case / date_filed_
>``` python
return iso8601date(getValue("date_filed"))
```

#### _legalaction_uri_
From column: __source / url_
>``` python
return pt_legal_action_uri(getValue("url"))
```

#### _court_state_
From column: __source / crawl_data / court_
>``` python
return standardize_state_code("US", pt_get_court_state(getValue("court")))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _case_name_ | `schema:name` | `memex:LegalAction1`|
| _court_ | `schema:name` | `schema:Place1`|
| _court_state_ | `schema:addressRegion` | `schema:PostalAddress1`|
| _date_filed_iso_ | `schema:startTime` | `memex:LegalAction1`|
| _docket_number_ | `schema:name` | `memex:Identifier1`|
| _federal_cite_ | `schema:name` | `memex:Identifier2`|
| _full-text_ | `schema:text` | `schema:WebPageElement1`|
| _legalaction_uri_ | `uri` | `memex:LegalAction1`|
| _patent_uri_ | `uri` | `memex:Patent1`|
| _url_ | `schema:url` | `schema:WebPageElement1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Identifier1` | `memex:hasType` | `xsd:http://dig.isi.edu/patents/data/thesaurus/identifier/docketnumber`|
| `memex:Identifier2` | `memex:hasType` | `xsd:http://dig.isi.edu/patents/data/thesaurus/identifier/federalcite`|
| `memex:LegalAction1` | `memex:identifier` | `memex:Identifier1`|
| `memex:LegalAction1` | `memex:identifier` | `memex:Identifier2`|
| `memex:LegalAction1` | `schema:location` | `schema:Place1`|
| `memex:LegalAction1` | `schema:mainEntityOfPage` | `schema:WebPageElement1`|
| `memex:Patent1` | `memex:legalAction` | `memex:LegalAction1`|
| `schema:Place1` | `schema:address` | `schema:PostalAddress1`|
| `schema:PostalAddress1` | `schema:addressCountry` | `xsd:US`|
