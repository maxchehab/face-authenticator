#!/bin/bash
while true; do
/usr/bin/python3 $HOME/.face-authenticator/authenticate.py > $HOME/.face-authenticator/log.log
done