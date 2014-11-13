
########################################################
#			Images
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/dipsy/github/dig-alignment/datasets/istr/images/import.sql --modelfilepath /Users/dipsy/github/dig-alignment/datasets/istr/images/ist-images-model.ttl --jsonoutputfile /Users/dipsy/github/dig-alignment/datasets/istr/images/x-ist-images-jsonld.json --contextfile /Users/dipsy/github/dig-alignment/datasets/istr/context-for-istr-datasets.json --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/images/x-ist-images-rdf.n3" -Dexec.classpathScope=compile


########################################################
#			Ads
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/import.sql --modelfilepath /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-main/ads-main-model.ttl --jsonoutputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-main/ads-main-jsonld.json --contextfile /Users/dipsy/github/dig-alignment/datasets/istr/context-for-istr-datasets.json --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-main/ads-main-rdf.n3" -Dexec.classpathScope=compile

#Ads phone
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/import.sql --modelfilepath /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-phone/ads-phonenumber-model.ttl --jsonoutputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-phone/ads-phonenumber-jsonld.json --contextfile /Users/dipsy/github/dig-alignment/datasets/istr/context-for-istr-datasets.json --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-address/ads-phonenumber-rdf.n3" -Dexec.classpathScope=compile

#Ads address
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/import.sql --modelfilepath /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-address/ads-address-model.ttl --jsonoutputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-address/ads-address-jsonld.json --contextfile /Users/dipsy/github/dig-alignment/datasets/istr/context-for-istr-datasets.json --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-address/ads-address-rdf.n3" -Dexec.classpathScope=compile

#Ads age
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/import.sql --modelfilepath /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-age/ads-age-model.ttl --jsonoutputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-age/ads-age-jsonld.json --contextfile /Users/dipsy/github/dig-alignment/datasets/istr/context-for-istr-datasets.json --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-age/ads-age-rdf.n3" -Dexec.classpathScope=compile

#Ads website
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/import.sql --modelfilepath /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-website/ads-website-model.ttl --jsonoutputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-website/ads-website-jsonld.json --contextfile /Users/dipsy/github/dig-alignment/datasets/istr/context-for-istr-datasets.json --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-website/ads-website-rdf.n3" -Dexec.classpathScope=compile

#Ads gender
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/import.sql --modelfilepath /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-gender/ads-gender-model.ttl --jsonoutputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-gender/ads-gender-jsonld.json --contextfile /Users/dipsy/github/dig-alignment/datasets/istr/context-for-istr-datasets.json --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-gender/ads-gender-rdf.n3" -Dexec.classpathScope=compile

#Ads email
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/import.sql --modelfilepath /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-email/ads-email-model.ttl --jsonoutputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-email/ads-email-jsonld.json --contextfile /Users/dipsy/github/dig-alignment/datasets/istr/context-for-istr-datasets.json --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/model-email/ads-email-rdf.n3" -Dexec.classpathScope=compile

########################################################
#			Ads-Attributes
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/dipsy/github/dig-alignment/datasets/istr/ads-attributes/import.sql --modelfilepath /Users/dipsy/github/dig-alignment/datasets/istr/ads-attributes/model-main/ads-attributes-main-model.ttl --jsonoutputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads-attributes/model-main/ads-attributes-main-jsonld.json --contextfile /Users/dipsy/github/dig-alignment/datasets/istr/context-for-istr-datasets.json --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads-attributes/model-main/ads-attributes-main-rdf.n3" -Dexec.classpathScope=compile


########################################################
#			Stanford Extractions
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype SQL --dbtype MySQL --hostname 23.101.198.62 --username dipsy --password sqlpassword --portnumber 3306 --dbname memex_small --queryfile /Users/dipsy/github/dig-alignment/datasets/istr/stanford-extractions/import.sql --modelfilepath /Users/dipsy/github/dig-alignment/datasets/istr/stanford-extractions/stanford-features-model.ttl --jsonoutputfile /Users/dipsy/github/dig-alignment/datasets/istr/stanford-extractions/x-stanford-features-jsonld.json --contextfile /Users/dipsy/github/dig-alignment/datasets/istr/context-for-istr-datasets.json --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/stanford-extractions/x-stanford-features-rdf.n3" -Dexec.classpathScope=compile
