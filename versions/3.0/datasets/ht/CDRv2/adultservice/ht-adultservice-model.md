## cdr_with_name.jl

### PyTransforms
#### _adultservice_uri_
From column: _url_
>``` python
return 'adultservice/' + SM.sha1_hash(getValue("url").strip())
```

#### _clean_weight_
From column: _extractions / weight / results / values_
>``` python
return SM.clean_weight(getValue("values"))
```

#### _clean_height_
From column: _extractions / height / results / values_
>``` python
return SM.clean_height(getValue("values"))
```

#### _clean_name_
From column: _extractions / name / results / values_
>``` python
return SM.clean_name(getValue("values"))
```

#### _clean_age_
From column: _extractions / age / results / values_
>``` python
return SM.clean_age(getValue("values"))
```

#### _clean_ethnicity_
From column: _extractions / ethnicity / results / values_
>``` python
return SM.clean_ethnicity(getValue("values"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _adultservice_uri_ | `uri` | `memex:AdultService1`|
| _clean_age_ | `memex:age` | `memex:AdultService1`|
| _clean_height_ | `schema:height` | `memex:AdultService1`|
| _clean_weight_ | `schema:weight` | `memex:AdultService1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
