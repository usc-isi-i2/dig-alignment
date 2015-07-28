## google-sample-clean.xml

### PyTransforms
#### _full-name_
From column: _us-patent-grant / us-bibliographic-data-grant / applicants / applicant / addressbook / first-name_
>``` python
return getValue("first-name") + " " + getValue("last-name")
```

#### _Patent-id_
From column: _us-patent-grant / us-bibliographic-data-grant / document-id / Patent-id_
>``` python
return pt_patent_uri(getValue("Patent-id"))
```

#### _doc-uri_
From column: _us-patent-grant / us-bibliographic-data-grant / references-cited / citation / document-id / doc-number_
>``` python
return pt_patent_uri(getValue('doc-number'))
```

#### _datepublished_iso_
From column: _us-patent-grant / date-publ_
>``` python
return translate_date(getValue("date-publ"), '%Y%m%d', "%Y-%m-%d")
```

#### _creator_uri_
From column: _us-patent-grant / us-bibliographic-data-grant / applicants / applicant / addressbook / address / city_
>``` python
return pt_creator_uri(getValue("first-name"), getValue("last-name"), getValue("city"), getValue("state"), getValue("country"))
```

#### _organization_uri_
From column: _us-patent-grant / us-bibliographic-data-grant / assignees / assignee / addressbook / orgname_
>``` python
return pt_organization_uri(getValue("orgname"))
```

#### _country_clean_
From column: _us-patent-grant / us-bibliographic-data-grant / agents / agent / addressbook / address / country_
>``` python
return pt_agent_country(getValue("country"))
```

#### _orgname_clean_
From column: _us-patent-grant / us-bibliographic-data-grant / agents / agent / addressbook / orgname_
>``` python
return orgname_clean(getValue("orgname"))
```

#### _date-produced_
From column: _us-patent-grant / date-produced_
>``` python
return translate_date(getValue("date-produced"), '%Y%m%d', "%Y-%m-%d")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Patent-id_ | `uri` | `memex:Patent1`|
| _city_ | `schema:addressLocality` | `schema:PostalAddress1`|
| _city_ | `schema:addressLocality` | `schema:PostalAddress2`|
| _claim-text_ | `schema:text` | `schema:WebPageElement2`|
| _content_ | `schema:name` | `memex:Patent1`|
| _country_ | `schema:addressCountry` | `schema:PostalAddress1`|
| _country_ | `schema:addressCountry` | `schema:PostalAddress2`|
| _country_clean_ | `schema:addressCountry` | `schema:PostalAddress3`|
| _creator_uri_ | `uri` | `schema:Person1`|
| _datepublished_iso_ | `schema:datePublished` | `memex:Patent1`|
| _doc-number_ | `schema:name` | `memex:Identifier1`|
| _doc-uri_ | `uri` | `memex:Patent2`|
| _full-name_ | `schema:name` | `schema:Person1`|
| _organization_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _orgname_ | `schema:name` | `memex:PersonOrOrganization1`|
| _orgname_clean_ | `schema:name` | `memex:PersonOrOrganization2`|
| _state_ | `schema:addressRegion` | `schema:PostalAddress1`|
| _state_ | `schema:addressRegion` | `schema:PostalAddress2`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Identifier1` | `memex:hasType` | `xsd:/thesaurus/identifier/patentid`|
| `memex:Patent1` | `memex:hasClaimPart` | `schema:WebPageElement2`|
| `memex:Patent1` | `memex:identifier` | `memex:Identifier1`|
| `memex:Patent1` | `schema:agent` | `memex:PersonOrOrganization2`|
| `memex:Patent1` | `schema:citation` | `memex:Patent2`|
| `memex:Patent1` | `schema:creator` | `schema:Person1`|
| `memex:Patent1` | `schema:sourceOrganization` | `memex:PersonOrOrganization1`|
| `memex:PersonOrOrganization1` | `schema:address` | `schema:PostalAddress2`|
| `memex:PersonOrOrganization2` | `schema:address` | `schema:PostalAddress3`|
| `schema:Person1` | `schema:address` | `schema:PostalAddress1`|
