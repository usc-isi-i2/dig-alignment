DIG_ALIGNMENT_HOME=$1
CONTEXT_URL="https://raw.githubusercontent.com/usc-isi-i2/dig-alignment/development/datasets/istr/context-for-istr-datasets.json"
function compare_outputs_images {
	BASE_DIR="${DIG_ALIGNMENT_HOME}/datasets/istr/images"
	compare_outputs "${BASE_DIR}/ist-images-jsonld.json" "${BASE_DIR}/ist-images-sample-jsonld.json" 
}

function compare_outputs_ads {
	BASE_DIR="${DIG_ALIGNMENT_HOME}/datasets/istr/ads"
	compare_outputs "${BASE_DIR}/model-${1}/ads-${1}-jsonld.json" "${BASE_DIR}/model-${1}/ads-${1}-sample-jsonld.json" 
}

function compare_outputs_stanford_extractions {
	BASE_DIR="${DIG_ALIGNMENT_HOME}/datasets/istr/stanford-extractions"
	compare_outputs "${BASE_DIR}/model-${1}/stanford-${1}-jsonld.json" "${BASE_DIR}/model-${1}/stanford-${1}-sample-jsonld.json" 
}

function compare_outputs_ads_attributes {
	BASE_DIR="${DIG_ALIGNMENT_HOME}/datasets/istr/ads-attributes"
	compare_outputs "${BASE_DIR}/model-${1}/ads-attributes-${1}-jsonld.json" "${BASE_DIR}/model-${1}/ads-attributes-${1}-sample-jsonld.json" 
}

function compare_outputs {
	INTERACTIVE_LC=$(wc -l ${1} | sed -E 's/([^0-9]*([0-9]*)){1}.*/\2/')
	OFFLINE_LC=$(wc -l ${2} | sed -E 's/([^0-9]*([0-9]*)){1}.*/\2/')
	if [ "$INTERACTIVE_LC" -ne "$OFFLINE_LC" ]
	then
		echo "line count differs ${INTERACTIVE_LC} ${OFFLINE_LC}"
	else
		echo "line counts match for ${1} and ${2}"
	fi	
}

function run_offline_with_defaults_images {
	BASE_DIR="${DIG_ALIGNMENT_HOME}/datasets/istr/images"
	INPUT_FILE="${BASE_DIR}/images-sample.json"
	run_offline_with_defaults "Images" "$INPUT_FILE" "${BASE_DIR}/ist-images-model.ttl" "$BASE_DIR/ist-images-sample-jsonld.json" "$BASE_DIR/ist-images-sample-rdf.n3"
}

function run_offline_with_defaults_ads {
	BASE_DIR="${DIG_ALIGNMENT_HOME}/datasets/istr/ads"
	INPUT_FILE="${BASE_DIR}/ads-sample.json"
	run_offline_with_defaults "Ads" "$INPUT_FILE" "${BASE_DIR}/model-${1}/ads-${1}-model.ttl" "$BASE_DIR/model-${1}/ads-${1}-sample-jsonld.json" "$BASE_DIR/model-${1}/ads-${1}-sample-rdf.n3"
}

function run_offline_with_defaults_stanford_extraction {
	BASE_DIR="${DIG_ALIGNMENT_HOME}/datasets/istr/stanford-extractions"
	INPUT_FILE="${BASE_DIR}/stanford-features-sample.json"
	run_offline_with_defaults "Stanford-Extractions" "$INPUT_FILE" "${BASE_DIR}/model-${1}/stanford-${1}-model.ttl" "$BASE_DIR/model-${1}/stanford-${1}-sample-jsonld.json" "$BASE_DIR/model-${1}/stanford-${1}-sample-rdf.n3"
}

function run_offline_with_defaults_ads_attributes {
	BASE_DIR="${DIG_ALIGNMENT_HOME}/datasets/istr/ads-attributes"
	INPUT_FILE="${DIG_ALIGNMENT_HOME}/datasets/istr/ads-attributes/add-attributes-sample-100.json"
	run_offline_with_defaults "Ads-Attributes" "$INPUT_FILE" "${BASE_DIR}/model-${1}/ads-attributes-${1}-model.ttl" "$BASE_DIR/model-${1}/ads-attributes-${1}-sample-jsonld.json" "$BASE_DIR/model-${1}/ads-attributes-${1}-sample-rdf.n3"
}

function run_offline_with_defaults {

	run_offline "JSON" "${1}" "DEFAULT_TEST" "${2}" "${3}" "${4}" "$CONTEXT_URL" "${5}"
}
function run_offline {
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="\
--sourcetype ${1} \
--sourcename ${2} \
--selection ${3} \
--filepath ${4} \
--modelfilepath ${5} \
--jsonoutputfile ${6} \
--contexturl ${7} \
--outputfile ${8}" \
>> karma.out 2>> karma.err
RETURN=$?
if [ "${RETURN}" -ne 0 ]
then
	echo "karma failed to apply ${5} to ${4}"
else
	echo "karma succeeded applying ${5} to ${4}"
fi	
}

########################################################
#			Images
########################################################
run_offline_with_defaults_images 
compare_outputs_images

########################################################
#			Ads
########################################################
run_offline_with_defaults_ads "main"
compare_outputs_ads "main"

#Ads phone
run_offline_with_defaults_ads "phone"
compare_outputs_ads "phone"

#Ads address
run_offline_with_defaults_ads "address"
compare_outputs_ads "address"

#Ads age
run_offline_with_defaults_ads "age"
compare_outputs_ads "age"

#Ads website
run_offline_with_defaults_ads "website"
compare_outputs_ads "website"

#Ads gender
run_offline_with_defaults_ads "gender"
compare_outputs_ads "gender"

#Ads email
run_offline_with_defaults_ads "email"
compare_outputs_ads "email"


########################################################
#			Ads-Attributes
########################################################
run_offline_with_defaults_ads_attributes "main"
compare_outputs_ads_attributes "main"

run_offline_with_defaults_ads_attributes "rate"
compare_outputs_ads_attributes "rate"

run_offline_with_defaults_ads_attributes "phone"
compare_outputs_ads_attributes "phone"


########################################################
#			Stanford Extractions
########################################################
#Phone Number
run_offline_with_defaults_stanford_extraction "phone"
compare_outputs_stanford_extractions "phone"

#Person Name
run_offline_with_defaults_stanford_extraction "person-name"
compare_outputs_stanford_extractions "person-name"

#Address
run_offline_with_defaults_stanford_extraction "address"
compare_outputs_stanford_extractions "address"
