#!/bin/sh

splitter=/opt/local/libexec/perl5.16/sitebin/xml_split
size='100M'
karmamr=/Users/philpot/Documents/project/Web-Karma/karma-mr

# infile: something like iheartguns.com.xml
infile=$1

# Note that linux readlink = mac greadlink (gnu readlink)
if [ "$OSTYPE" = "darwin14" ] ; then
    HERE=$(dirname $(greadlink -f $0))
else
    HERE=$(dirname $(readlink -f $0))
fi

# infer the open/close tag pair from first line (heuristic)
openTag=`head -1 $infile`
closeTag="</"${openTag:1}

# figure out the core file from input like iheartguns.com.xml => iheartguns.com
stopPosition=$((${#infile} - 4))
base=${infile:0:$stopPosition}

# Break the input file into files of $size
${splitter} -s${size} ${infile}

# get rid of the reassembly skeleton
rm ${base}-00.xml

# replace skeleton begin/end tags with desired open/close
# Note that sed -i has different behaviors on linux and mac/darwin/BSD
if [ "$OSTYPE" = "darwin14" ] ; then
    sed -i '' "s#<xml_split:root xmlns:xml_split=\"http://xmltwig.com/xml_split\">#$openTag#" ${base}-*.xml
    sed -i '' "s#</xml_split:root>#$closeTag#" ${base}-*.xml
else
    sed -i "s#<xml_split:root xmlns:xml_split=\"http://xmltwig.com/xml_split\">#$openTag#" ${base}-*.xml
    sed -i "s#</xml_split:root>##closeTag#" ${base}-*.xml
fi

workDir=`mktemp -d -t "$(basename $0).work.XXXXXXXXXX"`
echo "workDir is [[ $workDir ]]"

propertiesFile=`mktemp -t "$(basename $0).prop.XXXXXXXXXX"`
echo "properties file is [[ $propertiesFile ]]"

# put all artifacts in temporary dir
for inputFile in $base-*.xml ; 
do
    rm -f $workDir/*
    cp $inputFile $workDir
    echo "copied $inputFile to $workDir"
    # write output here
    outputFile=${HERE}/${inputFile}.seq
    echo "outputFile is $outputFile"
    # generate properties file for Karma MR task
    touch $propertiesFile
    echo "input.directory=${workDir}" > $propertiesFile
    echo "output.file=${outputFile}" >> $propertiesFile
    echo "propertiesFile is $propertiesFile"
    # use this properties file to instantiate karma run
    cd $karmamr
    mvn exec:java -Dexec.mainClass="edu.isi.karma.mapreduce.driver.InputFileDirectoryLoader" -Dexec.args="$propertiesFile"
    cd $HERE

    # cleanup
    rm -f $workDir/*
    rm -f $propertiesFile
done




# # Large files:
# # split into chunks of about size 100M
# # don't split files smaller than that

# echo ducksouth.com.xml
# ${splitter} -s${size} ${dir}/ducksouth.com.xml
# rm ${dir}/ducksouth.com-00.xml
# sed -i '' '1d;$d' ${dir}/ducksouth.com-*.xml

# echo levergunscommunity.com.xml
# ${splitter} -s${size} ${dir}/levergunscommunity.com.xml
# rm ${dir}/levergunscommunity.com-00.xml
# sed -i '' '1d;$d' ${dir}/levergunscommunity.com-*.xml

# echo texaschlforum.com.xml
# ${splitter} -s${size} ${dir}/texaschlforum.com.xml
# rm ${dir}/texaschlforum.com-00.xml
# sed -i '' '1d;$d' ${dir}/texaschlforum.com-*.xml

# echo tndeer.com.xml
# ${splitter} -s${size} ${dir}/tndeer.com.xml
# rm ${dir}/tndeer.com-00.xml
# sed -i '' '1d;$d' ${dir}/tndeer.com-*.xml

# echo ohioccwforums.org.xml
# ${splitter} -s${size} ${dir}/ohioccwforums.org.xml
# rm ${dir}/ohioccwforums.org-00.xml
# sed -i '' '1d;$d' ${dir}/ohioccwforums.org-*.xml

# echo theliberalgunclub.com.xml
# ${splitter} -s${size} ${dir}/theliberalgunclub.com.xml
# rm ${dir}/theliberalgunclub.com-00.xml
# sed -i '' '1d;$d' ${dir}/theliberalgunclub.com-*.xml

# echo comebackalive.com.xml
# ${splitter} -s${size} ${dir}/comebackalive.com.xml
# rm ${dir}/comebackalive.com-00.xml
# sed -i '' '1d;$d' ${dir}/comebackalive.com-*.xml

# echo nosler.com.xml
# ${splitter} -s${size} ${dir}/nosler.com.xml
# rm ${dir}/nosler.com-00.xml
# sed -i '' '1d;$d' ${dir}/nosler.com-*.xml

# echo americanpreppersnetwork.net.xml
# ${splitter} -s${size} ${dir}/americanpreppersnetwork.net.xml
# rm ${dir}/americanpreppersnetwork.net-00.xml
# sed -i '' '1d;$d' ${dir}/americanpreppersnetwork.net-*.xml

# echo isthmus.com.xml
# ${splitter} -s${size} ${dir}/isthmus.com.xml
# rm ${dir}/isthmus.com-00.xml
# sed -i '' '1d;$d' ${dir}/isthmus.com-*.xml

# echo nodakoutdoors.com.xml
# ${splitter} -s${size} ${dir}/nodakoutdoors.com.xml
# rm ${dir}/nodakoutdoors.com-00.xml
# sed -i '' '1d;$d' ${dir}/nodakoutdoors.com-*.xml

# echo utahconcealedcarry.com.xml
# ${splitter} -s${size} ${dir}/utahconcealedcarry.com.xml
# rm ${dir}/utahconcealedcarry.com-00.xml
# sed -i '' '1d;$d' ${dir}/utahconcealedcarry.com-*.xml

# echo modernmuzzleloader.com.xml
# ${splitter} -s${size} ${dir}/modernmuzzleloader.com.xml
# rm ${dir}/modernmuzzleloader.com-00.xml
# sed -i '' '1d;$d' ${dir}/modernmuzzleloader.com-*.xml

# echo spokaneguntrader.com.xml
# ${splitter} -s${size} ${dir}/spokaneguntrader.com.xml
# rm ${dir}/spokaneguntrader.com-00.xml
# sed -i '' '1d;$d' ${dir}/spokaneguntrader.com-*.xml

# echo gobblernation.com.xml
# ${splitter} -s${size} ${dir}/gobblernation.com.xml
# rm ${dir}/gobblernation.com-00.xml
# sed -i '' '1d;$d' ${dir}/gobblernation.com-*.xml

# echo kentuckyarmoryclub.com.xml
# ${splitter} -s${size} ${dir}/kentuckyarmoryclub.com.xml
# rm ${dir}/kentuckyarmoryclub.com-00.xml
# sed -i '' '1d;$d' ${dir}/kentuckyarmoryclub.com-*.xml

# # <xml_split:root xmlns:xml_split="http://xmltwig.com/xml_split">



# # Small files

# sed '1d;$d' ${dir}/arguntrader.com.xml > ${dir}/arguntrader.com-01.xml
# sed '1d;$d' ${dir}/claytargetclassifieds.com.xml > ${dir}/claytargetclassifieds.com-01.xml
# sed '1d;$d' ${dir}/henryfirearms.org.xml > ${dir}/henryfirearms.org-01.xml
# sed '1d;$d' ${dir}/marauderairrifle.com.xml > ${dir}/marauderairrifle.com-01.xml
# sed '1d;$d' ${dir}/newmexicoguntrader.net.xml > ${dir}/newmexicoguntrader.net-01.xml
# sed '1d;$d' ${dir}/remingtonsociety.com.xml > ${dir}/remingtonsociety.com-01.xml
# sed '1d;$d' ${dir}/rossi-rifleman.com.xml > ${dir}/rossi-rifleman.com-01.xml
# sed '1d;$d' ${dir}/silencerforum.com.xml > ${dir}/silencerforum.com-01.xml
# sed '1d;$d' ${dir}/tfaonline.org.xml > ${dir}/tfaonline.org-01.xml
# sed '1d;$d' ${dir}/treasurestatearms.com.xml > ${dir}/treasurestatearms.com-01.xml
