#!/bin/bash
# Trigger Chef run for nodes that haven't checked in within 24h

set -euo pipefail

if [[ ! -f chef_nodes.json ]]; then
  echo "chef_nodes.json not found" >&2
  exit 1
fi

NOW=$(date +%s)
TWENTY_FOUR_HOURS=$((24 * 3600))

for node in $(jq -r '.nodes[] | select(.last_run < (now - 86400)) | .id' chef_nodes.json); do
  echo "Triggering Chef run for $node"
  curl -sSL -X POST \
    https://chef.example.com/apis/infra/nodes/$node/runs \
    -H "api-token: $CHEF_API_TOKEN"
done
