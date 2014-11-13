select unix_timestamp(a.importtime)*1000 as timestamp, concat(t.title, "") as clean_title, concat(b.body, "") as clean_body, a.* from ads a join deobf_title t on a.id=t.id join deobf_body on a.id=b.id

