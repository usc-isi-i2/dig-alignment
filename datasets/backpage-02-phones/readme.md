## Phone Extractions

Andrew extracts phone numbers from the title and body part.


### PyTransforms
#### _documentUri_
From column: _url_
>``` python
return documentUrl(getValue("url"))
```

#### _titleUri_
From column: _titleText / role_
>``` python
return getValue("url")+"/title"
```

#### _bodyUri_
From column: _bodyText / role_
>``` python
return getValue("url")+"/body"
```

#### _phoneUri_
From column: _bodyText / phoneNumbers / values_
>``` python
return "phonenumber/"+getValue("values")
```

#### _phoneTitleUri_
From column: _titleText / phoneNumbers / values_
>``` python
return "phonenumber/"+getValue("values")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _bodyUri_ | `uri` | `schema:WebPageElement2`|
| _documentUri_ | `uri` | `dig:URLEntity1`|
| _phoneTitleUri_ | `uri` | `dig:PhoneNumber2`|
| _phoneUri_ | `uri` | `dig:PhoneNumber1`|
| _titleUri_ | `uri` | `schema:WebPageElement1`|
| _values_ | `dig:tenDigitPhoneNumber` | `dig:PhoneNumber1`|
| _values_ | `dig:tenDigitPhoneNumber` | `dig:PhoneNumber2`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `dig:URLEntity1` | `dig:snapshot` | `schema:WebPageElement1`|
| `dig:URLEntity1` | `dig:snapshot` | `schema:WebPageElement2`|
| `schema:WebPageElement1` | `dig:mentionsPhoneNumber` | `dig:PhoneNumber1`|
| `schema:WebPageElement1` | `dig:mentionsPhoneNumber` | `dig:PhoneNumber2`|