
########################################################
#			Images
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/dipsy/github/dig-alignment/datasets/istr/images/import.sql --modelfilepath /Users/dipsy/github/dig-alignment/datasets/istr/images/ist-images-model.ttl --jsonoutputfile /Users/dipsy/github/dig-alignment/datasets/istr/images/ist-images-jsonld.json --contextfile /Users/dipsy/github/dig-alignment/datasets/istr/images/ist-images-context.json --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/images/ist-images-rdf.n3" -Dexec.classpathScope=compile


########################################################
#			Ads
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/import.sql --modelfilepath /Users/dipsy/github/dig-alignment/datasets/istr/ads/ads-model.ttl --jsonoutputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/ads-jsonld.json --contextfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/ads-context.json --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/ads-rdf.n3" -Dexec.classpathScope=compile



########################################################
#			Ads-Attributes
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/dipsy/github/dig-alignment/datasets/istr/ads-attributes/import.sql --modelfilepath /Users/dipsy/github/dig-alignment/datasets/istr/ads-attributes/ads-attributes-features-model.ttl --jsonoutputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads-attributes/ads-attributes-features-jsonld.json --contextfile /Users/dipsy/github/dig-alignment/datasets/istr/ads-attributes/ads-attributes-features-context.json --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads-attributes/ads-attributes-features-rdf.n3" -Dexec.classpathScope=compile


########################################################
#			Stanford Extractions
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/dipsy/github/dig-alignment/datasets/istr/stanford-extractions/import.sql --modelfilepath /Users/dipsy/github/dig-alignment/datasets/istr/stanford-extractions/stanford-features-model.ttl --jsonoutputfile /Users/dipsy/github/dig-alignment/datasets/istr/stanford-extractions/stanford-features-jsonld.json --contextfile /Users/dipsy/github/dig-alignment/datasets/istr/stanford-extractions/stanford-features-context.json --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/stanford-extractions/stanford-features-rdf.n3" -Dexec.classpathScope=compile
