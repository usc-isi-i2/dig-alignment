
########################################################
#			Images
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/szekely/github/dig-alignment/datasets/istr/images/import.sql --modelfilepath /Users/szekely/github/dig-alignment/datasets/istr/images/ist-images-model.ttl --jsonoutputfile /Users/szekely/github/dig-alignment/datasets/istr/images/x-ist-images-jsonld.json --contextfile /Users/szekely/github/dig-alignment/datasets/istr/context-for-istr-datasets.json --outputfile /Users/szekely/github/dig-alignment/datasets/istr/images/x-ist-images-rdf.n3" -Dexec.classpathScope=compile


########################################################
#			Ads
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/szekely/github/dig-alignment/datasets/istr/ads/import.sql --modelfilepath /Users/szekely/github/dig-alignment/datasets/istr/ads/ads-model.ttl --jsonoutputfile /Users/szekely/github/dig-alignment/datasets/istr/ads/x-ads-jsonld.json --contextfile /Users/szekely/github/dig-alignment/datasets/istr/context-for-istr-datasets.json --outputfile /Users/szekely/github/dig-alignment/datasets/istr/ads/x-ads-rdf.n3" -Dexec.classpathScope=compile



########################################################
#			Ads-Attributes
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/szekely/github/dig-alignment/datasets/istr/ads-attributes/import.sql --modelfilepath /Users/szekely/github/dig-alignment/datasets/istr/ads-attributes/ads-attributes-features-model.ttl --jsonoutputfile /Users/szekely/github/dig-alignment/datasets/istr/ads-attributes/x-ads-attributes-features-jsonld.json --contextfile /Users/szekely/github/dig-alignment/datasets/istr/context-for-istr-datasets.json --outputfile /Users/szekely/github/dig-alignment/datasets/istr/ads-attributes/x-ads-attributes-features-rdf.n3" -Dexec.classpathScope=compile


########################################################
#			Stanford Extractions
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/szekely/github/dig-alignment/datasets/istr/stanford-extractions/import.sql --modelfilepath /Users/szekely/github/dig-alignment/datasets/istr/stanford-extractions/stanford-features-model.ttl --jsonoutputfile /Users/szekely/github/dig-alignment/datasets/istr/stanford-extractions/x-stanford-features-jsonld.json --contextfile /Users/szekely/github/dig-alignment/datasets/istr/context-for-istr-datasets.json --outputfile /Users/szekely/github/dig-alignment/datasets/istr/stanford-extractions/x-stanford-features-rdf.n3" -Dexec.classpathScope=compile
