## patent1-sample.xml

### PyTransforms
#### _date-publ-iso_
From column: _us-patent-grant / date-publ_
>``` python
return translate_date(getValue("date-publ"), '%Y%m%d', "%Y-%m-%d")
```

#### _creator_uri_
From column: _us-patent-grant / us-bibliographic-data-grant / us-parties / us-applicants / us-applicant / addressbook / address / city_
>``` python
return pt_creator_uri(getValue("first-name"), getValue("last-name"), getValue("city"), getValue("state"), getValue("country"))
```

#### _country_clean_
From column: _us-patent-grant / us-bibliographic-data-grant / us-parties / agents / agent / addressbook / address / country_
>``` python
return pt_agent_country(getValue("country"))
```

#### _orgname_clean_
From column: _us-patent-grant / us-bibliographic-data-grant / us-parties / agents / agent / addressbook / orgname_
>``` python
return orgname_clean(getValue("orgname"))
```

#### _patent_uri_
From column: _us-patent-grant / us-bibliographic-data-grant / publication-reference / document-id / doc-number_
>``` python
return pt_patent_uri(getValue('doc-number'))
```

#### _doc-uri_
From column: _us-patent-grant / us-bibliographic-data-grant / us-references-cited / us-citation / patcit / document-id / doc-number_
>``` python
return pt_patent_uri(getValue('doc-number'))
```

#### _full_name_
From column: _us-patent-grant / us-bibliographic-data-grant / us-parties / us-applicants / us-applicant / addressbook / last-name_
>``` python
return getValue("first-name") + " " + getValue("last-name")
```

#### _assignee_orgname_clean_
From column: _us-patent-grant / us-bibliographic-data-grant / assignees / assignee / addressbook / orgname_
>``` python
return orgname_clean(getValue("orgname"))
```

#### _assignee_org_uri_
From column: _us-patent-grant / us-bibliographic-data-grant / assignees / assignee / addressbook / orgname_
>``` python
return pt_organization_uri(getValue("orgname"))
```

#### _agent_uri_
From column: _us-patent-grant / us-bibliographic-data-grant / us-parties / agents / agent / addressbook / orgname_
>``` python
return pt_organization_uri(getValue("orgname"))
```

#### _assignee_address_uri_
From column: _us-patent-grant / us-bibliographic-data-grant / assignees / assignee / addressbook / address / city_
>``` python
return uri_from_fields('address/',getValue('city'),getValue('state'),getValue('country'))
```

#### _applicant_address_uri_
From column: _us-patent-grant / us-bibliographic-data-grant / us-parties / us-applicants / us-applicant / addressbook / address / city_
>``` python
return uri_from_fields('address/',getValue('city'),getValue('state'),getValue('country'))
```

#### _assignee_role_startdate_
From column: _us-patent-grant / us-bibliographic-data-grant / assignees / assignee / addressbook / orgname_
>``` python
if getValue("orgname"):
    return getValue('date-publ-iso')
else:
    return ''
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _agent_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _applicant_address_uri_ | `uri` | `schema:PostalAddress1`|
| _assignee_address_uri_ | `uri` | `schema:PostalAddress4`|
| _assignee_org_uri_ | `uri` | `memex:PersonOrOrganization2`|
| _assignee_orgname_clean_ | `schema:name` | `memex:PersonOrOrganization2`|
| _assignee_role_startdate_ | `schema:startDate` | `schema:Role1`|
| _city_ | `schema:addressLocality` | `schema:PostalAddress1`|
| _claim-text_ | `schema:text` | `schema:WebPageElement1`|
| _content_ | `schema:name` | `memex:Patent1`|
| _country_ | `schema:addressCountry` | `schema:PostalAddress1`|
| _creator_uri_ | `uri` | `schema:Person1`|
| _date-publ-iso_ | `schema:datePublished` | `memex:Patent1`|
| _doc-number_ | `schema:name` | `memex:Identifier2`|
| _doc-number_ | `schema:name` | `memex:Identifier1`|
| _doc-uri_ | `uri` | `memex:Patent2`|
| _full_name_ | `schema:name` | `schema:Person1`|
| _orgname_clean_ | `schema:name` | `memex:PersonOrOrganization1`|
| _patent_uri_ | `uri` | `memex:Patent1`|
| _state_ | `schema:addressRegion` | `schema:PostalAddress1`|
| _state_ | `schema:addressRegion` | `schema:PostalAddress4`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Identifier1` | `memex:hasType` | `xsd:thesaurus/identifier/patentid`|
| `memex:Identifier2` | `memex:hasType` | `xsd:thesaurus/identifier/patentid`|
| `memex:Patent1` | `memex:applicant` | `schema:Person1`|
| `memex:Patent1` | `memex:assignee` | `schema:Role1`|
| `memex:Patent1` | `memex:hasClaimPart` | `schema:WebPageElement1`|
| `memex:Patent1` | `memex:identifier` | `memex:Identifier1`|
| `memex:Patent1` | `schema:agent` | `memex:PersonOrOrganization1`|
| `memex:Patent1` | `schema:citation` | `memex:Patent2`|
| `memex:Patent2` | `memex:identifier` | `memex:Identifier2`|
| `memex:PersonOrOrganization2` | `schema:address` | `schema:PostalAddress4`|
| `schema:Person1` | `schema:address` | `schema:PostalAddress1`|
| `schema:Role1` | `memex:assignee` | `memex:PersonOrOrganization2`|
