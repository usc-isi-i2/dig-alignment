Data Source: https://memexproxy.com/wiki/pages/viewpage.action?title=Data+Catalog&spaceKey=MPM
			 Row: QPR 2 ATF Data
			 Direct Link: https://aden.istresearch.com/memex/qpr2/atf/evolution-forums.tar.xz

Data Type: Raw HTML files

The data is extracted using Inferlink's extraction code.
a. Copy the data to DT cluster
b. Run extractor on hadoop:
nohup time hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapred.map.tasks=100 \
    -D mapred.reduce.tasks=500 \
    -libjars /home/ubuntu/landmark-extraction/karma-mr.jar \
    -file /home/ubuntu/landmark-extraction/src/mr_landmark_html_mapper.py \
    -cacheFile hdfs://memex-nn1:8020/user/ubuntu/landmark-extractions/rules/evolution-forums_rules.txt#rules.txt \
    -cacheFile hdfs://memex-nn1:8020/user/ubuntu/landmark-extractions/rules/evolution-forums_urls.txt#urls.txt \
    -file /home/ubuntu/landmark-extraction/src/landmark.mod \
    -mapper /home/ubuntu/landmark-extraction/src/mr_landmark_html_mapper.py \
    -file /home/ubuntu/landmark-extraction/src/mr_landmark_reducer.py \
    -reducer /home/ubuntu/landmark-extraction/src/mr_landmark_reducer.py \
    -input /user/ubuntu/landmark-extractions/input/evolution-forums/* \
    -output /user/ubuntu/landmark-extractions/output/evolution-forums \
    -inputformat edu.isi.karma.mapreduce.inputformat.HTMLInputFormat &

c. Put the output of the above into the required folder for the workflow and then run the Karma workflow


