## weapons-wordlists-sample.json

### PyTransforms

### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _t_firearms_ | `schema:name` | `memex:Topic2`|
| _t_gang_ | `schema:name` | `memex:DistinctivePhrases1`|
| _t_nfa_ | `schema:name` | `memex:Topic3`|
| _t_non_english_ | `schema:name` | `memex:DistinctivePhrases2`|
| _t_redflags_ | `schema:name` | `memex:Topic4`|
| _t_technology_ | `schema:name` | `memex:Topic1`|
| _uri_ | `uri` | `schema:Thing1`|
| _values_ | `schema:name` | `schema:Text1`|
| _values_ | `schema:name` | `schema:Text6`|
| _values_ | `schema:name` | `schema:Text3`|
| _values_ | `schema:name` | `schema:Text2`|
| _values_ | `schema:name` | `schema:Text5`|
| _values_ | `schema:name` | `schema:Text4`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `memex:DistinctivePhrases1` | `memex:hasPhrase` | `schema:Text2`|
| `memex:DistinctivePhrases2` | `memex:hasPhrase` | `schema:Text5`|
| `memex:Topic1` | `memex:hasPhrase` | `schema:Text1`|
| `memex:Topic2` | `memex:hasPhrase` | `schema:Text3`|
| `memex:Topic3` | `memex:hasPhrase` | `schema:Text4`|
| `memex:Topic4` | `memex:hasPhrase` | `schema:Text6`|
| `schema:Thing1` | `memex:hasFirearmsPhrase` | `memex:Topic2`|
| `schema:Thing1` | `memex:hasFirearmsRedFlagPhrase` | `memex:Topic4`|
| `schema:Thing1` | `memex:hasGangPhrase` | `memex:DistinctivePhrases1`|
| `schema:Thing1` | `memex:hasNFAPhrase` | `memex:Topic3`|
| `schema:Thing1` | `memex:hasNonEnglishPhrase` | `memex:DistinctivePhrases2`|
| `schema:Thing1` | `memex:hasTechnologyPhrase` | `memex:Topic1`|
