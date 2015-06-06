#! /bin/bash

result=`echo "atrail brief 0 9999" | wc | grep "1"`

echo $result

result2=`echo $result | sed -n -e 's/\([0-9]{2}\)/\1/p'`

echo $result2