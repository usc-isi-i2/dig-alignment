## Basic Backpage Model

We use a backpage dataset from Andrew to define a basic model for a backpage page. The other models build on this model.

`backpage-uri-columns-model.ttl` is a model to define the URIs of the page elements so that we don't have to retype them when we build the other models.

### PyTransforms
#### _documentUri_
From column: _url_
>``` python
return documentUrl(getValue("url"))
```

#### _bodyUri_
From column: _bodyText / role_
>``` python
return getValue("url")+"/body"
```

#### _titleUri_
From column: _titleText / role_
>``` python
return getValue("url")+"/title"
```

#### _sidUri_
From column: _sid_
>``` python
return "backpage/"+getValue("sid")+"/identifier/sid"
```

#### _imageUri_
From column: _images / url_
>``` python
return "http://"+getValue("url")
```

#### _imageUrl_
From column: _images / imageUri_
>``` python
return "http://"+getValue("url")
```

#### _documentUrl_
From column: _documentUri_
>``` python
return getValue("documentUri")
```

#### _iataUri_
From column: _market_
>``` python
return "iata/"+getValue("market").lower()
```

#### _locationUri_
From column: _locationText / content_
>``` python
return "place/"+getValue("market").lower()+"/"+fingerprintString(getValue("content"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _bodyUri_ | `uri` | `schema:WebPageElement1`|
| _cacheUrl_ | `dig:cacheUrl` | `schema:ImageObject1`|
| _cacheUrl_ | `dig:cacheUrl` | `schema:WebPage1`|
| _content_ | `rdfs:label` | `schema:Place2`|
| _content_ | `schema:text` | `schema:WebPageElement2`|
| _content_ | `schema:text` | `schema:WebPageElement1`|
| _created_ | `schema:dateCreated` | `schema:WebPage1`|
| _documentUri_ | `uri` | `dig:URLEntity1`|
| _documentUrl_ | `schema:url` | `schema:WebPage1`|
| _iataUri_ | `uri` | `schema:Place1`|
| _imageUri_ | `uri` | `schema:ImageObject1`|
| _imageUrl_ | `schema:url` | `schema:ImageObject1`|
| _locationUri_ | `uri` | `schema:Place2`|
| _market_ | `schema:iataCode` | `schema:Place1`|
| _sid_ | `rdfs:label` | `dig:Identifier1`|
| _sidUri_ | `uri` | `dig:Identifier1`|
| _statedAge_ | `dig:mentionsPersonAge` | `schema:WebPage1`|
| _titleUri_ | `uri` | `schema:WebPageElement2`|
| _url_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `dig:URLEntity1` | `dig:snapshot` | `schema:WebPage1`|
| `schema:WebPage1` | `dig:hasBodyPart` | `schema:WebPageElement1`|
| `schema:WebPage1` | `dig:hasImagePart` | `schema:ImageObject1`|
| `schema:WebPage1` | `dig:hasTitlePart` | `schema:WebPageElement2`|
| `schema:WebPage1` | `dig:mentionsPlace` | `schema:Place2`|
| `schema:WebPage1` | `dig:preferredIdentifier` | `dig:Identifier1`|
| `schema:WebPage1` | `dig:primaryLocation` | `schema:Place1`|