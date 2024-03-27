#!/bin/bash
# Takes url and send request to it
curl -Is "$1" | grep Content-length | cut -f2 -d' '
