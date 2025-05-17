# MCP Integration Example

This repository demonstrates how Azure MCP can orchestrate tasks across Microsoft Graph/Intune, Chef Automate and GCP Logging. The sample includes a CI pipeline, scripts and a minimal LangChain agent.

## Pipeline

The `mcp_integration_pipeline.yaml` file contains an Azure DevOps pipeline that executes four steps:

1. **Query Intune** – Retrieves non-compliant devices using Microsoft Graph.
2. **Query Chef** – Downloads Chef node states.
3. **Trigger Chef Remediation** – Starts a Chef run if the last run exceeds 24 hours.
4. **Fetch GCP Logs** – Reads recent error logs from Cloud Logging.

Required variables:

- `GRAPH_TOKEN` – OAuth token for Microsoft Graph.
- `CHEF_API_TOKEN` – API token for Chef Automate.
- `GOOGLE_APPLICATION_CREDENTIALS` – GCP service account JSON.

## LangChain Agent

A basic agent implementation in `agent/langchain_skill_agent.py` wires these tasks together so you can issue natural language prompts.

Run it with:

```bash
pip install -r requirements.txt
python agent/langchain_skill_agent.py
```

The agent expects the same environment variables used in the pipeline
(`GRAPH_TOKEN`, `CHEF_API_TOKEN` and `GOOGLE_APPLICATION_CREDENTIALS`) to be
available so the scripts can authenticate with each service.

## Docker

A `Dockerfile` is provided for local development. It installs PowerShell, Azure CLI and Google Cloud CLI so you can run the scripts locally.

Build the image:

```bash
docker build -t mcp-integration .
```

Then start an interactive shell:

```bash
docker run -it mcp-integration
```
