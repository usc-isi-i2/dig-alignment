#!/bin/sh

DIR=/Users/philpot/Documents/project/dig-alignment/datasets/atf/j28json
COUNT=5
TEMPFILE=$(mktemp -t "$0")
touch ${TEMPFILE}

head -${COUNT} ${DIR}/airgunadvice.net.json | sed -e 's#^{#{"originalfile": "airgunadvice.net.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/americanpreppersnetwork.net.json | sed -e 's#^{#{"originalfile": "americanpreppersnetwork.net.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/arguntrader.com.json | sed -e 's#^{#{"originalfile": "arguntrader.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/claytargetclassifieds.com.json | sed -e 's#^{#{"originalfile": "claytargetclassifieds.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/comebackalive.com.json | sed -e 's#^{#{"originalfile": "comebackalive.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/ducksouth.com.json | sed -e 's#^{#{"originalfile": "ducksouth.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/gobblernation.com.json | sed -e 's#^{#{"originalfile": "gobblernation.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/henryfirearms.org.json | sed -e 's#^{#{"originalfile": "henryfirearms.org.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/isthmus.com.json | sed -e 's#^{#{"originalfile": "isthmus.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/kentuckyarmoryclub.com.json | sed -e 's#^{#{"originalfile": "kentuckyarmoryclub.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/levergunscommunity.com.json | sed -e 's#^{#{"originalfile": "levergunscommunity.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/marauderairrifle.com.json | sed -e 's#^{#{"originalfile": "marauderairrifle.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/modernmuzzleloader.com.json | sed -e 's#^{#{"originalfile": "modernmuzzleloader.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/newmexicoguntrader.net.json | sed -e 's#^{#{"originalfile": "newmexicoguntrader.net.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/nodakoutdoors.com.json | sed -e 's#^{#{"originalfile": "nodakoutdoors.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/nosler.com.json | sed -e 's#^{#{"originalfile": "nosler.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/ohioccwforums.org.json | sed -e 's#^{#{"originalfile": "ohioccwforums.org.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/pistolworld.com.json | sed -e 's#^{#{"originalfile": "pistolworld.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/remingtonsociety.com.json | sed -e 's#^{#{"originalfile": "remingtonsociety.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/rossi-rifleman.com.json | sed -e 's#^{#{"originalfile": "rossi-rifleman.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/silencerforum.com.json | sed -e 's#^{#{"originalfile": "silencerforum.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/spokaneguntrader.com.json | sed -e 's#^{#{"originalfile": "spokaneguntrader.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/texaschlforum.com.json | sed -e 's#^{#{"originalfile": "texaschlforum.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/tfaonline.org.json | sed -e 's#^{#{"originalfile": "tfaonline.org.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/theliberalgunclub.com.json | sed -e 's#^{#{"originalfile": "theliberalgunclub.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/tndeer.com.json | sed -e 's#^{#{"originalfile": "tndeer.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/treasurestatearms.com.json | sed -e 's#^{#{"originalfile": "treasurestatearms.com.json",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/utahconcealedcarry.com.json | sed -e 's#^{#{"originalfile": "utahconcealedcarry.com.json",#' >> ${TEMPFILE}

# add comma after every line
sed -i ".bak1" "s/$/,/g" ${TEMPFILE}

# now delete last comma
sed -i '.bak2' '$s/,$//' ${TEMPFILE}

# now add a [ ] around this.
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/j28json-labeled-sample.json

rm ${TEMPFILE}
rm ${TEMPFILE}.bak*
