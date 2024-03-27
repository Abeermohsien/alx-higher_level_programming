#!/bin/bash
# Sending post json request to url
curl -sX POST "$1" -H "Content-Type: aplication/json" -d @"$2"
