"""Priority Living CLI — Agent management subcommands."""

import json
import sys
import urllib.request
import urllib.error

from priority_living.config_manager import load_config


def api_request(endpoint, data=None, method="GET", api_key="", backend="", anon_key=""):
    url = f"{backend}/functions/v1/{endpoint}"
    headers = {
        "Content-Type": "application/json",
        "apikey": anon_key,
        "Authorization": f"Bearer {anon_key}",
        "x-bridge-key": api_key,
    }
    if data:
        body = json.dumps(data).encode("utf-8")
        req = urllib.request.Request(url, data=body, headers=headers, method=method)
    else:
        req = urllib.request.Request(url, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode() if e.fp else ""
        print(f"  ⚠ API error {e.code}: {body[:200]}")
        return None
    except Exception as e:
        print(f"  ⚠ Request failed: {e}")
        return None


def handle_agents(args, default_backend, default_anon_key):
    cfg = load_config()
    api_key = cfg.get("bridge_key")
    backend = cfg.get("backend_url", default_backend)
    anon_key = cfg.get("anon_key", default_anon_key)

    if not api_key:
        print("❌ Bridge key required. Run: pl config set bridge_key pb_xxx")
        sys.exit(1)

    if not args.agents_action or args.agents_action == "list":
        print("📋 Fetching agents...")
        result = api_request(
            "bridge-poll",
            data={"action": "list_agents"},
            method="POST",
            api_key=api_key, backend=backend, anon_key=anon_key,
        )
        if result and "agents" in result:
            agents = result["agents"]
            if not agents:
                print("  No agents bound to this bridge key.")
            else:
                for a in agents:
                    status_icon = "🟢" if a.get("status") == "active" else "⚪"
                    print(f"  {status_icon} {a.get('name', 'Unnamed')} ({a.get('agent_type', '?')}) — {a.get('id', '?')[:8]}...")
        else:
            print("  Could not fetch agents.")

    elif args.agents_action == "start":
        print(f"🚀 Starting local agent worker: {args.agent_id}")
        print("  [Agent worker subprocess not yet implemented — coming in v3.1]")

    elif args.agents_action == "deploy":
        print(f"📦 Deploying agent {args.agent_id} to {args.platform}")
        print("  [Platform deployment not yet implemented — coming in v3.1]")

    else:
        print(f"Unknown agents action: {args.agents_action}")
