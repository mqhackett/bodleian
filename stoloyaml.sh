#!/bin/bash
curl -H "Accept: application/vnd.github.v3+json" https://api.github.com/search/code\?q=language:yaml+org:stolostron
