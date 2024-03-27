#!/bin/bash
# Displays url
curl -Is "$1" | grep Allow | cut -c 8-
