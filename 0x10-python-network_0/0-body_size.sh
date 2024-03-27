#!/bin/bash
#  sent request 
curl -Is "$1" | grep Content-Length | cut -f2 -d' '
