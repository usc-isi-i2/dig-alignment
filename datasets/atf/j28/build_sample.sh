#!/bin/sh

COUNT=5
TEMPFILE=$(mktemp -t "$0")
touch ${TEMPFILE}

head -${COUNT} airgunadvice.net.json >> ${TEMPFILE}
head -${COUNT} americanpreppersnetwork.net.json >> ${TEMPFILE}
head -${COUNT} arguntrader.com.json >> ${TEMPFILE}
head -${COUNT} claytargetclassifieds.com.json >> ${TEMPFILE}
head -${COUNT} comebackalive.com.json >> ${TEMPFILE}
head -${COUNT} ducksouth.com.json >> ${TEMPFILE}
head -${COUNT} gobblernation.com.json >> ${TEMPFILE}
head -${COUNT} henryfirearms.org.json >> ${TEMPFILE}
head -${COUNT} isthmus.com.json >> ${TEMPFILE}
head -${COUNT} kentuckyarmoryclub.com.json >> ${TEMPFILE}
head -${COUNT} levergunscommunity.com.json >> ${TEMPFILE}
head -${COUNT} marauderairrifle.com.json >> ${TEMPFILE}
head -${COUNT} modernmuzzleloader.com.json >> ${TEMPFILE}
head -${COUNT} newmexicoguntrader.net.json >> ${TEMPFILE}
head -${COUNT} nodakoutdoors.com.json >> ${TEMPFILE}
head -${COUNT} nosler.com.json >> ${TEMPFILE}
head -${COUNT} ohioccwforums.org.json >> ${TEMPFILE}
head -${COUNT} pistolworld.com.json >> ${TEMPFILE}
head -${COUNT} remingtonsociety.com.json >> ${TEMPFILE}
head -${COUNT} rossi-rifleman.com.json >> ${TEMPFILE}
head -${COUNT} silencerforum.com.json >> ${TEMPFILE}
head -${COUNT} spokaneguntrader.com.json >> ${TEMPFILE}
head -${COUNT} texaschlforum.com.json >> ${TEMPFILE}
head -${COUNT} tfaonline.org.json >> ${TEMPFILE}
head -${COUNT} theliberalgunclub.com.json >> ${TEMPFILE}
head -${COUNT} tndeer.com.json >> ${TEMPFILE}
head -${COUNT} treasurestatearms.com.json >> ${TEMPFILE}
head -${COUNT} utahconcealedcarry.com.json >> ${TEMPFILE}
# add comma after every line
sed -i ".bak" "s/$/,/g" ${TEMPFILE}
# now delete last comma

sed -i '.bak2' '$s/,$//' ${TEMPFILE}

# now add a [ ] around this.

{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > j28-sample.json
rm ${TEMPFILE}
