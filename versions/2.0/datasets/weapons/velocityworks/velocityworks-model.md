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
| _#text_ | `schema:title` | `schema:ScholarlyArticle2`|
| _#text_ | `schema:name` | `schema:Organization1`|
| _Feedback_ | `schema:ratingValue` | `schema:AggregateRating1`|
| _Patent-id_ | `uri` | `memex:Patent2`|
| _Posts_ | `memex:activityCount` | `schema:OrganizationRole1`|
| _SKU_ | `schema:sku` | `schema:Offer1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:postalCode` | `schema:PostalAddress1`|
| _Values_ | `schema:subtype` | `schema:Organization1`|
| _Values_ | `schema:model` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:itemCondition` | `schema:Product1`|
| _Values_ | `schema:model` | `schema:Product1`|
| _Values_ | `schema:name` | `schema:Place2`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:email` | `schema:ContactPoint1`|
| _Values_ | `schema:description` | `memex:PersonOrOrganization1`|
| _Values_ | `schema:manufacturer` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:category` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:name` | `schema:State1`|
| _Values_ | `schema:keywords` | `schema:Product1`|
| _Values_ | `schema:status` | `schema:GovernmentPermit1`|
| _Values_date_iso_ | `schema:validFrom` | `schema:GovernmentPermit1`|
| _abstract_ | `schema:text` | `schema:ScholarlyArticle1`|
| _applicant_address_uri_ | `uri` | `schema:PostalAddress2`|
| _article_author_name_ | `schema:alternateName` | `schema:Person2`|
| _article_author_name_normalized_ | `schema:name` | `schema:Person2`|
| _article_author_uri_ | `uri` | `schema:Person2`|
| _article_uri_ | `uri` | `schema:ScholarlyArticle1`|
| _asignee_role_date_ | `schema:startDate` | `schema:Role1`|
| _assignee_address_uri_ | `uri` | `schema:PostalAddress1`|
| _brand_ | `schema:name` | `schema:Brand1`|
| _category_ | `schema:category` | `schema:Offer1`|
| _cause_clean_ | `schema:name` | `memex:LegalActionCause1`|
| _city_ | `schema:addressLocality` | `schema:PostalAddress2`|
| _city_ | `schema:addressLocality` | `schema:PostalAddress3`|
| _city_ | `schema:addressLocality` | `schema:PostalAddress1`|
| _cleanPrice_ | `schema:price` | `schema:Offer1`|
| _cleanPrice_ | `schema:price` | `schema:Offer1`|
| _clean_alt_phone_ | `schema:name` | `memex:PhoneNumber2`|
| _clean_phone_ | `schema:name` | `memex:PhoneNumber1`|
| _clean_price_btc_ | `schema:price` | `schema:PriceSpecification2`|
| _cleanimgurl_ | `schema:url` | `schema:ImageObject1`|
| _cleanimgurl_ | `schema:url` | `schema:ImageObject1`|
| _contact_point_uri_ | `uri` | `schema:ContactPoint1`|
| _content_ | `schema:name` | `memex:Patent2`|
| _content_clean_ | `schema:text` | `schema:WebPageElement3`|
| _country_ | `schema:addressCountry` | `schema:PostalAddress3`|
| _country_ | `schema:addressCountry` | `schema:PostalAddress1`|
| _country_clean_ | `schema:addressCountry` | `schema:PostalAddress2`|
| _currency_ | `schema:priceCurrency` | `schema:Offer1`|
| _dateCreated_ | `schema:dateCreated` | `schema:Role1`|
| _date_filed_ | `schema:startTime` | `memex:LegalAction1`|
| _datepublished_ | `schema:datePublished` | `schema:ScholarlyArticle1`|
| _datepublished_iso_ | `schema:datePublished` | `memex:Patent2`|
| _description_ | `schema:description` | `schema:Offer1`|
| _description_ | `schema:description` | `schema:Offer1`|
| _doc-uri_ | `uri` | `memex:Patent1`|
| _email_ | `schema:email` | `schema:Person2`|
| _expiryDate_ | `schema:availabilityEnds` | `schema:Offer1`|
| _filing_body_ | `schema:valueName` | `schema:Organization2`|
| _from_clean2_ | `schema:name` | `schema:Place1`|
| _industry_ | `schema:serviceType` | `schema:Service1`|
| _iso_date_posted_ | `schema:dateCreated` | `memex:Post1`|
| _iso_date_posted_2_ | `memex:dateRecorded` | `schema:OrganizationRole1`|
| _joined_iso_ | `schema:startDate` | `schema:OrganizationRole1`|
| _listedOnDate_ | `schema:availabilityStarts` | `schema:Offer1`|
| _location_ | `schema:name` | `schema:PostalAddress1`|
| _location_uri_ | `uri` | `schema:Place1`|
| _manufacturer_clean_ | `schema:name` | `schema:Organization2`|
| _manufacturer_uri_ | `uri` | `schema:Organization2`|
| _model_clean_ | `schema:mpn` | `schema:Product1`|
| _name_ | `schema:legalName` | `schema:Organization1`|
| _name_ | `schema:legalName` | `schema:Organization2`|
| _name_ | `schema:alternateName` | `schema:Organization1`|
| _offer-version_uri_ | `uri` | `schema:Offer2`|
| _org_role_uri_ | `uri` | `schema:OrganizationRole1`|
| _org_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _organization_uri_ | `uri` | `memex:PersonOrOrganization2`|
| _organization_uri_ | `uri` | `schema:Offer1`|
| _organization_uri_ | `uri` | `schema:Organization1`|
| _organizationuri_ | `uri` | `schema:Organization1`|
| _orgname_ | `schema:name` | `memex:PersonOrOrganization2`|
| _orgname_clean_ | `schema:name` | `memex:PersonOrOrganization1`|
| _other_organization_phone_clean_ | `schema:telephone` | `schema:Organization2`|
| _permit_uri_ | `uri` | `schema:GovernmentPermit1`|
| _personOrOrganization_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _phones_clean_ | `schema:telephone` | `schema:Organization1`|
| _place_name_ | `schema:name` | `schema:PostalAddress1`|
| _plaintiffs_clean_ | `schema:name` | `schema:Organization3`|
| _plaintiffs_clean_uri_ | `uri` | `schema:Organization3`|
| _post_id_ | `schema:name` | `memex:Identifier2`|
| _post_uri_ | `uri` | `memex:Post1`|
| _price_btc_currency_ | `schema:priceCurrency` | `schema:PriceSpecification2`|
| _price_clean_ | `schema:price` | `schema:PriceSpecification1`|
| _price_currency_ | `schema:priceCurrency` | `schema:PriceSpecification1`|
| _pricecurrency_ | `schema:priceCurrency` | `schema:Offer1`|
| _product_code_ | `schema:productID` | `schema:Product1`|
| _product_uri_ | `uri` | `schema:Product1`|
| _quantity_ | `schema:inventoryLevel` | `schema:Offer1`|
| _raw_text_ | `schema:text` | `memex:Thread1`|
| _raw_text_ | `schema:text` | `schema:Offer1`|
| _raw_text_ | `schema:text` | `schema:Offer1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `memex:Thread1`|
| _rawtextdetectedlanguage_ | `schema:inLanguage` | `schema:Offer1`|
| _reference_uri_ | `uri` | `schema:ScholarlyArticle2`|
| _role_uri_ | `uri` | `schema:Role1`|
| _serial_number_ | `schema:serialNumber` | `schema:Product1`|
| _ships_to_ | `schema:name` | `schema:PostalAddress2`|
| _ships_to_uri_ | `uri` | `schema:Place2`|
| _signature_clean_ | `schema:text` | `schema:WebPageElement1`|
| _state_ | `schema:addressRegion` | `schema:PostalAddress2`|
| _state_ | `schema:addressRegion` | `schema:PostalAddress3`|
| _state_ | `schema:addressRegion` | `schema:PostalAddress1`|
| _state_uri_ | `uri` | `schema:State1`|
| _street1_ | `schema:streetAddress` | `schema:PostalAddress2`|
| _street1_ | `schema:streetAddress` | `schema:PostalAddress1`|
| _t_firearms_ | `schema:name` | `memex:Topic2`|
| _t_gang_ | `schema:name` | `memex:DistinctivePhrases2`|
| _t_nfa_ | `schema:name` | `memex:Topic3`|
| _t_non_english_ | `schema:name` | `memex:DistinctivePhrases1`|
| _t_redflags_ | `schema:name` | `memex:Topic4`|
| _t_technology_ | `schema:name` | `memex:Topic1`|
| _text_ | `schema:description` | `schema:Offer2`|
| _title_ | `schema:name` | `schema:ScholarlyArticle1`|
| _title_ | `schema:name` | `memex:LegalAction1`|
| _title_ | `schema:title` | `schema:Offer1`|
| _title_ | `schema:jobTitle` | `schema:Person1`|
| _title_ | `schema:title` | `schema:Offer2`|
| _title_ | `schema:title` | `schema:Offer1`|
| _title_2_ | `schema:name` | `schema:Product1`|
| _title_plaintiff_ | `schema:name` | `schema:Organization4`|
| _title_plaintiff_uri_ | `uri` | `schema:Organization4`|
| _topic_id_ | `schema:name` | `memex:Identifier1`|
| _topic_title_ | `schema:text` | `schema:WebPageElement4`|
| _topic_title_ | `schema:text` | `schema:WebPageElement2`|
| _transactionType_ | `km-dev:columnSubClassOfLink` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|
| _uri_ | `uri` | `schema:Offer1`|
| _uri_ | `uri` | `memex:Thread1`|
| _uri_ | `uri` | `schema:Thing1`|
| _url_ | `schema:url` | `schema:Offer1`|
| _url_ | `schema:url` | `memex:LegalAction1`|
| _url_ | `schema:url` | `schema:Organization1`|
| _url_ | `schema:url` | `memex:Thread1`|
| _url_ | `schema:url` | `schema:Offer1`|
| _user_id_ | `schema:name` | `memex:Identifier3`|
| _user_uri_ | `uri` | `schema:Person1`|
| _username_ | `schema:name` | `schema:Person1`|
| _username_ | `schema:name` | `schema:ContactPoint1`|
| _username_ | `schema:name` | `schema:ContactPoint1`|
| _values_ | `schema:name` | `schema:Text3`|
| _values_ | `memex:hasPhrase` | `memex:Topic1`|
| _values_ | `memex:hasPhrase` | `memex:Topic2`|
| _values_ | `schema:name` | `schema:Text1`|
| _values_ | `schema:name` | `schema:Text4`|
| _values_ | `schema:name` | `schema:Text2`|
| _values_ | `schema:keywords` | `schema:ScholarlyArticle1`|
| _values_ | `schema:name` | `schema:Text6`|
| _values_ | `memex:hasPhrase` | `memex:DistinctivePhrases1`|
| _values_ | `schema:name` | `schema:Text5`|
| _values_ | `schema:alternateName` | `schema:Person1`|
| _values_ | `memex:hasPhrase` | `memex:DistinctivePhrases2`|
| _values_ | `memex:hasType` | `schema:Role1`|
| _year_published_ | `schema:datePublished` | `schema:ScholarlyArticle2`|
| _zipcode_ | `schema:postalCode` | `schema:PostalAddress2`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Offer1` | `schema:publisher` | `schema:Organization1`|
| `schema:Offer1` | `schema:itemOffered` | `schema:Product1`|
| `schema:Organization1` | `schema:name` | `xsd:velocityworks.net`|
| `schema:Product1` | `schema:image` | `schema:ImageObject1`|
| `schema:Product1` | `schema:offers` | `schema:Offer1`|
