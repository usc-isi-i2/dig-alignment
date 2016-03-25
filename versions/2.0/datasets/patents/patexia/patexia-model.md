## patexia_sample_41.json

### PyTransforms
#### _title_plaintiff_
From column: _title_
>``` python
return plaintiff_from_title(getValue("title"))
```

#### _title_defendant_
From column: _title_
>``` python
return defendant_from_title(getValue("title"))
```

#### _date_filed_
From column: _filing_date_
>``` python
return translate_date(getValue("filing_date"), '%b %d, %Y', "%Y-%m-%d")
```

#### _plaintiffs_clean_
From column: _plantiffs / values_
>``` python
return orgname_clean(getValue("values"))
```

#### _defendants_clean_
From column: _defendants / values_
>``` python
return orgname_clean(getValue("values"))
```

#### _title_defendant_uri_
From column: _title_defendant_
>``` python
return pt_organization_uri(getValue("title_defendant"))
```

#### _title_plaintiff_uri_
From column: _title_plaintiff_
>``` python
return pt_organization_uri(getValue("title_plaintiff"))
```

#### _plaintiffs_clean_uri_
From column: _plantiffs / values_
>``` python
return pt_organization_uri(getValue("plaintiffs_clean"))
```

#### _defendants_clean_uri_
From column: _defendants / values_
>``` python
return pt_organization_uri(getValue("defendants_clean"))
```

#### _patent_uri_
From column: _related_patents / doc_no_
>``` python
return pt_patent_uri(getValue('doc_no'))
```

#### _cause_clean_
From column: _causes / values_
>``` python
return clean_legal_action_cause(getValue("values"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _case_number_ | `schema:name` | `memex:Identifier1`|
| _cause_clean_ | `schema:name` | `memex:LegalActionCause1`|
| _court_ | `schema:name` | `schema:Place1`|
| _date_filed_ | `schema:startTime` | `memex:LegalAction1`|
| _defendants_clean_ | `schema:name` | `schema:Organization4`|
| _defendants_clean_uri_ | `uri` | `schema:Organization4`|
| _patent_uri_ | `uri` | `memex:Patent1`|
| _plaintiffs_clean_ | `schema:name` | `schema:Organization3`|
| _plaintiffs_clean_uri_ | `uri` | `schema:Organization3`|
| _title_ | `schema:name` | `memex:LegalAction1`|
| _title_defendant_ | `schema:name` | `schema:Organization1`|
| _title_defendant_uri_ | `uri` | `schema:Organization1`|
| _title_plaintiff_ | `schema:name` | `schema:Organization2`|
| _title_plaintiff_uri_ | `uri` | `schema:Organization2`|
| _url_ | `schema:url` | `memex:LegalAction1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:Identifier1` | `memex:hasType` | `xsd:http://dig.isi.edu/patents/data/thesaurus/identifier/docketnumber`|
| `memex:LegalAction1` | `memex:defendant` | `schema:Organization1`|
| `memex:LegalAction1` | `memex:defendant` | `schema:Organization4`|
| `memex:LegalAction1` | `memex:identifier` | `memex:Identifier1`|
| `memex:LegalAction1` | `memex:plaintiff` | `schema:Organization2`|
| `memex:LegalAction1` | `memex:plaintiff` | `schema:Organization3`|
| `memex:LegalAction1` | `schema:cause` | `memex:LegalActionCause1`|
| `memex:LegalAction1` | `schema:location` | `schema:Place1`|
| `memex:Patent1` | `memex:legalAction` | `memex:LegalAction1`|
