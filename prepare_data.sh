STAGE=$1

unzip data/repo_archives_$STAGE -d data/repositories_$STAGE

for zipfile in data/repositories_$STAGE/*.zip; do
  unzip "$zipfile" -d "${zipfile%.zip}"
done