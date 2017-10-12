#!/bin/bash
# THIS IS A SCRIPT TO PULL IMPORTANT INFO FROM LOG FILES
NOW=$( date '+%s' )
REF=$(( $NOW - 15*60 ))

while read MONTH DAY HMS A4 ; do

	TIMESTAMP=$(date --date "${MONTH} ${DAY} ${HMS}" '+%s')
	if [[ "$TIMESTAMP" -ge "$REF" ]] ; then
		echo "${MONTH} ${DAY} ${HMS} ${A4}"
			
	fi

done < /var/lib/bind/query.log | grep 'query'
sleep 15
sudo ./log3.sh
