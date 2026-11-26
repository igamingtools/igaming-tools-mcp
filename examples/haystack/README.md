# iGaming Tools + Haystack

Use [iGaming Tools](https://i-gaming.tools/) slot data in [Haystack](https://haystack.deepset.ai/) pipelines and agents
through the free MCP server. No registration, no API key.

The data comes from the providers' official game demos, captured with a headless browser and checked with OCR:
RTP per mode (default, bonus buy, ante bet), volatility, max win, mechanics, features, series and providers.
Also available: regulators, iGaming news, job vacancies and search demand by country.
iGaming Tools is a data API. We don't run games or take bets.

## Install

```bash
pip install -r requirements.txt
```

## Without an LLM

`tools_direct.py` calls `search_slots` and `get_slot` directly and prints every RTP variant of a slot:

```bash
python tools_direct.py
```

## Agent

`agent.py` gives a Haystack `Agent` all 17 MCP tools (needs `OPENAI_API_KEY`, any Haystack chat generator works):

```bash
python agent.py "Which high-volatility Pragmatic Play slots have an ante bet?"
```

The core of it:

```python
from haystack_integrations.tools.mcp import MCPToolset, StreamableHttpServerInfo

toolset = MCPToolset(server_info=StreamableHttpServerInfo(url="https://mcp.i-gaming.tools/mcp"))
agent = Agent(chat_generator=OpenAIChatGenerator(), tools=toolset)
```

## Links

- MCP server: `https://mcp.i-gaming.tools/mcp`
- REST API and docs: https://i-gaming.tools/docs/
- Open dataset: https://doi.org/10.5281/zenodo.24331735
