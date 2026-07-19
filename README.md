# iGaming Tools — MCP server

**A structured iGaming data source for AI assistants** — slot games (RTP, specs, demos, screenshots), slot providers, regulators, industry news and jobs. Independent data, **not a casino**.

- **Server URL:** `https://mcp.i-gaming.tools/mcp`
- **Transport:** Streamable HTTP · **Auth:** none (free) · **Access:** read-only
- **Full setup guide:** https://i-gaming.tools/docs/mcp/
- **Homepage:** https://i-gaming.tools/

Registered in the official MCP registry as `tools.i-gaming/igaming-data`.

## What you get — 11 read-only tools

| Tool | What you get |
|---|---|
| `search_providers` | Search and list slot providers by name or filter |
| `get_provider` | About, licenses and key metrics for a single provider |
| `list_provider_slots` | All slots released by one provider |
| `search_slots` | Search slots by RTP, bonus buy, jackpot tier, mechanics |
| `get_slot` | Full slot card plus a demo link |
| `list_news` | Latest iGaming news articles |
| `list_jobs` | iGaming job listings |
| `list_regulators` | All licensing regulators we track |
| `get_regulator` | Detail on a single regulator |
| `list_sources` | Where our data comes from |
| `get_provider_demand` | Search-interest / demand stats for a provider |

Every tool is read-only and returns the same public data as our REST API.

## Quick connect

The URL is the same in every client — only *where* you paste it differs.

**Chat apps (paste the URL):** in Claude or ChatGPT open **Settings → Connectors → Add custom connector** and paste `https://mcp.i-gaming.tools/mcp`.

**Coding tools (config file):** e.g. Cursor `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "igaming": { "url": "https://mcp.i-gaming.tools/mcp" }
  }
}
```

Full per-client instructions (VS Code, Claude Code, Gemini, Windsurf, Zed and more): **https://i-gaming.tools/docs/mcp/**

## What it's good for

- **Competitor monitoring** — track new slot releases and provider activity.
- **Content population** — pull structured provider and slot data into your workflow.
- **Demand analytics** — compare search interest across providers over time.
- **Job-market research** — see which studios are hiring and who licenses them.
- **Design reference** — slot mechanics, themes and screenshot metadata.

## Notes

- Free, read-only, no API key.
- A per-IP rate limit applies — heavy or automated use may be throttled.
- Data matches our public REST API. For deeper integration see https://i-gaming.tools/docs/
