# iGaming Tools — MCP server

**Structured iGaming data for AI assistants** — slot games (RTP variants, specs, mechanics, demos), providers, regulators, industry news and jobs. Independent industry reference data, delivered over the Model Context Protocol.

- **Server URL:** `https://mcp.i-gaming.tools/mcp`
- **Transport:** Streamable HTTP · **Auth:** none (free) · **Access:** read-only
- **Homepage:** https://i-gaming.tools/
- **Full setup guide:** https://i-gaming.tools/docs/mcp/

Registered in the official MCP registry as `tools.i-gaming/igaming-data`.

## What you get — 11 read-only tools

| Tool | What it returns |
| --- | --- |
| `search_providers` | Search and list slot providers by name or filter |
| `get_provider` | Profile, licenses and key metrics for one provider |
| `list_provider_slots` | All slots released by a given provider |
| `search_slots` | Search slots by RTP, bonus buy, jackpot tier or mechanic |
| `get_slot` | Full slot spec — RTP variants, mechanics, bonus buy, demo link |
| `get_slot_demand` | Search-demand for one slot, by country over time |
| `get_provider_demand` | Search-demand for a provider, by country over 24 months |
| `list_news` | Latest iGaming industry news |
| `list_jobs` | iGaming job listings |
| `list_regulators` | Licensing regulators we track |
| `get_regulator` | Detail on a single regulator |

Every tool is read-only and returns the same public data as our REST API.

## Quick connect

The URL is identical in every client — only *where* you paste it differs.

**Chat apps** (paste the URL): in Claude or ChatGPT open **Settings → Connectors → Add custom connector** and paste `https://mcp.i-gaming.tools/mcp`.

**Coding tools** (config file), e.g. Cursor `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "igaming-tools": {
      "url": "https://mcp.i-gaming.tools/mcp"
    }
  }
}
```

Per-client instructions for VS Code, Claude Code, Cline, Gemini, Windsurf and Zed: **https://i-gaming.tools/docs/mcp/**

## What it's good for

- **Competitor monitoring** — track new slot releases and provider activity
- **Content population** — pull structured provider and slot data into your workflow
- **Demand analytics** — compare search interest across providers and titles over time
- **Job-market research** — see which studios are hiring and who licenses them
- **Design reference** — slot mechanics, themes and asset metadata

## Notes

- Free, read-only, no API key
- A per-IP rate limit applies — heavy or automated use may be throttled
- Data matches our public REST API; for deeper integration see https://i-gaming.tools/docs/

## License

MIT
