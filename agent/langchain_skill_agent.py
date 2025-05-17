"""Simple LangChain agent integrating Intune, Chef and GCP logs."""
from __future__ import annotations

import subprocess
from pathlib import Path

from langchain.agents import Tool, initialize_agent
from langchain.llms import OpenAI


SCRIPT_DIR = Path(__file__).resolve().parent.parent / "scripts"


def _run(cmd: list[str]) -> None:
    """Execute a command and raise if it fails."""
    subprocess.check_call(cmd)


def check_device_compliance() -> str:
    """Call the Intune PowerShell script."""
    _run(["pwsh", str(SCRIPT_DIR / "query-intune.ps1")])
    return "Intune compliance results exported"


def query_chef_nodes() -> str:
    _run(["bash", str(SCRIPT_DIR / "query-chef.sh")])
    return "Chef node data retrieved"


def trigger_chef_remediation() -> str:
    _run(["bash", str(SCRIPT_DIR / "trigger-chef-run.sh")])
    return "Chef remediation triggered"


def fetch_error_logs() -> str:
    _run(["bash", str(SCRIPT_DIR / "fetch-gcp-logs.sh")])
    return "Fetched GCP logs"


def build_agent() -> None:
    llm = OpenAI(temperature=0)
    tools = [
        Tool(name="check_device_compliance", func=lambda _: check_device_compliance(), description="Check Intune compliance"),
        Tool(name="trigger_chef_remediation", func=lambda _: trigger_chef_remediation(), description="Run Chef remediation"),
        Tool(name="fetch_error_logs", func=lambda _: fetch_error_logs(), description="Fetch logs from GCP"),
        Tool(name="query_chef_nodes", func=lambda _: query_chef_nodes(), description="Query Chef nodes"),
    ]
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
    agent.run("List non-compliant devices and remediate via Chef, then fetch GCP logs")


if __name__ == "__main__":
    build_agent()
