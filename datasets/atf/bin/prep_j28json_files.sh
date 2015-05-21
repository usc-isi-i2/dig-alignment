#!/bin/sh

DIR=/Users/philpot/Documents/project/dig-alignment/datasets/atf/j28json

TEMPFILE=$(mktemp -t "$0")
touch ${TEMPFILE}

cat ${DIR}/airgunadvice.net.json | sed -e 's#^{#{"originalfile": "airgunadvice.net.json",#' >> ${TEMPFILE}
cat ${DIR}/americanpreppersnetwork.net.json | sed -e 's#^{#{"originalfile": "americanpreppersnetwork.net.json",#' >> ${TEMPFILE}
cat ${DIR}/arguntrader.com.json | sed -e 's#^{#{"originalfile": "arguntrader.com.json",#' >> ${TEMPFILE}
cat ${DIR}/claytargetclassifieds.com.json | sed -e 's#^{#{"originalfile": "claytargetclassifieds.com.json",#' >> ${TEMPFILE}
cat ${DIR}/comebackalive.com.json | sed -e 's#^{#{"originalfile": "comebackalive.com.json",#' >> ${TEMPFILE}
cat ${DIR}/ducksouth.com.json | sed -e 's#^{#{"originalfile": "ducksouth.com.json",#' >> ${TEMPFILE}
cat ${DIR}/gobblernation.com.json | sed -e 's#^{#{"originalfile": "gobblernation.com.json",#' >> ${TEMPFILE}
cat ${DIR}/henryfirearms.org.json | sed -e 's#^{#{"originalfile": "henryfirearms.org.json",#' >> ${TEMPFILE}
cat ${DIR}/isthmus.com.json | sed -e 's#^{#{"originalfile": "isthmus.com.json",#' >> ${TEMPFILE}
cat ${DIR}/kentuckyarmoryclub.com.json | sed -e 's#^{#{"originalfile": "kentuckyarmoryclub.com.json",#' >> ${TEMPFILE}
cat ${DIR}/levergunscommunity.com.json | sed -e 's#^{#{"originalfile": "levergunscommunity.com.json",#' >> ${TEMPFILE}
cat ${DIR}/marauderairrifle.com.json | sed -e 's#^{#{"originalfile": "marauderairrifle.com.json",#' >> ${TEMPFILE}
cat ${DIR}/modernmuzzleloader.com.json | sed -e 's#^{#{"originalfile": "modernmuzzleloader.com.json",#' >> ${TEMPFILE}
cat ${DIR}/newmexicoguntrader.net.json | sed -e 's#^{#{"originalfile": "newmexicoguntrader.net.json",#' >> ${TEMPFILE}
cat ${DIR}/nodakoutdoors.com.json | sed -e 's#^{#{"originalfile": "nodakoutdoors.com.json",#' >> ${TEMPFILE}
cat ${DIR}/nosler.com.json | sed -e 's#^{#{"originalfile": "nosler.com.json",#' >> ${TEMPFILE}
cat ${DIR}/ohioccwforums.org.json | sed -e 's#^{#{"originalfile": "ohioccwforums.org.json",#' >> ${TEMPFILE}
cat ${DIR}/pistolworld.com.json | sed -e 's#^{#{"originalfile": "pistolworld.com.json",#' >> ${TEMPFILE}
cat ${DIR}/remingtonsociety.com.json | sed -e 's#^{#{"originalfile": "remingtonsociety.com.json",#' >> ${TEMPFILE}
cat ${DIR}/rossi-rifleman.com.json | sed -e 's#^{#{"originalfile": "rossi-rifleman.com.json",#' >> ${TEMPFILE}
cat ${DIR}/silencerforum.com.json | sed -e 's#^{#{"originalfile": "silencerforum.com.json",#' >> ${TEMPFILE}
cat ${DIR}/spokaneguntrader.com.json | sed -e 's#^{#{"originalfile": "spokaneguntrader.com.json",#' >> ${TEMPFILE}
cat ${DIR}/texaschlforum.com.json | sed -e 's#^{#{"originalfile": "texaschlforum.com.json",#' >> ${TEMPFILE}
cat ${DIR}/tfaonline.org.json | sed -e 's#^{#{"originalfile": "tfaonline.org.json",#' >> ${TEMPFILE}
cat ${DIR}/theliberalgunclub.com.json | sed -e 's#^{#{"originalfile": "theliberalgunclub.com.json",#' >> ${TEMPFILE}
cat ${DIR}/tndeer.com.json | sed -e 's#^{#{"originalfile": "tndeer.com.json",#' >> ${TEMPFILE}
cat ${DIR}/treasurestatearms.com.json | sed -e 's#^{#{"originalfile": "treasurestatearms.com.json",#' >> ${TEMPFILE}
cat ${DIR}/utahconcealedcarry.com.json | sed -e 's#^{#{"originalfile": "utahconcealedcarry.com.json",#' >> ${TEMPFILE}

# add comma after every line
sed -i ".bak1" "s/$/,/g" ${TEMPFILE}

# now delete last comma
sed -i '.bak2' '$s/,$//' ${TEMPFILE}

# now add a [ ] around it

{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_j28json_all.json

rm ${TEMPFILE}
rm ${TEMPFILE}.bak*
