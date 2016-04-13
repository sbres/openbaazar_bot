#!/bin/bash

cmd="python openbazaard.py start -d -a 127.0.0.1"
if [ -d "/root/.openbazaar" ]; then
    rm -rf /root/.openbazaar;
    echo "deleted old repo";
fi
sed -i "s|#USERNAME = username|USERNAME = get_followers|g" ob.cfg;
sed -i "s|#PASSWORD = password|PASSWORD = get_followers69|g" ob.cfg;

$cmd

python run.py $GUID
