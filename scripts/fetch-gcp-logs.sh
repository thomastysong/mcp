#!/bin/bash
# Read recent error logs from GCP Logging

set -euo pipefail

echo "$GOOGLE_APPLICATION_CREDENTIALS" > creds.json

gcloud auth activate-service-account --key-file=creds.json

gcloud logging read 'severity>=ERROR' --limit=5
