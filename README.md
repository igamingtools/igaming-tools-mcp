# iGaming Tools — MCP server

**Structured iGaming data for AI assistants** — slot games (RTP variants, specs, mechanics, demos), providers, regulators, industry news and jobs. Independent industry reference data, delivered over the Model Context Protocol.

- **Server URL:** `https://mcp.i-gaming.tools/mcp`
- **Transport:** Streamable HTTP · **Auth:** none (free) · **Access:** read-only
- **Homepage:** https://i-gaming.tools/
- **Full setup guide:** https://i-gaming.tools/docs/mcp/

Registered in the official MCP registry as `tools.i-gaming/igaming-data`.

## What you get — 17 read-only tools

| Tool | What it returns |
| --- | --- |
| `search_providers` | Search and list slot providers (casino game studios) |
| `get_provider` | Full provider profile — firmographics, licensing, offices, counts |
| `get_provider_demand` | Provider demand snapshot — metrics and top slots |
| `list_provider_slots` | All slots by a given provider, with structural filters |
| `search_slots` | Search and list public slots |
| `get_slot` | Full slot profile — RTP/volatility/mechanics, spec sheet, assets |
| `get_slot_demand` | Per-slot search demand — aggregate + country×month matrix |
| `list_series` | Slot series (game families, e.g. Big Bass, Wolf Gold) with aggregate stats |
| `get_series` | Series summary — RTP/max-win/year ranges, volatility mix, slot roster |
| `list_themes` | Slot themes (Egyptian, Ancient Rome, Fantasy…) with slot counts and aliases |
| `list_features` | Slot features (Bonus Buy, Cluster Pays, Ante Bet…) with slot counts and aliases |
| `get_demand_cut` | Which slots are searched in a given country, ranked by 12-month volume |
| `list_regulators` | Search/list regulators (UKGC, MGA, GGL, ANJ, etc.) |
| `get_regulator` | Full regulator profile — jurisdiction, authority, statutory basis |
| `list_news` | iGaming industry news articles |
| `list_jobs` | iGaming job vacancies |
| `list_sources` | Active news sources (hosts) with brand attribution |

All tools are read-only and return the same public data as our REST API.

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
