# J3 data
* three open gun forum sites crawled by NYU
** www.glocktalk.com/forums
** www.calguns.net
** www.ar15.com/forums

* data obtained from NYU's S3 bucket
https://s3.amazonaws.com/vida-nyu/ATF/www.glocktalk.com_1432329770745_json.tar.gz
https://s3.amazonaws.com/vida-nyu/ATF/www.calguns.net_1432330019071_json.tar.gz
https://s3.amazonaws.com/vida-nyu/ATF/www.ar15.com_1432688094582_json.tar.gz

* When unzipped, these files contain json objects that are not newline
terminated.  So to create a single json-lines file, we run the
following scripts in the folder where we unzipped the archives.

* ./concat2jl.sh com_ar15_www
* ./concat2jl.sh net_calguns_www
* ./concat2jl.sh com_glocktalk_www
