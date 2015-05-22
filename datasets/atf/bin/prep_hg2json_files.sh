#!/bin/sh

DIR=/Users/philpot/Documents/project/dig-alignment/datasets/atf/hg2json

TEMPFILE=$(mktemp -t "$0")
touch ${TEMPFILE}

cat ${DIR}/smf/smf_abraxasgacelesox.onion.jl | sed -e 's#^{#{"originalfile": "smf_abraxasgacelesox.onion.jl",#' >> ${TEMPFILE}
cat ${DIR}/z34/phpbb_z34uj4opd3tejafn.onion.jl | sed -e 's#^{#{"originalfile": "phpbb_z34uj4opd3tejafn.onion.jl",#' >> ${TEMPFILE}

# add comma after every line
sed -i ".bak1" "s/$/,/g" ${TEMPFILE}

# now delete last comma
sed -i '.bak2' '$s/,$//' ${TEMPFILE}

# now add a [ ] around it

{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/labeled_hg2json_all.json

rm ${TEMPFILE}
rm ${TEMPFILE}.bak*
