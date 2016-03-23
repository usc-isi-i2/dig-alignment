mvn -e exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype JSON --filepath //Users/rajagopal/PycharmProjects/trie/citations-karmainput-full-without-html.json --modelfilepath /Users/rajagopal/Desktop/dig-alignment/versions/2.0/datasets/autonomy/ieee-citations/ieee-citations-model.ttl --sourcename ieee --outputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/citations-output.n3 --contextfile /Users/rajagopal/Desktop/dig-alignment/versions/2.0/karma/context.json --root "http://schema.org/ScholarlyArticle1" --jsonoutputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/citations-output.json" -Dexec.classpathScope=compile


mvn -e exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype JSON --filepath //Users/rajagopal/PycharmProjects/trie/keywords-karmainput-full-without-html.json --modelfilepath /Users/rajagopal/Desktop/dig-alignment/versions/2.0/datasets/autonomy/ieee-keywords/ieee-keywords-model.ttl --sourcename ieee --outputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/keywords-output.n3 --contextfile /Users/rajagopal/Desktop/dig-alignment/versions/2.0/karma/context.json --root "http://schema.org/ScholarlyArticle1" --jsonoutputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/keywords-output.json" -Dexec.classpathScope=compile

mvn -e exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype JSON --filepath //Users/rajagopal/PycharmProjects/trie/references-karmainput-full-without-html.json --modelfilepath /Users/rajagopal/Desktop/dig-alignment/versions/2.0/datasets/autonomy/ieee-references/ieee-references-model.ttl --sourcename ieee --outputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/references-output.n3 --contextfile /Users/rajagopal/Desktop/dig-alignment/versions/2.0/karma/context.json --root "http://schema.org/ScholarlyArticle1" --jsonoutputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/references-output.json" -Dexec.classpathScope=compile


mvn -e exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype JSON --filepath //Users/rajagopal/Desktop/github_repos/HG_Autonomy/karma-input-no-html/details-extracted.json --modelfilepath /Users/rajagopal/Desktop/dig-alignment/versions/2.0/datasets/autonomy/ieee-details/ieee-details-model.ttl --sourcename ieee --outputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/details-output.n3 --contextfile /Users/rajagopal/Desktop/dig-alignment/versions/2.0/karma/context.json --root "http://schema.org/Person1" --jsonoutputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/details-Person-output.json" -Dexec.classpathScope=compile


mvn -e exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype JSON --filepath //Users/rajagopal/Desktop/github_repos/HG_Autonomy/karma-input-no-html/details-extracted.json --modelfilepath /Users/rajagopal/Desktop/dig-alignment/versions/2.0/datasets/autonomy/ieee-details/ieee-details-model.ttl --sourcename ieee --outputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/details-output.n3 --contextfile /Users/rajagopal/Desktop/dig-alignment/versions/2.0/karma/context.json --root "http://schema.org/ScholarlyArticle1" --jsonoutputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/details-Scholar-output.json" -Dexec.classpathScope=compile



##sd
mvn -e exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype JSON --filepath /Users/rajagopal/Desktop/github_repos/landmark-extraction/sciencedirect-extracted.json --modelfilepath /Users/rajagopal/Desktop/dig-alignment/versions/2.0/datasets/autonomy/sciencedirect/sciencedirect-model.ttl --sourcename sciencedirect --outputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/sciencedirect-output.n3 --contextfile /Users/rajagopal/Desktop/dig-alignment/versions/2.0/karma/context.json --root "http://schema.org/ScholarlyArticle1" --jsonoutputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/sciencedirect-Scholar-output.json" -Dexec.classpathScope=compile

mvn -e exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype JSON --filepath /Users/rajagopal/Desktop/github_repos/landmark-extraction/sciencedirect-extracted.json --modelfilepath /Users/rajagopal/Desktop/dig-alignment/versions/2.0/datasets/autonomy/sciencedirect/sciencedirect-model.ttl --sourcename sciencedirect --outputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/sciencedirect-output.n3 --contextfile /Users/rajagopal/Desktop/dig-alignment/versions/2.0/karma/context.json --root "http://schema.org/Person1" --jsonoutputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/sciencedirect-Person-output.json" -Dexec.classpathScope=compile

##dtic article
mvn -e exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype JSON --filepath /Users/rajagopal/Desktop/github_repos/landmark-extraction/dtic-extracted.json --modelfilepath /Users/rajagopal/Desktop/dig-alignment/versions/2.0/datasets/autonomy/dtic/dtic-model.ttl --sourcename dtic --outputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/dtic-output.n3 --contextfile /Users/rajagopal/Desktop/dig-alignment/versions/2.0/karma/context.json --root "http://schema.org/ScholarlyArticle1" --jsonoutputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/dtic-Scholar-output.json" -Dexec.classpathScope=compile

mvn -e exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="--sourcetype JSON --filepath /Users/rajagopal/Desktop/github_repos/landmark-extraction/dtic-extracted.json --modelfilepath /Users/rajagopal/Desktop/dig-alignment/versions/2.0/datasets/autonomy/dtic/dtic-model.ttl --sourcename dtic --outputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/dtic-output.n3 --contextfile /Users/rajagopal/Desktop/dig-alignment/versions/2.0/karma/context.json --root "http://schema.org/Person1" --jsonoutputfile /Users/rajagopal/Desktop/github_repos/HG_Autonomy/dtic-Person-output.json" -Dexec.classpathScope=compile














