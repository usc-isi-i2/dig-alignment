DIG_ALIGNMENT_HOME=$1
########################################################
#			Images
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Images \
--selection DEFAULT_TEST \
--filepath ${DIG_ALIGNMENT_HOME}/datasets/istr/images/images-sample.json \
--modelfilepath ${DIG_ALIGNMENT_HOME}/datasets/istr/images/ist-images-model.ttl \
--jsonoutputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/images/ist-images-sample-jsonld.json \
--contexturl https://raw.githubusercontent.com/usc-isi-i2/dig-alignment/development/datasets/istr/context-for-istr-datasets.json \
--outputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/images/ist-images-sample-rdf.n3" 


########################################################
#			Ads
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads \
--selection DEFAULT_TEST \
--filepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/ads-sample.json \
--modelfilepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-main/ads-main-model.ttl \
--jsonoutputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-main/ads-main-sample-jsonld.json \
--contexturl https://raw.githubusercontent.com/usc-isi-i2/dig-alignment/development/datasets/istr/context-for-istr-datasets.json \
--outputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-main/ads-main-sample-rdf.n3" 

#Ads phone
# mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
# --sourcetype JSON \
# --sourcename Ads \
# --selection DEFAULT_TEST \
# --filepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/ads-sample.json \
# --modelfilepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-phone/ads-phonenumber-model.ttl \
# --jsonoutputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-phone/ads-phonenumber-sample-jsonld.json \
# --contexturl https://raw.githubusercontent.com/usc-isi-i2/dig-alignment/development/datasets/istr/context-for-istr-datasets.json \ 
# --outputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-address/ads-phonenumber-sample-rdf.n3" 

#Ads address
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads \
--selection DEFAULT_TEST \
--filepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/ads-sample.json \
--modelfilepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-address/ads-address-model.ttl \
--jsonoutputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-address/ads-address-sample-jsonld.json \
--contexturl https://raw.githubusercontent.com/usc-isi-i2/dig-alignment/development/datasets/istr/context-for-istr-datasets.json \
--outputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-address/ads-address-sample-rdf.n3" 

#Ads age
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads \
--selection DEFAULT_TEST \
--filepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/ads-sample.json \
--modelfilepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-age/ads-age-model.ttl \
--jsonoutputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-age/ads-age-sample-jsonld.json \
--contexturl https://raw.githubusercontent.com/usc-isi-i2/dig-alignment/development/datasets/istr/context-for-istr-datasets.json \
--outputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-age/ads-age-sample-rdf.n3" 

#Ads website
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads \
--selection DEFAULT_TEST \
--filepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/ads-sample.json \
--modelfilepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-website/ads-website-model.ttl \
--jsonoutputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-website/ads-website-sample-jsonld.json \
--contexturl https://raw.githubusercontent.com/usc-isi-i2/dig-alignment/development/datasets/istr/context-for-istr-datasets.json \
--outputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-website/ads-website-sample-rdf.n3" 

#Ads gender
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads \
--selection DEFAULT_TEST \
--filepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/ads-sample.json \
--modelfilepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-gender/ads-gender-model.ttl \
--jsonoutputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-gender/ads-gender-sample-jsonld.json \
--contexturl https://raw.githubusercontent.com/usc-isi-i2/dig-alignment/development/datasets/istr/context-for-istr-datasets.json \
--outputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-gender/ads-gender-sample-rdf.n3" 

#Ads email
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads \
--selection DEFAULT_TEST \
--filepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/ads-sample.json \
--modelfilepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-email/ads-email-model.ttl \
--jsonoutputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-email/ads-email-sample-jsonld.json \
--contexturl https://raw.githubusercontent.com/usc-isi-i2/dig-alignment/development/datasets/istr/context-for-istr-datasets.json \
--outputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads/model-email/ads-email-sample-rdf.n3" 

########################################################
#			Ads-Attributes
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads-Attributes \
--selection DEFAULT_TEST \
--filepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads-attributes/add-attributes-sample-100.json \
--modelfilepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads-attributes/model-main/ads-attributes-main-model.ttl \
--jsonoutputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads-attributes/model-main/ads-attributes-main-sample-jsonld.json \
--contexturl https://raw.githubusercontent.com/usc-isi-i2/dig-alignment/development/datasets/istr/context-for-istr-datasets.json \
--outputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads-attributes/model-main/ads-attributes-main-sample-rdf.n3" 
INTERACTIVE_LC=$(wc -l ${DIG_ALIGNMENT_HOME}/datasets/istr/ads-attributes/model-main/ads-attributes-main-jsonld.json)
OFFLINE_LC=$(wc -l ${DIG_ALIGNMENT_HOME}/datasets/istr/ads-attributes/model-main/ads-attributes-main-sample-jsonld.json)
if[ "$INTERACTIVE_LC" -nq "$OFFLINE_LC" ]
	echo "line count differs"
fi
#Ads attributes Rate
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads-Attributes \
--selection DEFAULT_TEST \
--filepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads-attributes/add-attributes-sample-100.json \
--modelfilepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads-attributes/model-rate/ads-attributes-rate-model.ttl \
--jsonoutputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads-attributes/model-rate/ads-attributes-rate-sample-jsonld.json \
--contexturl https://raw.githubusercontent.com/usc-isi-i2/dig-alignment/development/datasets/istr/context-for-istr-datasets.json \
--outputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads-attributes/model-rate/ads-attributes-rate-sample-rdf.n3" 

#Ads attributes phone
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Ads-Attributes \
--filepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads-attributes/add-attributes-sample-100.json \
--modelfilepath ${DIG_ALIGNMENT_HOME}/datasets/istr/ads-attributes/model-rate/ads-attributes-rate-model.ttl \
--jsonoutputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads-attributes/model-rate/ads-attributes-rate-sample-jsonld.json \
--contexturl https://raw.githubusercontent.com/usc-isi-i2/dig-alignment/development/datasets/istr/context-for-istr-datasets.json \
--outputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/ads-attributes/model-rate/ads-attributes-rate-sample-rdf.n3" 

########################################################
#			Stanford Extractions
########################################################
#Phone Number
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Stanford-Extractions \
--filepath ${DIG_ALIGNMENT_HOME}/datasets/istr/stanford-extractions/stanford-features-sample.json \
--modelfilepath ${DIG_ALIGNMENT_HOME}/datasets/istr/stanford-extractions/model-phone/stanford-phone-model.ttl \
--jsonoutputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/stanford-extractions/model-phone/stanford-phone-sample-jsonld.json \
--contexturl https://raw.githubusercontent.com/usc-isi-i2/dig-alignment/development/datasets/istr/context-for-istr-datasets.json \
--outputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/stanford-extractions/model-phone/stanford-phone-sample-rdf.n3" 

#Person Name
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Stanford-Extractions \
--filepath ${DIG_ALIGNMENT_HOME}/datasets/istr/stanford-extractions/stanford-features-sample.json \
--modelfilepath ${DIG_ALIGNMENT_HOME}/datasets/istr/stanford-extractions/model-person-name/stanford-person-name-model.ttl \
--jsonoutputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/stanford-extractions/model-person-name/stanford-person-name-sample-jsonld.json \
--contexturl https://raw.githubusercontent.com/usc-isi-i2/dig-alignment/development/datasets/istr/context-for-istr-datasets.json \
--outputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/stanford-extractions/model-person-name/stanford-person-name-sample-rdf.n3" 

#Address
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype JSON \
--sourcename Stanford-Extractions \
--filepath ${DIG_ALIGNMENT_HOME}/datasets/istr/stanford-extractions/stanford-features-sample.json \
--modelfilepath ${DIG_ALIGNMENT_HOME}/datasets/istr/stanford-extractions/model-address/stanford-address-model.ttl \
--jsonoutputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/stanford-extractions/model-address/stanford-address-sample-jsonld.json \
--contexturl https://raw.githubusercontent.com/usc-isi-i2/dig-alignment/development/datasets/istr/context-for-istr-datasets.json \
--outputfile ${DIG_ALIGNMENT_HOME}/datasets/istr/stanford-extractions/model-address/stanford-address-sample-rdf.n3" 
