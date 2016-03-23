## ht-cdr2-ads-500.jl

### PyTransforms
#### _adultservice_uri_
From column: _url_
>``` python
return 'adultservice/' + SM.sha1_hash(getValue("url").strip())
```

#### _clean_weight_
From column: _extractions / weight / results / value_
>``` python
return SM.clean_weight(getValue("value"))
```

#### _clean_height_
From column: _extractions / height / results / value_
>``` python
return SM.clean_height(getValue("value"))
```

#### _clean_name_
From column: _extractions / name / results / value_
>``` python
return SM.clean_name(getValue("value"))
```

#### _clean_age_
From column: _extractions / age / results / values_
>``` python
return SM.clean_age(getValue("values"))
```

#### _clean_ethnicity_
From column: _extractions / ethnicity / results / value_
>``` python
return SM.clean_ethnicity(getValue("value"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _adultservice_uri_ | `uri` | `memex:AdultService1`|
| _author_ | `schema:name` | `memex:UserName1`|
| _clean_age_ | `memex:age` | `memex:AdultService1`|
| _clean_ethnicity_ | `memex:ethnicity` | `memex:AdultService1`|
| _clean_height_ | `schema:height` | `memex:AdultService1`|
| _clean_name_ | `schema:name` | `memex:AdultService1`|
| _clean_weight_ | `schema:weight` | `memex:AdultService1`|
| _eventTime_ | `schema:startDate` | `schema:Event1`|
| _eventType_ | `km-dev:columnSubClassOfLink` | `schema:Event1`|
| _lat_ | `schema:latitude` | `schema:GeoCoordinates1`|
| _lon_ | `schema:longitude` | `schema:GeoCoordinates1`|
| _person_uri_ | `uri` | `schema:Person1`|
| _sentence_ | `schema:text` | `schema:CreativeWork1`|
| _sentiment_ | `memex:polarityValue` | `memex:Sentiment1`|
| _values_ | `schema:name` | `schema:CreativeWork1`|
| _values_ | `schema:name` | `schema:CreativeWork1`|
| _values_ | `schema:name` | `schema:Person2`|
| _values_ | `schema:name` | `memex:Topic1`|
| _values_ | `schema:mentions` | `schema:CreativeWork1`|
| _values_ | `schema:name` | `schema:Place1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
