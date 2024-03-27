#!/bin/bash
# Takes url and send request to it
curl -Is "$l" | grep Content-length | cut -f2 -d' '
