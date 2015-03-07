select distinct(mid(url,8,locate('.',url)-8)) as backpage_sitekey from ads where sources_id=1 limit 739
