mvn exec:java -Dexec.mainClass="edu.isi.karma.rdf.OfflineRdfGenerator" -Dexec.args=" \
--sourcetype JSON --filepath \"/Users/szekely/Downloads/autonomy_2291_pdfextractions.json\" \
--modelfilepath \"/Users/szekely/github/dig-alignment/versions/2.0/datasets/autonomy/jpl-pdf/jpl-pdf-model.ttl\" \
--sourcename jpl-pdf \
--selection \"DEFAULT_TEST\" \
--outputfile jpl-output.n3 \
--contextfile \"/Users/szekely/github/dig-alignment/versions/2.0/datasets/autonomy/jpl-pdf/jpl-pdf-context.json\" \
--root \"http://schema.org/ScholarlyArticle2\" \
--encoding \"UTF-8\" \
--jsonoutputfile /Users/szekely/Downloads/jpl-sdo/jpl-pdf-scholarlyarticle2.json" -Dexec.classpathScope=compile
