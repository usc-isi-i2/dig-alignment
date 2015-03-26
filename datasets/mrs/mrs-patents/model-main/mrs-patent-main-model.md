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

#### _modtime_
From column: _modtime_
>``` python
return iso8601date(getCurrentTime(), "%Y-%m-%d %H:%M:%S")
```

#### _publicationdate_
From column: _publicationdate_
>``` python
return iso8601date(getValue("Publication Date"), '%b %d, %Y')
```

#### _citedUris_
From column: _CitedPatents / citedUris_
>``` python
return "page/" + getValue("values") + "/processed"
```

#### _referencedByUris_
From column: _ReferencedBy / referencedByUris_
>``` python
return "page/" + getValue("values").strip() + "/processed"
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Abstract_ | `schema:text` | `schema:WebPageElement1`|
| _Description_ | `schema:text` | `schema:WebPageElement3`|
| _Patent Title_ | `schema:text` | `schema:WebPageElement2`|
| _abstract_uri_ | `uri` | `schema:WebPageElement1`|
| _citedUris_ | `uri` | `schema:WebPage2`|
| _image_uri1_ | `uri` | `schema:ImageObject1`|
| _modtime_ | `prov:endedAtTime` | `prov:Activity1`|
| _publicationUri_ | `memex:publicationUri` | `schema:WebPage1`|
| _publicationdate_ | `schema:datePublished` | `schema:WebPage1`|
| _referencedByUris_ | `uri` | `schema:WebPage3`|
| _title_uri_ | `uri` | `schema:WebPageElement2`|
| _uri_ | `uri` | `schema:WebPage1`|
| _url_ | `schema:url` | `schema:WebPage1`|
| _values_ | `schema:url` | `schema:ImageObject1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `prov:Activity1` | `prov:wasAttributedTo` | `xsd:http://dig.isi.edu/mrs/data/api/google`|
| `schema:ImageObject1` | `prov:wasGeneratedBy` | `prov:Activity1`|
| `schema:WebPage1` | `memex:hasAbstractPart` | `schema:WebPageElement1`|
| `schema:WebPage1` | `memex:hasBodyPart` | `schema:WebPageElement3`|
| `schema:WebPage1` | `memex:hasImagePart` | `schema:ImageObject1`|
| `schema:WebPage1` | `memex:hasTitlePart` | `schema:WebPageElement2`|
| `schema:WebPage1` | `memex:isCitationOf` | `schema:WebPage3`|
| `schema:WebPage1` | `schema:citation` | `schema:WebPage2`|
