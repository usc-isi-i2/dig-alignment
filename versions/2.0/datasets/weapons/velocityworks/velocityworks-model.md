## extracted_velocityworks.json

### PyTransforms
#### _uri_
From column: _url_
>``` python
return uri_from_url_timestamp(getValue("url"),getValue("timestamp"))
```

#### _cleanPrice_
From column: _price_
>``` python
return cleanPrice(getValue("price"))
```

#### _pricecurrency_
From column: _price_
>``` python
return getCurrency(getValue("price"))
```

#### _cleanimgurl_
From column: _images / src_
>``` python
return vw_clean_image_url(getValue("src"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:model` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _cleanPrice_ | `schema:price` | `schema:Offer1`|
| _cleanimgurl_ | `schema:url` | `schema:ImageObject1`|
| _description_ | `schema:description` | `schema:Offer1`|
| _organizationuri_ | `uri` | `schema:Organization1`|
| _pricecurrency_ | `schema:priceCurrency` | `schema:Offer1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|
| _url_ | `schema:url` | `schema:Offer1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Offer1` | `schema:publisher` | `schema:Organization1`|
| `schema:Offer1` | `schema:itemOffered` | `schema:Product1`|
| `schema:Organization1` | `schema:name` | `xsd:velocityworks.net`|
| `schema:OrganizationRole1` | `schema:memberOf` | `schema:Organization1`|
| `schema:Product1` | `schema:image` | `schema:ImageObject1`|
| `schema:Product1` | `schema:offers` | `schema:Offer1`|
| `schema:Product1` | `schema:memberOf` | `schema:OrganizationRole1`|
