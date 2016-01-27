## ht-cdr2-ads-500.jl

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

#### _organization_uri_
From column: _crawl_data / domain_
>``` python
return 'organization/' + getValue("domain")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _adultservice_uri_ | `uri` | `memex:AdultService1`|
| _author_ | `schema:name` | `memex:UserName1`|
| _clean_age_ | `memex:age` | `memex:AdultService1`|
| _clean_email_ | `schema:name` | `memex:EmailAddress1`|
| _clean_ethnicity_ | `memex:ethnicity` | `memex:AdultService1`|
| _clean_height_ | `schema:height` | `memex:AdultService1`|
| _clean_name_ | `schema:name` | `memex:AdultService1`|
| _clean_text_ | `schema:description` | `schema:WebPage1`|
| _clean_text_ | `schema:description` | `schema:WebPage1`|
| _clean_weight_ | `schema:weight` | `memex:AdultService1`|
| _domain_ | `schema:name` | `schema:Organization1`|
| _domain_ | `schema:name` | `schema:Organization1`|
| _email_uri_ | `uri` | `memex:EmailAddress1`|
| _eventTime_ | `schema:startDate` | `schema:Event1`|
| _eventType_ | `km-dev:columnSubClassOfLink` | `schema:Event1`|
| _extractions_Glue_1_extractions_phone_results_values_ | `schema:name` | `memex:PhoneNumber1`|
| _lat_ | `schema:latitude` | `schema:GeoCoordinates1`|
| _lon_ | `schema:longitude` | `schema:GeoCoordinates1`|
| _organization_uri_ | `uri` | `schema:Organization1`|
| _organization_uri_ | `uri` | `schema:Organization1`|
| _person_uri_ | `uri` | `schema:Person1`|
| _phone_uri_ | `uri` | `memex:PhoneNumber1`|
| _seller_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _sentence_ | `schema:text` | `schema:CreativeWork1`|
| _sentiment_ | `memex:polarityValue` | `memex:Sentiment1`|
| _values_ | `schema:name` | `schema:CreativeWork1`|
| _values_ | `schema:url` | `schema:WebPage1`|
| _values_ | `schema:name` | `schema:CreativeWork1`|
| _values_ | `schema:name` | `schema:WebPage1`|
| _values_ | `schema:url` | `schema:WebPage1`|
| _values_ | `schema:name` | `schema:Person2`|
| _values_ | `schema:name` | `memex:Identifier1`|
| _values_ | `schema:name` | `memex:Topic1`|
| _values_ | `schema:name` | `schema:WebPage1`|
| _values_ | `schema:mentions` | `schema:CreativeWork1`|
| _values_ | `schema:name` | `schema:Place1`|
| _webpage_uri_ | `uri` | `schema:WebPage1`|
| _webpage_uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Identifier1` | `memex:hasType` | `xsd:http://dig.isi.edu/thesaurus/identifier/sources-id`|
| `schema:WebPage1` | `memex:identifier` | `memex:Identifier1`|
| `schema:WebPage1` | `schema:publisher` | `schema:Organization1`|
