mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args="
--sourcetype JSON \
--filepath \"/Users/szekely/Downloads/autonomy_2291_pdfextractions.json\" \
--modelfilepath \"/Users/szekely/github/dig-alignment/versions/2.0/datasets/autonomy/jpl-pdf/jpl-pdf-model.ttl\" \
--sourcename jpl-pdf \
--outputfile wikipedia-rdf.n3" -Dexec.classpathScope=compile