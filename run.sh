#!/bin/bash

set -e

cmd="python openbazaard.py start -a 127.0.0.1"
if [ -d "/root/.openbazaar" ]; then
    rm -rf /root/.openbazaar;
    echo "deleted old repo";
fi
sed -i "s|#USERNAME = username|USERNAME = get_followers|g" ob.cfg;
sed -i "s|#PASSWORD = password|PASSWORD = get_followers69|g" ob.cfg;

$cmd >/dev/null 2>&1 &

python script/run.py $GUID
