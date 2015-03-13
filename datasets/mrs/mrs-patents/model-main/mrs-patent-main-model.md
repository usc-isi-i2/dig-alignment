## mrs-patent-data-sample.json

### PyTransforms
#### _uri_
From column: _uri_
>``` python
publicationNumber = getValue("Publication Number")
publicationNumber = ''.join(publicationNumber.split())
return "page/" + publicationNumber + "/processed"
```

#### _url_
From column: _url_
>``` python
return getValue("URL")
```

#### _publicationUri_
From column: _publicationUri_
>``` python
publicationNumber =  getValue("Publication Number")
patentNumber = publicationNumber.split(' ')
return "page/" + patentNumber[0] + "/processed/"
```

#### _abstract_uri_
From column: _abstract_uri_
>``` python
return getValue("uri") + "/abstract"
```

#### _title_uri_
From column: _title_uri_
>``` python
return getValue("uri") + "/title"
```

#### _image_uri_
From column: _image_uri_
>``` python
publicationNumber =  getValue("Publication Number") 
publicationNumber = ''.join(publicationNumber.split())
return "image/" + publicationNumber + "/processed"
```

#### _image_uri1_
From column: _Thumbnail Image / values_
>``` python
return "image/"+get_url_hash(getValue("values"))+"/processed"

```

#### _values_
From column: _Thumbnail Image / values_
>``` python
url =  getValue("values")
url = url[0:]
url = 'http:' + url
return url
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Abstract_ | `schema:text` | `schema:WebPageElement1`|
| _Description_ | `schema:text` | `schema:WebPageElement3`|
| _Patent Title_ | `schema:text` | `schema:WebPageElement2`|
| _abstract_uri_ | `uri` | `schema:WebPageElement1`|
| _image_uri1_ | `uri` | `schema:ImageObject1`|
| _publicationUri_ | `memex:publicationUri` | `schema:WebPage1`|
| _title_uri_ | `uri` | `schema:WebPageElement2`|
| _uri_ | `uri` | `schema:WebPage1`|
| _url_ | `schema:url` | `schema:WebPage1`|
| _values_ | `schema:url` | `schema:ImageObject1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:WebPage1` | `memex:hasAbstractPart` | `schema:WebPageElement1`|
| `schema:WebPage1` | `memex:hasBodyPart` | `schema:WebPageElement3`|
| `schema:WebPage1` | `memex:hasImagePart` | `schema:ImageObject1`|
| `schema:WebPage1` | `memex:hasTitlePart` | `schema:WebPageElement2`|
