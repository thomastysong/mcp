#!/bin/bash
# Fetch Chef Automate node states

set -euo pipefail

curl -sSL -X GET \
  https://chef.example.com/apis/infra/nodes \
  -H "api-token: $CHEF_API_TOKEN" \
  -o chef_nodes.json

echo "Chef node data saved to chef_nodes.json"
