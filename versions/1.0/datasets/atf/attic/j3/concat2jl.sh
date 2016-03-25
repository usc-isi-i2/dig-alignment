#!/bin/sh

usage(){
    echo "Usage: $0 filenamePrefix"
    echo "Combine all files whose names begin with filenamePrefix"
    echo "with newlines interspersed between each file's contents."
    echo "Output is written to all_<filenamePrefix>.json"
    exit 1
}

# invoke  usage
# call usage() function if filename not supplied
[[ $# -eq 0 ]] && usage

PATTERN=$1'*'

IFS="$(printf '\n\t')"   # Remove space.
outfile="all_${1}.json"
touch $outfile
#  Correct glob use:
#  Always use for-loop, prefix glob, check if exists file.
for file in ./$PATTERN ; do         # Use ./* ... NEVER bare *
  if [ -e "$file" ] ; then   # Check whether file exists.
      cat "$file" >> $outfile
      echo "" >> $outfile
  fi
done

exit

