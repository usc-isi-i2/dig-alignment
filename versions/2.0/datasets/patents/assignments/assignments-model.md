## ad20150727-assignments-sample.xml

### PyTransforms
#### _patent_uri_
From column: _us-patent-assignments / patent-assignments / patent-assignment / patent-properties / patent-property / Unfold: kind / Glue_1 / Values_2_
>``` python
return pt_patent_uri(getValue("b1_or_b2"))
```

#### _b1_or_b2_
From column: _us-patent-assignments / patent-assignments / patent-assignment / patent-properties / patent-property / Unfold: kind / Glue_1 / Values_3_
>``` python
return first_non_null(getValue("Values_2"),getValue("Values"),getValue("Values_1"))
```

#### _dummy_
From column: _us-patent-assignments / patent-assignments / patent-assignment / dummy_
>``` python
return getValueFromNestedColumnByIndex('patent-assignors', 'patent-assignor/execution-date/date', 0)
```

#### _execution_date_clean_
From column: _us-patent-assignments / patent-assignments / patent-assignment / dummy_
>``` python
return translate_date(getValue("dummy"), '%Y%m%d', "%Y-%m-%d")
```

#### _org_uri_
From column: _us-patent-assignments / patent-assignments / patent-assignment / patent-assignees / patent-assignee / name_
>``` python
return pt_organization_uri(getValue("name"))
```

#### _name_clean_
From column: _us-patent-assignments / patent-assignments / patent-assignment / patent-assignees / patent-assignee / name_
>``` python
return orgname_clean(getValue("name"))
```

#### _postal_address_uri_
From column: _us-patent-assignments / patent-assignments / patent-assignment / patent-assignees / patent-assignee / address-2_
>``` python
return uri_from_fields("address/",getValue("address-2"),getValue("address-1"),getValue("city"),getValue("state"),getValue("postcode"),getValue("country"))
```

#### _patent_identifier_
From column: _us-patent-assignments / patent-assignments / patent-assignment / patent-properties / patent-property / Unfold: kind / x0 / Values_
>``` python
a1=getValueFromNestedColumnByIndex("Unfold: kind", "a1/Values", 0)
b1=getValueFromNestedColumnByIndex("Unfold: kind", "b1/Values", 0)
b2=getValueFromNestedColumnByIndex("Unfold: kind", "b2/Values", 0)
return first_non_null(b2,b1,a1)
```

#### _patent_uri_2_
From column: _us-patent-assignments / patent-assignments / patent-assignment / patent-properties / patent-property / Unfold: kind / x0 / patent_identifier_
>``` python
return pt_patent_uri(getValue("patent_identifier"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `schema:name` | `memex:Identifier3`|
| _Values_ | `schema:name` | `memex:Identifier2`|
| _Values_ | `schema:name` | `memex:Identifier1`|
| _address-1_ | `schema:streetAddress` | `schema:PostalAddress1`|
| _city_ | `schema:addressLocality` | `schema:PostalAddress1`|
| _country-name_ | `schema:addressCountry` | `schema:PostalAddress1`|
| _execution_date_clean_ | `schema:startDate` | `schema:Role1`|
| _name_clean_ | `schema:name` | `memex:PersonOrOrganization1`|
| _org_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _patent_uri_2_ | `uri` | `memex:Patent1`|
| _postal_address_uri_ | `uri` | `schema:PostalAddress1`|
| _postcode_ | `schema:postalCode` | `schema:PostalAddress1`|
| _state_ | `schema:addressRegion` | `schema:PostalAddress1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Identifier1` | `memex:hasType` | `xsd:thesaurus/identifier/patentid`|
| `memex:Identifier2` | `memex:hasType` | `xsd:thesaurus/identifier/patentid`|
| `memex:Identifier3` | `memex:hasType` | `xsd:thesaurus/identifier/patentid`|
| `memex:Patent1` | `memex:assignee` | `schema:Role1`|
| `memex:Patent1` | `memex:identifier` | `memex:Identifier1`|
| `memex:Patent1` | `memex:identifier` | `memex:Identifier2`|
| `memex:Patent1` | `memex:identifier` | `memex:Identifier3`|
| `memex:PersonOrOrganization1` | `schema:address` | `schema:PostalAddress1`|
| `schema:Role1` | `memex:assignee` | `memex:PersonOrOrganization1`|
