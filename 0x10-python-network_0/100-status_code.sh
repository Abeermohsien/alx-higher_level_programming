#!/bin/bash
# Sending reqiest to URL and pass as arg
curl -s -o /dev/null -w "%{http_code}" "$1"
