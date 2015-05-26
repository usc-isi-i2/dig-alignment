## j28-sample.json

### PyTransforms
#### _postUri_
From column: _link_
>``` python
return j28PostUri(getValue("link"))
```

#### _createdAtIso_
From column: _created_at_
>``` python
return iso8601date(getValue("created_at"))
```

#### _fcUri_
From column: _postUri_
>``` python
return j28FcUri(getValue("postUri"))
```

#### _username2_
From column: _author / username_
>``` python
return getValue("username")
```

#### _location2_
From column: _author / location_
>``` python
return getValue("location")
```

#### _imageUri_
From column: _image_urls / values_
>``` python
return j28ImageUri(getValue("values"))
```

#### _dollarPricesJoined_
From column: _content_
>``` python
return get_dollar_prices(getValue("content"), getValue("title"))
```

#### _dollarPrice2_
From column: _dollarPrices / Values_
>``` python
return getValue("Values")
```

#### _bitcoinPricesJoined_
From column: _dollarPricesJoined_
>``` python
return get_bitcoin_prices(getValue("content"), getValue("title"))
```

#### _bitcoinPrice2_
From column: _bitcoinPrices / Values_
>``` python
return getValue("Values")
```

#### _inferredSourceName_
From column: _originalfile_
>``` python
return inferSourceName(getValue("thread_link"), getValue("link"))
```

#### _originalfile_
From column: _originalfile_
>``` python
return getValue("inferredSourceName") + ".json"
```

#### _inferredSourceName2_
From column: _inferredSourceName_
>``` python
return getValue("inferredSourceName")
```

#### _siteRoot_
From column: _inferredSourceName2_
>``` python
return j28SiteRoot(getValue("inferredSourceName"))
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

#### _threadFcUri_
From column: _threadUri_
>``` python
return j28FcUri(getValue("threadUri"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `memex:featureValue` | `memex:Feature4`|
| _Values_ | `memex:featureValue` | `memex:Feature3`|
| _bitcoinPrice2_ | `memex:bitcoinPricesMentioned` | `memex:Feature4`|
| _content_ | `schema:text` | `schema:WebPageElement2`|
| _createdAtIso_ | `schema:dateCreated` | `memex:Post1`|
| _dollarPrice2_ | `memex:pricesMentioned` | `memex:Feature3`|
| _fcUri_ | `uri` | `memex:FeatureCollection1`|
| _imageUri_ | `uri` | `schema:ImageObject1`|
| _inferredSourceName_ | `memex:featureValue` | `memex:Feature5`|
| _inferredSourceName2_ | `memex:website` | `memex:Feature5`|
| _item_id_ | `rdfs:label` | `memex:Identifier1`|
| _location_ | `memex:featureValue` | `memex:Feature2`|
| _location2_ | `memex:place_postalAddress` | `memex:Feature2`|
| _postUri_ | `uri` | `memex:Post1`|
| _threadFcUri_ | `uri` | `memex:FeatureCollection2`|
| _threadUri_ | `uri` | `memex:Thread1`|
| _thread_id_ | `rdfs:label` | `memex:Identifier2`|
| _thread_name_ | `schema:text` | `schema:WebPageElement3`|
| _title_ | `schema:text` | `schema:WebPageElement1`|
| _username_ | `memex:featureValue` | `memex:Feature1`|
| _username2_ | `memex:person_username` | `memex:Feature1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Feature1` | `memex:featureName` | `xsd:person_username`|
| `memex:Feature2` | `memex:featureName` | `xsd:place_postalAddress`|
| `memex:Feature3` | `memex:featureName` | `xsd:prices_mentioned`|
| `memex:Feature4` | `memex:featureName` | `xsd:bitcoin_pricesMentioned`|
| `memex:Feature5` | `memex:featureName` | `xsd:website`|
| `memex:FeatureCollection1` | `memex:bitcoinPricesMentioned_feature` | `memex:Feature4`|
| `memex:FeatureCollection1` | `memex:person_username_feature` | `memex:Feature1`|
| `memex:FeatureCollection1` | `memex:place_postalAddress_feature` | `memex:Feature2`|
| `memex:FeatureCollection1` | `memex:pricesMentioned_feature` | `memex:Feature3`|
| `memex:FeatureCollection2` | `memex:website_feature` | `memex:Feature5`|
| `memex:Post1` | `memex:hasBodyPart` | `schema:WebPageElement2`|
| `memex:Post1` | `memex:hasFeatureCollection` | `memex:FeatureCollection1`|
| `memex:Post1` | `memex:hasIdentifier` | `memex:Identifier1`|
| `memex:Post1` | `memex:hasImagePart` | `schema:ImageObject1`|
| `memex:Post1` | `memex:hasTitlePart` | `schema:WebPageElement1`|
| `memex:Thread1` | `memex:hasFeatureCollection` | `memex:FeatureCollection2`|
| `memex:Thread1` | `memex:hasIdentifier` | `memex:Identifier2`|
| `memex:Thread1` | `memex:hasPost` | `memex:Post1`|
| `memex:Thread1` | `memex:hasTitlePart` | `schema:WebPageElement3`|
