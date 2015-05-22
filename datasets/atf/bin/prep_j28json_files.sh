#!/bin/sh

DIR=/Users/philpot/Documents/project/dig-alignment/datasets/atf/j28json
TEMPFILE=$(mktemp -t "$0")

touch ${TEMPFILE}
cat ${DIR}/silencerforum.com.json | sed -e 's#^{#{"originalfile": "silencerforum.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_silencerforum.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/airgunadvice.net.json | sed -e 's#^{#{"originalfile": "airgunadvice.net.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" "s/$/,/g" ${TEMPFILE}
# now delete last comma
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_airgunadvice.net.json
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/americanpreppersnetwork.net.json | sed -e 's#^{#{"originalfile": "americanpreppersnetwork.net.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_americanpreppersnetwork.net.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/arguntrader.com.json | sed -e 's#^{#{"originalfile": "arguntrader.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_arguntrader.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/claytargetclassifieds.com.json | sed -e 's#^{#{"originalfile": "claytargetclassifieds.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_claytargetclassifieds.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/comebackalive.com.json | sed -e 's#^{#{"originalfile": "comebackalive.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_comebackalive.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/ducksouth.com.json | sed -e 's#^{#{"originalfile": "ducksouth.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_ducksouth.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/gobblernation.com.json | sed -e 's#^{#{"originalfile": "gobblernation.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_gobblernation.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/henryfirearms.org.json | sed -e 's#^{#{"originalfile": "henryfirearms.org.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_henryfirearms.org.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/isthmus.com.json | sed -e 's#^{#{"originalfile": "isthmus.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_isthmus.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/kentuckyarmoryclub.com.json | sed -e 's#^{#{"originalfile": "kentuckyarmoryclub.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_kentuckyarmoryclub.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/levergunscommunity.com.json | sed -e 's#^{#{"originalfile": "levergunscommunity.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_levergunscommunity.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/marauderairrifle.com.json | sed -e 's#^{#{"originalfile": "marauderairrifle.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_marauderairrifle.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/modernmuzzleloader.com.json | sed -e 's#^{#{"originalfile": "modernmuzzleloader.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_modernmuzzleloader.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/newmexicoguntrader.net.json | sed -e 's#^{#{"originalfile": "newmexicoguntrader.net.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_newmexicoguntrader.net.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/nodakoutdoors.com.json | sed -e 's#^{#{"originalfile": "nodakoutdoors.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_nodakoutdoors.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/nosler.com.json | sed -e 's#^{#{"originalfile": "nosler.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_nosler.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/ohioccwforums.org.json | sed -e 's#^{#{"originalfile": "ohioccwforums.org.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_ohioccwforums.org.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/pistolworld.com.json | sed -e 's#^{#{"originalfile": "pistolworld.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_pistolworld.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/remingtonsociety.com.json | sed -e 's#^{#{"originalfile": "remingtonsociety.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_remingtonsociety.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/rossi-rifleman.com.json | sed -e 's#^{#{"originalfile": "rossi-rifleman.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_rossi-rifleman.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/spokaneguntrader.com.json | sed -e 's#^{#{"originalfile": "spokaneguntrader.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_spokaneguntrader.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/texaschlforum.com.json | sed -e 's#^{#{"originalfile": "texaschlforum.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_texaschlforum.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/tfaonline.org.json | sed -e 's#^{#{"originalfile": "tfaonline.org.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_tfaonline.org.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/theliberalgunclub.com.json | sed -e 's#^{#{"originalfile": "theliberalgunclub.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_theliberalgunclub.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/tndeer.com.json | sed -e 's#^{#{"originalfile": "tndeer.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_tndeer.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/treasurestatearms.com.json | sed -e 's#^{#{"originalfile": "treasurestatearms.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_treasurestatearms.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*


touch ${TEMPFILE}
cat ${DIR}/utahconcealedcarry.com.json | sed -e 's#^{#{"originalfile": "utahconcealedcarry.com.json",#' > ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_utahconcealedcarry.com.json 
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*
