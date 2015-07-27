## weapons-wordlists-sample.json

### PyTransforms

### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _t_firearms_ | `schema:name` | `memex:Topic2`|
| _t_gang_ | `schema:name` | `memex:DistinctivePhrases1`|
| _t_nfa_ | `schema:name` | `memex:Topic3`|
| _t_non_english_ | `schema:name` | `memex:DistinctivePhrases2`|
| _t_technology_ | `schema:name` | `memex:Topic1`|
| _uri_ | `uri` | `schema:Thing1`|
| _values_ | `schema:name` | `schema:Text1`|
| _values_ | `schema:name` | `schema:Text2`|
| _values_ | `schema:name` | `schema:Text4`|
| _values_ | `schema:name` | `schema:Text3`|
| _values_ | `schema:name` | `schema:Text5`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:DistinctivePhrases1` | `memex:hasPhrase` | `schema:Text2`|
| `memex:DistinctivePhrases2` | `memex:hasPhrase` | `schema:Text5`|
| `memex:Topic1` | `memex:hasPhrase` | `schema:Text1`|
| `memex:Topic2` | `memex:hasPhrase` | `schema:Text3`|
| `memex:Topic3` | `memex:hasPhrase` | `schema:Text4`|
| `schema:Thing1` | `memex:distinctivePhrases` | `memex:DistinctivePhrases1`|
| `schema:Thing1` | `memex:distinctivePhrases` | `memex:DistinctivePhrases2`|
| `schema:Thing1` | `schema:about` | `memex:Topic1`|
| `schema:Thing1` | `schema:about` | `memex:Topic2`|
| `schema:Thing1` | `schema:about` | `memex:Topic3`|
