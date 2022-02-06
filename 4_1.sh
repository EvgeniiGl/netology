#!/usr/bin/env bash
array_int=({0..4})
array_str=("http://173.194.222.113:80" "http://192.168.0.1:80" "http://87.250.250.242:80")

for i in "${array_int[@]}"
do
    for url in "${array_str[@]}"
    do
      # store the whole response with the status at the and
      HTTP_RESPONSE=$(curl --silent --write-out "HTTPSTATUS:%{http_code}" -m 2 "$url")
      if (($? != 0))
        then echo "$url" >> error.log
        exit;
      fi
      # extract the body
      HTTP_BODY=$(echo $HTTP_RESPONSE | sed -e 's/HTTPSTATUS\:.*//g')
      # extract the status
      HTTP_STATUS=$(echo $HTTP_RESPONSE | tr -d '\n' | sed -e 's/.*HTTPSTATUS://')
      # print the body
      echo "$url" status: "$HTTP_STATUS", response: "$HTTP_BODY" >> curl.log

    done
     sleep 1
done
