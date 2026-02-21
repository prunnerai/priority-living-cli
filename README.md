# Priority Living CLI

> Sovereign AI command & control for your local machine.

## Features

- 🖥 **Bridge Worker** — Connect your machine to the Priority Living platform
- 🤖 **Agent Management** — List, start, and deploy agents locally
- 🧠 **Model Operations** — Download, run inference, and serve HuggingFace models
- 📊 **System Diagnostics** — GPU detection, dependency checks, connectivity tests
- ⚙️ **Local Config** — Persistent configuration in `~/.priority-living/`
- 📡 **Streaming Output** — Real-time command output to the cloud dashboard
- 🛡 **Safety Guards** — Blocks dangerous commands automatically

## Quick Start

```bash
# 1. Clone and install
git clone https://github.com/YOUR_USERNAME/priority-living-cli.git
cd priority-living-cli
pip install -e .

# 2. Configure
pl config set bridge_key pb_YOUR_KEY

# 3. Check status
pl status

# 4. Start the bridge
pl bridge start
```

## Commands

| Command | Description |
|---------|-------------|
| `pl bridge start` | Start the bridge worker |
| `pl agents list` | List bound agents |
| `pl agents start <id>` | Start a local agent worker |
| `pl models download <name>` | Download a HuggingFace model |
| `pl models infer <name> -p "..."` | Run local inference |
| `pl models serve <name>` | Start local model API server |
| `pl status` | Show system status |
| `pl diagnose` | Deep diagnostic scan |
| `pl config set <key> <val>` | Set config value |
| `pl config get <key>` | Get config value |

## AI Features (Optional)

For model download, inference, and serving:

```bash
pip install priority-living-cli[ai]
# or
pip install torch transformers huggingface_hub
```

## Configuration

Config is stored in `~/.priority-living/config.json`:

| Key | Description | Default |
|-----|-------------|---------|
| `bridge_key` | Your bridge API key (pb_...) | — |
| `backend_url` | Priority Living backend URL | auto |
| `poll_interval` | Bridge poll interval (seconds) | 3 |
| `auto_restart` | Auto-restart on crash | true |
| `default_model_path` | Model storage directory | ~/.priority-living/models |

## Security

- Dangerous commands (`rm -rf /`, `mkfs`, etc.) are automatically blocked
- Output truncated at 50KB
- Commands timeout after 5 minutes
- Bridge keys are scoped to your account
- Errors are reported to the cloud for diagnostics

## License

MIT — Built with ❤️ by Priority Living Labs
