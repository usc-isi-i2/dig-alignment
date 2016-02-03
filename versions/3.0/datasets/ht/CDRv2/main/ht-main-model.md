## ht-cdr2-ads-500.jl

### PyTransforms
#### _hash_url_
From column: _url_
>``` python
return SM.sha1_hash(getValue("url").strip())
```

#### _adultservice_uri_
From column: _hash_url_
>``` python
return 'adultservice/' + getValue('hash_url')
```

#### _seller_uri_
From column: _adultservice_uri_
>``` python
return 'seller/' + getValue('hash_url')
```

#### _offer_uri_
From column: _isi_id_
>``` python
return "offer/" + getValue("isi_id")
```

#### _webpage_uri_
From column: _offer_uri_
>``` python
return "webpage/" + getValue("isi_id")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _adultservice_uri_ | `uri` | `memex:AdultService1`|
| _offer_uri_ | `uri` | `schema:Offer1`|
| _seller_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _webpage_uri_ | `uri` | `schema:WebPage1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:AdultService1` | `schema:offers` | `schema:Offer1`|
| `memex:PersonOrOrganization1` | `schema:makesOffer` | `schema:Offer1`|
| `schema:Offer1` | `schema:itemOffered` | `memex:AdultService1`|
| `schema:Offer1` | `schema:seller` | `memex:PersonOrOrganization1`|
| `schema:Offer1` | `schema:mainEntityOfPage` | `schema:WebPage1`|
| `schema:WebPage1` | `schema:mainEntity` | `schema:Offer1`|
