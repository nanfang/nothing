#!/bin/bash
while read line
do
        FILENAME=$(echo "$line" | cut -f 1 )
        URL=$(echo "$line" | cut -f 2 )
        echo $FILENAME
        #wget $URL -O "'$FILENAME'"
done
