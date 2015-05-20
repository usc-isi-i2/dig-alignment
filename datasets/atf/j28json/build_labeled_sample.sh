#!/bin/sh

COUNT=5
TEMPFILE=$(mktemp -t "$0")
touch ${TEMPFILE}

head -${COUNT} airgunadvice.net.json | sed -e 's#^{#{"originalfile": "airgunadvice.net.json",#' >> ${TEMPFILE}
head -${COUNT} americanpreppersnetwork.net.json | sed -e 's#^{#{"originalfile": "americanpreppersnetwork.net.json",#' >> ${TEMPFILE}
head -${COUNT} arguntrader.com.json | sed -e 's#^{#{"originalfile": "arguntrader.com.json",#' >> ${TEMPFILE}
head -${COUNT} claytargetclassifieds.com.json | sed -e 's#^{#{"originalfile": "claytargetclassifieds.com.json",#' >> ${TEMPFILE}
head -${COUNT} comebackalive.com.json | sed -e 's#^{#{"originalfile": "comebackalive.com.json",#' >> ${TEMPFILE}
head -${COUNT} ducksouth.com.json | sed -e 's#^{#{"originalfile": "ducksouth.com.json",#' >> ${TEMPFILE}
head -${COUNT} gobblernation.com.json | sed -e 's#^{#{"originalfile": "gobblernation.com.json",#' >> ${TEMPFILE}
head -${COUNT} henryfirearms.org.json | sed -e 's#^{#{"originalfile": "henryfirearms.org.json",#' >> ${TEMPFILE}
head -${COUNT} isthmus.com.json | sed -e 's#^{#{"originalfile": "isthmus.com.json",#' >> ${TEMPFILE}
head -${COUNT} kentuckyarmoryclub.com.json | sed -e 's#^{#{"originalfile": "kentuckyarmoryclub.com.json",#' >> ${TEMPFILE}
head -${COUNT} levergunscommunity.com.json | sed -e 's#^{#{"originalfile": "levergunscommunity.com.json",#' >> ${TEMPFILE}
head -${COUNT} marauderairrifle.com.json | sed -e 's#^{#{"originalfile": "marauderairrifle.com.json",#' >> ${TEMPFILE}
head -${COUNT} modernmuzzleloader.com.json | sed -e 's#^{#{"originalfile": "modernmuzzleloader.com.json",#' >> ${TEMPFILE}
head -${COUNT} newmexicoguntrader.net.json | sed -e 's#^{#{"originalfile": "newmexicoguntrader.net.json",#' >> ${TEMPFILE}
head -${COUNT} nodakoutdoors.com.json | sed -e 's#^{#{"originalfile": "nodakoutdoors.com.json",#' >> ${TEMPFILE}
head -${COUNT} nosler.com.json | sed -e 's#^{#{"originalfile": "nosler.com.json",#' >> ${TEMPFILE}
head -${COUNT} ohioccwforums.org.json | sed -e 's#^{#{"originalfile": "ohioccwforums.org.json",#' >> ${TEMPFILE}
head -${COUNT} pistolworld.com.json | sed -e 's#^{#{"originalfile": "pistolworld.com.json",#' >> ${TEMPFILE}
head -${COUNT} remingtonsociety.com.json | sed -e 's#^{#{"originalfile": "remingtonsociety.com.json",#' >> ${TEMPFILE}
head -${COUNT} rossi-rifleman.com.json | sed -e 's#^{#{"originalfile": "rossi-rifleman.com.json",#' >> ${TEMPFILE}
head -${COUNT} silencerforum.com.json | sed -e 's#^{#{"originalfile": "silencerforum.com.json",#' >> ${TEMPFILE}
head -${COUNT} spokaneguntrader.com.json | sed -e 's#^{#{"originalfile": "spokaneguntrader.com.json",#' >> ${TEMPFILE}
head -${COUNT} texaschlforum.com.json | sed -e 's#^{#{"originalfile": "texaschlforum.com.json",#' >> ${TEMPFILE}
head -${COUNT} tfaonline.org.json | sed -e 's#^{#{"originalfile": "tfaonline.org.json",#' >> ${TEMPFILE}
head -${COUNT} theliberalgunclub.com.json | sed -e 's#^{#{"originalfile": "theliberalgunclub.com.json",#' >> ${TEMPFILE}
head -${COUNT} tndeer.com.json | sed -e 's#^{#{"originalfile": "tndeer.com.json",#' >> ${TEMPFILE}
head -${COUNT} treasurestatearms.com.json | sed -e 's#^{#{"originalfile": "treasurestatearms.com.json",#' >> ${TEMPFILE}
head -${COUNT} utahconcealedcarry.com.json | sed -e 's#^{#{"originalfile": "utahconcealedcarry.com.json",#' >> ${TEMPFILE}
# add comma after every line
sed -i ".bak" "s/$/,/g" ${TEMPFILE}
# now delete last comma

sed -i '.bak2' '$s/,$//' ${TEMPFILE}

# now add a [ ] around this.

{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > j28-labeled-sample.json
rm ${TEMPFILE}
