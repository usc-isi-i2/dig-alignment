
########################################################
#			Images
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Images \
--selection DEFAULT_TEST \
--filepath /Users/chengyey/dig-alignment/datasets/istr/images/images-sample.json \
--modelfilepath /Users/chengyey/dig-alignment/datasets/istr/images/ist-images-model.ttl \
--jsonoutputfile /Users/chengyey/dig-alignment/datasets/istr/images/ist-images-sample-jsonld.json \
--contextfile /Users/chengyey/dig-alignment/datasets/istr/context-for-istr-datasets.json \
--outputfile /Users/chengyey/dig-alignment/datasets/istr/images/ist-images-sample-rdf.n3" -Dexec.classpathScope=compile


########################################################
#			Ads
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads \
--selection DEFAULT_TEST \
--filepath /Users/chengyey/dig-alignment/datasets/istr/ads/ads-sample.json \
--modelfilepath /Users/chengyey/dig-alignment/datasets/istr/ads/model-main/ads-main-model.ttl \
--jsonoutputfile /Users/chengyey/dig-alignment/datasets/istr/ads/model-main/ads-main-sample-jsonld.json \
--contextfile /Users/chengyey/dig-alignment/datasets/istr/context-for-istr-datasets.json \
--outputfile /Users/chengyey/dig-alignment/datasets/istr/ads/model-main/ads-main-sample-rdf.n3" -Dexec.classpathScope=compile

#Ads phone
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads \
--selection DEFAULT_TEST \
--filepath /Users/chengyey/dig-alignment/datasets/istr/ads/ads-sample.json \
--modelfilepath /Users/chengyey/dig-alignment/datasets/istr/ads/model-phone/ads-phonenumber-model.ttl \
--jsonoutputfile /Users/chengyey/dig-alignment/datasets/istr/ads/model-phone/ads-phonenumber-sample-jsonld.json \
--contextfile /Users/chengyey/dig-alignment/datasets/istr/context-for-istr-datasets.json \
--outputfile /Users/chengyey/dig-alignment/datasets/istr/ads/model-address/ads-phonenumber-sample-rdf.n3" -Dexec.classpathScope=compile

#Ads address
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads \
--selection DEFAULT_TEST \
--filepath /Users/chengyey/dig-alignment/datasets/istr/ads/ads-sample.json \
--modelfilepath /Users/chengyey/dig-alignment/datasets/istr/ads/model-address/ads-address-model.ttl \
--jsonoutputfile /Users/chengyey/dig-alignment/datasets/istr/ads/model-address/ads-address-sample-jsonld.json \
--contextfile /Users/chengyey/dig-alignment/datasets/istr/context-for-istr-datasets.json \
--outputfile /Users/chengyey/dig-alignment/datasets/istr/ads/model-address/ads-address-sample-rdf.n3" -Dexec.classpathScope=compile

#Ads age
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads \
--selection DEFAULT_TEST \
--filepath /Users/chengyey/dig-alignment/datasets/istr/ads/ads-sample.json \
--modelfilepath /Users/chengyey/dig-alignment/datasets/istr/ads/model-age/ads-age-model.ttl \
--jsonoutputfile /Users/chengyey/dig-alignment/datasets/istr/ads/model-age/ads-age-sample-jsonld.json \
--contextfile /Users/chengyey/dig-alignment/datasets/istr/context-for-istr-datasets.json \
--outputfile /Users/chengyey/dig-alignment/datasets/istr/ads/model-age/ads-age-sample-rdf.n3" -Dexec.classpathScope=compile

#Ads website
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads \
--selection DEFAULT_TEST \
--filepath /Users/chengyey/dig-alignment/datasets/istr/ads/ads-sample.json \
--modelfilepath /Users/chengyey/dig-alignment/datasets/istr/ads/model-website/ads-website-model.ttl \
--jsonoutputfile /Users/chengyey/dig-alignment/datasets/istr/ads/model-website/ads-website-sample-jsonld.json \
--contextfile /Users/chengyey/dig-alignment/datasets/istr/context-for-istr-datasets.json \
--outputfile /Users/chengyey/dig-alignment/datasets/istr/ads/model-website/ads-website-sample-rdf.n3" -Dexec.classpathScope=compile

#Ads gender
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads \
--selection DEFAULT_TEST \
--filepath /Users/chengyey/dig-alignment/datasets/istr/ads/ads-sample.json \
--modelfilepath /Users/chengyey/dig-alignment/datasets/istr/ads/model-gender/ads-gender-model.ttl \
--jsonoutputfile /Users/chengyey/dig-alignment/datasets/istr/ads/model-gender/ads-gender-sample-jsonld.json \
--contextfile /Users/chengyey/dig-alignment/datasets/istr/context-for-istr-datasets.json \
--outputfile /Users/chengyey/dig-alignment/datasets/istr/ads/model-gender/ads-gender-sample-rdf.n3" -Dexec.classpathScope=compile

#Ads email
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads \
--selection DEFAULT_TEST \
--filepath /Users/chengyey/dig-alignment/datasets/istr/ads/ads-sample.json \
--modelfilepath /Users/chengyey/dig-alignment/datasets/istr/ads/model-email/ads-email-model.ttl \
--jsonoutputfile /Users/chengyey/dig-alignment/datasets/istr/ads/model-email/ads-email-sample-jsonld.json \
--contextfile /Users/chengyey/dig-alignment/datasets/istr/context-for-istr-datasets.json \
--outputfile /Users/chengyey/dig-alignment/datasets/istr/ads/model-email/ads-email-sample-rdf.n3" -Dexec.classpathScope=compile

########################################################
#			Ads-Attributes
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads-Attributes \
--selection DEFAULT_TEST \
--filepath /Users/chengyey/dig-alignment/datasets/istr/ads-attributes/add-attributes-sample-100.json \
--modelfilepath /Users/chengyey/dig-alignment/datasets/istr/ads-attributes/model-main/ads-attributes-main-model.ttl \
--jsonoutputfile /Users/chengyey/dig-alignment/datasets/istr/ads-attributes/model-main/ads-attributes-main-sample-jsonld.json \
--contextfile /Users/chengyey/dig-alignment/datasets/istr/context-for-istr-datasets.json \
--outputfile /Users/chengyey/dig-alignment/datasets/istr/ads-attributes/model-main/ads-attributes-main-sample-rdf.n3" -Dexec.classpathScope=compile

#Ads attributes Rate
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads-Attributes \
--selection DEFAULT_TEST \
--filepath /Users/chengyey/dig-alignment/datasets/istr/ads-attributes/add-attributes-sample-100.json \
--modelfilepath /Users/chengyey/dig-alignment/datasets/istr/ads-attributes/model-rate/ads-attributes-rate-model.ttl \
--jsonoutputfile /Users/chengyey/dig-alignment/datasets/istr/ads-attributes/model-rate/ads-attributes-rate-sample-jsonld.json \
--contextfile /Users/chengyey/dig-alignment/datasets/istr/context-for-istr-datasets.json \
--outputfile /Users/chengyey/dig-alignment/datasets/istr/ads-attributes/model-rate/ads-attributes-rate-sample-rdf.n3" -Dexec.classpathScope=compile

########################################################
#			Stanford Extractions
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Stanford-Extractions \
--selection DEFAULT_TEST \
--filepath /Users/chengyey/dig-alignment/datasets/istr/stanford-extractions/stanford-features-sample.json \
--modelfilepath /Users/chengyey/dig-alignment/datasets/istr/stanford-extractions/stanford-features-model.ttl \
--jsonoutputfile /Users/chengyey/dig-alignment/datasets/istr/stanford-extractions/x-stanford-features-sample-jsonld.json \
--contextfile /Users/chengyey/dig-alignment/datasets/istr/context-for-istr-datasets.json \
--outputfile /Users/chengyey/dig-alignment/datasets/istr/stanford-extractions/x-stanford-features-sample-rdf.n3" -Dexec.classpathScope=compile
