## jpl-pdf-sample.json

### PyTransforms
#### _article_uri_
From column: _fileName_
>``` python
return jp_article_uri(getValue("fileName"))
```

#### _author_uri_
From column: _references / biblStruct / analytic / author / persName / forename / author_uri_
>``` python
if getValue('@type') == 'first':
    return jp_author_uri(getValue("#text"),getValue("surname"))
else:
    return ''
```

#### _author_name_
From column: _references / biblStruct / analytic / author / persName / forename / author_uri_
>``` python
if getValue('@type') == 'first':
    return jp_author_name(getValue("#text"),getValue("surname"))
else:
    return ''
```

#### _article_author_name_
From column: _authors / persName / forename / #text_
>``` python
if getValue('@type') == 'first':
    return jp_author_name(getValue("#text"),getValue("surname"))
else:
    return ''
```

#### _article_author_uri_
From column: _authors / persName / forename / #text_
>``` python
if getValue('@type') == 'first':
    return jp_author_uri(getValue("#text"),getValue("surname"))
else:
    return ''
```

#### _author_name_nromalized_
From column: _references / biblStruct / analytic / author / persName / forename / author_name_
>``` python
if getValue('@type') == 'first':
    return jp_author_name_normalized(getValue("#text")+" "+getValue("surname"))
else:
    return ''
```

#### _year_published_
From column: _references / biblStruct / monogr / imprint / date / @when_
>``` python
return jp_clean_year_best_effort(getValue("@when"))
```

#### _article_author_name_normalized_
From column: _authors / persName / forename / article_author_name_
>``` python
if getValue('@type') == 'first':
    return jp_author_name_normalized(getValue("#text")+' '+getValue("surname"))
else:
    return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _#text_ | `schema:name` | `schema:Organization1`|
| _#text_ | `schema:name` | `schema:ScholarlyArticle2`|
| _#text_ | `schema:title` | `schema:ScholarlyArticle1`|
| _abstract_ | `schema:text` | `schema:ScholarlyArticle2`|
| _article_author_name_ | `schema:alternateName` | `schema:Person2`|
| _article_author_name_normalized_ | `schema:name` | `schema:Person2`|
| _article_author_uri_ | `uri` | `schema:Person2`|
| _article_uri_ | `uri` | `schema:ScholarlyArticle2`|
| _author_name_ | `schema:alternateName` | `schema:Person1`|
| _author_name_nromalized_ | `schema:name` | `schema:Person1`|
| _author_uri_ | `uri` | `schema:Person1`|
| _email_ | `schema:email` | `schema:Person2`|
| _settlement_ | `schema:name` | `schema:Place1`|
| _year_published_ | `schema:datePublished` | `schema:ScholarlyArticle1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Organization1` | `schema:location` | `schema:Place1`|
| `schema:Person2` | `memex:isAuthorOf` | `schema:ScholarlyArticle2`|
| `schema:ScholarlyArticle1` | `schema:author` | `schema:Person1`|
| `schema:ScholarlyArticle2` | `schema:citation` | `schema:ScholarlyArticle1`|
| `schema:ScholarlyArticle2` | `schema:sourceOrganization` | `schema:Organization1`|
| `schema:ScholarlyArticle2` | `schema:author` | `schema:Person2`|
