
########################################################
#			Images
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.GenerateContextFromModel" -Dexec.args="--modelpath /Users/dipsy/github/dig-alignment/datasets/istr/images/ist-images-model.ttl --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/images/ist-images-context.json" -Dexec.classpathScope=compile

########################################################
#			Ads
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.GenerateContextFromModel" -Dexec.args="--modelpath /Users/dipsy/github/dig-alignment/datasets/istr/ads/v06-ads-model.ttl --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads/v06-ads-context.json" -Dexec.classpathScope=compile


########################################################
#			Ads-Attributes
########################################################
# Have created the context for Ads-Attributes manually
#mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.GenerateContextFromModel" -Dexec.args="--modelpath /Users/dipsy/github/dig-alignment/datasets/istr/ads-attributes/ads-attributes-features-model.ttl --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/ads-attributes/ads-attributes-features-context.json" -Dexec.classpathScope=compile


########################################################
#			Stanford Extractions
########################################################
mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.GenerateContextFromModel" -Dexec.args="--modelpath /Users/dipsy/github/dig-alignment/datasets/istr/stanford-extractions/stanford-features-model.ttl --outputfile /Users/dipsy/github/dig-alignment/datasets/istr/stanford-extractions/stanford-features-context.json" -Dexec.classpathScope=compile
