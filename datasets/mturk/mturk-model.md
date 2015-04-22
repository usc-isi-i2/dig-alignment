## mturk-sample.tsv

### PyTransforms
#### _HitUri_
From column: _HitId_
>``` python
return "hit/" + getValue("HitId")
```

#### _WorkerUri_
From column: _WorkerId_
>``` python
return "Worker/" + getValue("WorkerId")
```

#### _AssignmentUri_
From column: _DocumentUri_
>``` python
return getValue("DocumentUri") + "/" + getValue("AssignmentId") + "/" + getValue("Offset") + "/" + ("0" if getValue("Offset")=="0" else str(len(getValue("Value"))))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AssignmentUri_ | `uri` | `mturk:Annotation1`|
| _DocumentUri_ | `uri` | `schema:CreativeWork1`|
| _HitUri_ | `uri` | `schema:AssessAction1`|
| _Label_ | `mturk:annotationLabel` | `mturk:Annotation1`|
| _Offset_ | `mturk:annotationOffset` | `mturk:Annotation1`|
| _Value_ | `mturk:annotationValue` | `mturk:Annotation1`|
| _WorkerUri_ | `uri` | `schema:Person1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `mturk:Annotation1` | `prov:wasDerivedFrom` | `schema:CreativeWork1`|
| `schema:AssessAction1` | `schema:agent` | `schema:Person1`|
| `schema:AssessAction1` | `schema:result` | `mturk:Annotation1`|
| `schema:AssessAction1` | `schema:object` | `schema:CreativeWork1`|
