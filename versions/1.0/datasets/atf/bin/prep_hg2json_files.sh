#!/bin/sh

DIR=/Users/philpot/Documents/project/dig-alignment/datasets/atf/hg2json

TEMPFILE=$(mktemp -t "$0")
touch ${TEMPFILE}


cat ${DIR}/smf/smf_abraxasgacelesox.onion.json | sed -e 's#^{#{"originalfile": "smf_abraxasgacelesox.onion.json",#' >> ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_smf_abraxasgacelesox.onion.json
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*

touch ${TEMPFILE}
cat ${DIR}/z34/phpbb_z34uj4opd3tejafn.onion.json | sed -e 's#^{#{"originalfile": "phpbb_z34uj4opd3tejafn.onion.json",#' >> ${TEMPFILE}
# add comma after every line
sed -i ".bak1" 's/$/,/g' ${TEMPFILE}
# now delete last comma	
sed -i ".bak2" '$s/,$//' ${TEMPFILE}
# now add a [ ] around it
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_phpbb_z34uj4opd3tejafn.onion.json
rm ${TEMPFILE}
rm ${TEMPFILE}.bak*
