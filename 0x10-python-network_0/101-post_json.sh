#!/bin/bash
# Sending post json request to url
curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2"
