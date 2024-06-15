for i in {1..30}
do
    if [ -e Day$i.md ]
    then
        (cat Day$i.md | awk '{gsub("_","")}1') > Day$i.formatted.md
        mv Day$i.formatted.md Day$i.md
    fi
done
