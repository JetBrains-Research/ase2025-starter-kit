#!/bin/bash -x

STAGE=$1
LANGUAGE=$2

unzip data/$LANGUAGE-$STAGE -d data/repositories-$LANGUAGE-$STAGE

for zipfile in data/repositories-$LANGUAGE-$STAGE/*.zip; do
  unzip -o "$zipfile" -d "${zipfile%.zip}"
done
