#!/bin/sh

# smf_abraxasgacelesox.onion.jl
# phpbb_z34uj4opd3tejafn.onion.jl

DIR=/Users/philpot/Documents/project/dig-alignment/datasets/atf/hg2json
COUNT=5
TEMPFILE=$(mktemp -t "$0")
touch ${TEMPFILE}

head -${COUNT} ${DIR}/smf/smf_abraxasgacelesox.onion.jl | sed -e 's#^{#{"originalfile": "smf_abraxasgacelesox.onion.jl",#' >> ${TEMPFILE}
head -${COUNT} ${DIR}/z34/phpbb_z34uj4opd3tejafn.onion.jl | sed -e 's#^{#{"originalfile": "phpbb_z34uj4opd3tejafn.onion.jl",#' >> ${TEMPFILE}

# add comma after every line
sed -i ".bak1" "s/$/,/g" ${TEMPFILE}

# now delete last comma
sed -i '.bak2' '$s/,$//' ${TEMPFILE}

# now add a [ ] around this.
{ echo "[" ; cat ${TEMPFILE} ; echo "]" ; } > ${DIR}/hg2json-labeled-sample.json

rm ${TEMPFILE}
rm ${TEMPFILE}.bak*