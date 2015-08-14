## patent1-sample.xml

### PyTransforms
#### _date-publ-iso_
From column: _PATDOC / SDOBI / B100 / B140 / DATE / PDAT_
>``` python
return translate_date(getValue("PDAT"), '%Y%m%d', "%Y-%m-%d")
```

#### _patent_uri_
From column: _PATDOC / SDOBI / B100 / B110 / DNUM / PDAT_
>``` python
return pt_patent_uri(getValue('PDAT'))
```

#### _doc-uri_
From column: _PATDOC / SDOBI / B500 / B560 / B561 / PCIT / DOC / DNUM / PDAT_
>``` python
return pt_patent_uri(getValue('PDAT'))
```

#### _ignore1_
From column: _PATDOC / SDOBI / B700 / B720 / B721 / PARTY-US / ADR / STR / PDAT_
>``` python
return getValue("PDAT") + ": " + getValueFromNestedColumnByIndex("ADR", "STATE/PDAT", 0)
```

#### _applicant_address_uri_
From column: _PATDOC / SDOBI / B700 / B720 / B721 / PARTY-US / ADR / CITY / PDAT_
>``` python
return uri_from_fields('address/', getValue("PDAT"), getValueFromNestedColumnByIndex("ADR", "STATE/PDAT", 0), getValueFromNestedColumnByIndex("ADR", "CTRY/PDAT", 0) or "US")
```

#### _full_name_
From column: _PATDOC / SDOBI / B700 / B720 / B721 / PARTY-US / NAM / FNM / PDAT_
>``` python
return getValue("PDAT") + " " + getValueFromNestedColumnByIndex("NAM", "SNM/STEXT/PDAT", 0)
```

#### _creator_uri_
From column: _PATDOC / SDOBI / B700 / B720 / B721 / PARTY-US / NAM / FNM / full_name_
>``` python
return pt_creator_uri(getValue("PDAT"), getValueFromNestedColumnByIndex("NAM", "SNM/STEXT/PDAT", 0), getValueFromNestedColumnByIndex("PARTY-US", "ADR/CITY/PDAT", 0), getValueFromNestedColumnByIndex("PARTY-US", "ADR/STATE/PDAT", 0), getValueFromNestedColumnByIndex("PARTY-US", "ADR/CTRY/PDAT", 0) or "us")
```

#### _agent_name_
From column: _PATDOC / SDOBI / B700 / B740 / B741 / PARTY-US / NAM / FNM / PDAT_
>``` python
return getValue("PDAT") + " " + getValueFromNestedColumnByIndex("NAM", "SNM/STEXT/PDAT", 0)
```

#### _agent_object_type_
From column: _PATDOC / SDOBI / B700 / B740 / B741 / PARTY-US / NAM_
>``` python
orgName = getValueFromNestedColumnByIndex("PARTY-US", "NAM/ONM/STEXT/PDAT", 0)
return "organization" if orgName else "person"
```

#### _agent_uri_
From column: _PATDOC / SDOBI / B700 / B740 / B741 / PARTY-US / agent_object_type_
>``` python
if getValue("agent_object_type")=='organization':
    return pt_organization_uri(getValueFromNestedColumnByIndex('PARTY-US', 'NAM/ONM/STEXT/PDAT', 0))
else:
    return pt_creator_uri(getValueFromNestedColumnByIndex("PARTY-US", "NAM/FNM/PDAT", 0), 
                          getValueFromNestedColumnByIndex("PARTY-US", "NAM/SNM/STEXT/PDAT", 0), 
                          getValueFromNestedColumnByIndex("PARTY-US", "ADR/CITY/PDAT", 0), 
                          getValueFromNestedColumnByIndex("PARTY-US", "ADR/STATE/PDAT", 0), 
                          getValueFromNestedColumnByIndex("PARTY-US", "ADR/CTRY/PDAT", 0))
```

#### _applicant_country_name_
From column: _PATDOC / SDOBI / B700 / B720 / B721 / PARTY-US / ADR_
>``` python
ctryName = getValueFromNestedColumnByIndex("PARTY-US", "ADR/CTRY/PDAT", 0)
return ctryName or "us"
```

#### _assignee_country_name_
From column: _PATDOC / SDOBI / B700 / B730 / B731 / PARTY-US / ADR_
>``` python
ctryName = getValueFromNestedColumnByIndex("PARTY-US", "ADR/CTRY/PDAT", 0)
return ctryName or "us"
```

#### _assignee_name_
From column: _PATDOC / SDOBI / B700 / B730 / B731 / PARTY-US / NAM / FNM / PDAT_
>``` python
return getValue("PDAT") + " " + getValueFromNestedColumnByIndex("NAM", "SNM/STEXT/PDAT", 0)
```

#### _assignee_object_type_
From column: _PATDOC / SDOBI / B700 / B730 / B731 / PARTY-US / NAM_
>``` python
orgName = getValueFromNestedColumnByIndex("PARTY-US", "NAM/ONM/STEXT/PDAT", 0)
return "organization" if orgName else "person"
```

#### _assignee_uri_
From column: _PATDOC / SDOBI / B700 / B730 / B731 / PARTY-US / assignee_object_type_
>``` python
if getValue("assignee_object_type")=='organization':
    return pt_organization_uri(getValueFromNestedColumnByIndex('PARTY-US', 'NAM/ONM/STEXT/PDAT', 0))
else:
    return pt_creator_uri(getValueFromNestedColumnByIndex("PARTY-US", "NAM/FNM/PDAT", 0), 
                          getValueFromNestedColumnByIndex("PARTY-US", "NAM/SNM/STEXT/PDAT", 0), 
                          getValueFromNestedColumnByIndex("PARTY-US", "ADR/CITY/PDAT", 0), 
                          getValueFromNestedColumnByIndex("PARTY-US", "ADR/STATE/PDAT", 0), 
                          getValueFromNestedColumnByIndex("PARTY-US", "ADR/CTRY/PDAT", 0) or "us")
```

#### _assignee_role_startdate_
From column: _PATDOC / SDOBI / B700 / B730 / B731 / PARTY-US / assignee_uri_
>``` python
if getValue('assignee_object_type')=='organization':
    return getValueFromNestedColumnByIndex('SDOBI', 'B100/B140/DATE/date-publ-iso', 0)
else:
    return ''
```

#### _assignee_address_uri_
From column: _PATDOC / SDOBI / B700 / B730 / B731 / PARTY-US / ADR / CITY / PDAT_
>``` python
return uri_from_fields('address/', getValue("PDAT"), getValueFromNestedColumnByIndex("ADR", "STATE/PDAT", 0), getValueFromNestedColumnByIndex("ADR", "CTRY/PDAT", 0) or "US")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _PDAT_ | `schema:name` | `memex:Identifier1`|
| _PDAT_ | `schema:addressRegion` | `schema:PostalAddress1`|
| _PDAT_ | `schema:addressLocality` | `schema:PostalAddress2`|
| _PDAT_ | `schema:addressRegion` | `schema:PostalAddress2`|
| _PDAT_ | `schema:name` | `memex:Patent1`|
| _PDAT_ | `schema:addressLocality` | `schema:PostalAddress1`|
| _PDAT_ | `schema:name` | `memex:Identifier2`|
| _agent_name_ | `schema:name` | `memex:PersonOrOrganization1`|
| _agent_uri_ | `uri` | `memex:PersonOrOrganization1`|
| _applicant_address_uri_ | `uri` | `schema:PostalAddress1`|
| _applicant_country_name_ | `schema:addressCountry` | `schema:PostalAddress1`|
| _assignee_address_uri_ | `uri` | `schema:PostalAddress2`|
| _assignee_country_name_ | `schema:addressCountry` | `schema:PostalAddress2`|
| _assignee_name_ | `schema:name` | `memex:PersonOrOrganization2`|
| _assignee_role_startdate_ | `schema:startDate` | `schema:Role1`|
| _assignee_uri_ | `uri` | `memex:PersonOrOrganization2`|
| _creator_uri_ | `uri` | `schema:Person1`|
| _date-publ-iso_ | `schema:datePublished` | `memex:Patent1`|
| _doc-uri_ | `uri` | `memex:Patent2`|
| _full_name_ | `schema:name` | `schema:Person1`|
| _patent_uri_ | `uri` | `memex:Patent1`|
| _values_ | `schema:text` | `schema:WebPageElement1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Identifier1` | `memex:hasType` | `xsd:thesaurus/identifier/patentid`|
| `memex:Identifier2` | `memex:hasType` | `xsd:thesaurus/identifier/patentid`|
| `memex:Patent1` | `memex:assignee` | `schema:Role1`|
| `memex:Patent1` | `memex:hasClaimPart` | `schema:WebPageElement1`|
| `memex:Patent1` | `memex:identifier` | `memex:Identifier1`|
| `memex:Patent1` | `schema:agent` | `memex:PersonOrOrganization1`|
| `memex:Patent1` | `schema:citation` | `memex:Patent2`|
| `memex:Patent2` | `memex:identifier` | `memex:Identifier2`|
| `memex:PersonOrOrganization2` | `schema:address` | `schema:PostalAddress2`|
| `schema:Person1` | `schema:address` | `schema:PostalAddress1`|
| `schema:Role1` | `memex:assignee` | `memex:PersonOrOrganization2`|
