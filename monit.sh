#!/bin/bash
tail -f sample.log | \
while read line 
do
  echo $line | egrep '.*load_hostkeys:\s.*'
  if [[ $? == 0 ]]; then 
    sendmail user@example.com < /tmp/email.txt
  fi 
done
