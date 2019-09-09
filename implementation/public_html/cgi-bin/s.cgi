#!/bin/bash
ID=`echo "$QUERY_STRING" | grep -o "id=[a-zA-Z0-9]*" | cut -d = -f 2`
if [ -n "$ID" ]
then
  URL=`grep "^$ID	" ../../shortcuts/s | head -1 | cut -f 2`
  if [ -n "$URL" ]
  then
    echo "Status: 302 Found"
    echo "Location: $URL"
    echo
  else
    echo "Status: 404 Not Found"
    echo "Content-Type: text/plain"
    echo
    echo "Not Found: $ID"
  fi
fi
