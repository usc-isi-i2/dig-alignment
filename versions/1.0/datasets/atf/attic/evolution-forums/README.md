Data Source: https://memexproxy.com/wiki/pages/viewpage.action?title=Data+Catalog&spaceKey=MPM
			 Row: QPR 2 ATF Data
			 Direct Link: https://aden.istresearch.com/memex/qpr2/atf/evolution-forums.tar.xz

Data Type: Raw HTML files

The data is extracted using Inferlink's extraction code.
a. Copy the data to DT cluster and unzip it
ssh -i ~/keypairs/diglshhadoop-01.pem ubuntu@10.3.2.99
Copy data to /ISI/atf and then unzip

b. Convert data to sequence file
cd /ISI/Web-Karma/karma-mr
edit /ISI/atf/genseq.properties to update the input and output folders
run > nohup /ISI/Web-Karma/karma-mr/start-covert.sh &
to convert to sequence files.
start-convert.sh executes:
mvn exec:java -Dexec.mainClass="edu.isi.karma.mapreduce.driver.InputFileDirectoryader" -Dexec.args="/ISI/atf/genseq.properties" -Dexec.classpathScope=compile

c. Make sure the output of the above is in
/home/worker/extractor-ingest/evolution-forums

d. Execute the 'extract-atf-evolution-forums' workflow on Hue

or run the following hadoop job: 
nohup time hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapred.map.tasks=100 \
    -D mapred.reduce.tasks=500 \
    -libjars /home/worker/landmark-extraction/karma-mr.jar \
    -file /home/worker/landmark-extraction/mr_landmark_seq_mapper.py \
    -file /home/worker/landmark-extraction/rules/evolution-forums\rules.txt
    -file /home/worker/landmark-extraction/rules/evolution-forums\urls.txt
    -file /home/worker/landmark-extraction/landmark.mod \
    -mapper /home/worker/landmark-extraction/mr_landmark_seq_mapper.py \
    -file /home/worker/landmark-extraction/mr_landmark_reducer.py \
    -reducer /home/worker/landmark-extraction/mr_landmark_reducer.py \
    -input /user/worker/landmark-extractions/input/evolution-forums/* \
    -output /user/woker/ingest/atf/evolution-forums/test01/ \
    -inputformat edu.isi.karma.mapreduce.inputformat.SequenceFileAsLineInputFormat &



