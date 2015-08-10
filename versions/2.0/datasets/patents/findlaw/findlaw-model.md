## findlaw-sample.json

### PyTransforms
#### _organization_uri_
From column: _name_
>``` python
return uri_from_fields('organization/', getValue("name"))
```

#### _other_organization_uri_
From column: _other_offices / address / zipcode_
>``` python
return uri_from_fields('organization/', getValue("name"),getValue('city'), getValue('state'))
```

#### _other_organization_phone_clean_
From column: _other_offices / phone_
>``` python
return tenDigitPhoneNumber(getValue("phone"))
```

#### _phones_clean_
From column: _phones / values_
>``` python
return tenDigitPhoneNumber(getValue("values"))
```

#### _person_uri_
From column: _people / name_
>``` python
return attorney_uri(getValue('organization_uri'),getValue('name'))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _city_ | `schema:addressLocality` | `schema:PostalAddress2`|
| _city_ | `schema:addressLocality` | `schema:PostalAddress1`|
| _name_ | `schema:name` | `schema:Person1`|
| _name_ | `schema:legalName` | `schema:Organization1`|
| _name_ | `schema:legalName` | `schema:Organization2`|
| _organization_uri_ | `uri` | `schema:Organization1`|
| _other_organization_phone_clean_ | `schema:telephone` | `schema:Organization2`|
| _other_organization_uri_ | `uri` | `schema:Organization2`|
| _person_uri_ | `uri` | `schema:Person1`|
| _phones_clean_ | `schema:telephone` | `schema:Organization1`|
| _state_ | `schema:addressRegion` | `schema:PostalAddress2`|
| _state_ | `schema:addressRegion` | `schema:PostalAddress1`|
| _street1_ | `schema:streetAddress` | `schema:PostalAddress1`|
| _street1_ | `schema:streetAddress` | `schema:PostalAddress2`|
| _title_ | `schema:jobTitle` | `schema:Person1`|
| _values_ | `schema:url` | `schema:Organization1`|
| _zipcode_ | `schema:postalCode` | `schema:PostalAddress1`|
| _zipcode_ | `schema:postalCode` | `schema:PostalAddress2`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `schema:Organization1` | `schema:employee` | `schema:Person1`|
| `schema:Organization1` | `schema:location` | `schema:PostalAddress1`|
| `schema:Organization1` | `schema:subOrganization` | `schema:Organization2`|
| `schema:Organization2` | `schema:location` | `schema:PostalAddress2`|
| `schema:Person1` | `schema:worksFor` | `schema:Organization1`|
