#!/bin/sh

splitter=/opt/local/libexec/perl5.16/sitebin/xml_split
size='100M'
dir=/Users/philpot/Documents/project/dig-alignment/datasets/atf/j28json

# Large files:
# split into chunks of about size 100M
# don't split files smaller than that

echo ducksouth.com.xml
${splitter} -s${size} ${dir}/ducksouth.com.xml
rm ${dir}/ducksouth.com.xml-00.xml
sed -i '' '1;$d' ${dir}/ducksouth.com-*.xml

echo levergunscommunity.com.xml
${splitter} -s${size} ${dir}/levergunscommunity.com.xml
rm ${dir}/levergunscommunity.com.xml-00.xml
sed -i '' '1;$d' ${dir}/levergunscommunity.com-*.xml

echo texaschlforum.com.xml
${splitter} -s${size} ${dir}/texaschlforum.com.xml
rm ${dir}/texaschlforum.com.xml-00.xml
sed -i '' '1;$d' ${dir}/texaschlforum.com-*.xml

echo tndeer.com.xml
${splitter} -s${size} ${dir}/tndeer.com.xml
rm ${dir}/tndeer.com.xml-00.xml
sed -i '' '1;$d' ${dir}/tndeer.com-*.xml

echo ohioccwforums.org.xml
${splitter} -s${size} ${dir}/ohioccwforums.org.xml
rm ${dir}/ohioccwforums.org.xml-00.xml
sed -i '' '1;$d' ${dir}/ohioccwforums.org-*.xml

echo theliberalgunclub.com.xml
${splitter} -s${size} ${dir}/theliberalgunclub.com.xml
rm ${dir}/theliberalgunclub.com.xml-00.xml
sed -i '' '1;$d' ${dir}/theliberalgunclub.com-*.xml

echo comebackalive.com.xml
${splitter} -s${size} ${dir}/comebackalive.com.xml
rm ${dir}/comebackalive.com.xml-00.xml
sed -i '' '1;$d' ${dir}/comebackalive.com-*.xml

echo nosler.com.xml
${splitter} -s${size} ${dir}/nosler.com.xml
rm ${dir}/nosler.com.xml-00.xml
sed -i '' '1;$d' ${dir}/nosler.com-*.xml

echo americanpreppersnetwork.net.xml
${splitter} -s${size} ${dir}/americanpreppersnetwork.net.xml
rm ${dir}/americanpreppersnetwork.net.xml-00.xml
sed -i '' '1;$d' ${dir}/americanpreppersnetwork.net-*.xml

echo isthmus.com.xml
${splitter} -s${size} ${dir}/isthmus.com.xml
rm ${dir}/isthmus.com.xml-00.xml
sed -i '' '1;$d' ${dir}/isthmus.com-*.xml

echo nodakoutdoors.com.xml
${splitter} -s${size} ${dir}/nodakoutdoors.com.xml
rm ${dir}/nodakoutdoors.com.xml-00.xml
sed -i '' '1;$d' ${dir}/nodakoutdoors.com-*.xml

echo utahconcealedcarry.com.xml
${splitter} -s${size} ${dir}/utahconcealedcarry.com.xml
rm ${dir}/utahconcealedcarry.com.xml-00.xml
sed -i '' '1;$d' ${dir}/utahconcealedcarry.com-*.xml

echo modernmuzzleloader.com.xml
${splitter} -s${size} ${dir}/modernmuzzleloader.com.xml
rm ${dir}/modernmuzzleloader.com.xml-00.xml
sed -i '' '1;$d' ${dir}/modernmuzzleloader.com-*.xml

echo spokaneguntrader.com.xml
${splitter} -s${size} ${dir}/spokaneguntrader.com.xml
rm ${dir}/spokaneguntrader.com.xml-00.xml
sed -i '' '1;$d' ${dir}/spokaneguntrader.com-*.xml

echo gobblernation.com.xml
${splitter} -s${size} ${dir}/gobblernation.com.xml
rm ${dir}/gobblernation.com.xml-00.xml
sed -i '' '1;$d' ${dir}/gobblernation.com-*.xml

echo kentuckyarmoryclub.com.xml
${splitter} -s${size} ${dir}/kentuckyarmoryclub.com.xml
rm ${dir}/kentuckyarmoryclub.com.xml-00.xml
sed -i '' '1;$d' ${dir}/kentuckyarmoryclub.com-*.xml

echo airgunadvice.net.xml
${splitter} -s${size} ${dir}/airgunadvice.net.xml
rm ${dir}/airgunadvice.net-00.xml
sed -i '' '1d;$d' ${dir}/airgunadvice.net-*.xml

# Small files

sed '1d;$d' ${dir}/arguntrader.com.xml > ${dir}/arguntrader.com-01.xml
sed '1d;$d' ${dir}/claytargetclassifieds.com.xml > ${dir}/claytargetclassifieds.com-01.xml
sed '1d;$d' ${dir}/henryfirearms.org.xml > ${dir}/henryfirearms.org-01.xml
sed '1d;$d' ${dir}/marauderairrifle.com.xml > ${dir}/marauderairrifle.com-01.xml
sed '1d;$d' ${dir}/newmexicoguntrader.net.xml > ${dir}/newmexicoguntrader.net-01.xml
sed '1d;$d' ${dir}/remingtonsociety.com.xml > ${dir}/remingtonsociety.com-01.xml
sed '1d;$d' ${dir}/rossi-rifleman.com.xml > ${dir}/rossi-rifleman.com-01.xml
sed '1d;$d' ${dir}/silencerforum.com.xml > ${dir}/silencerforum.com-01.xml
sed '1d;$d' ${dir}/tfaonline.org.xml > ${dir}/tfaonline.org-01.xml
sed '1d;$d' ${dir}/treasurestatearms.com.xml > ${dir}/treasurestatearms.com-01.xml
