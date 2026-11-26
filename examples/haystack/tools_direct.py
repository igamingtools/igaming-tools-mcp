"""Call iGaming Tools MCP tools from Haystack without an LLM.

No API key needed: the MCP server at https://mcp.i-gaming.tools/mcp is free and open.
Run: pip install -r requirements.txt && python tools_direct.py
"""
import json

from haystack_integrations.tools.mcp import MCPToolset, StreamableHttpServerInfo

toolset = MCPToolset(
    server_info=StreamableHttpServerInfo(url="https://mcp.i-gaming.tools/mcp"),
    tool_names=["search_slots", "get_slot"],
    eager_connect=True,
)
tools = {tool.name: tool for tool in toolset.tools}


def payload(result) -> dict:
    """MCP returns a JSON string with a list of content blocks; take the first text block."""
    return json.loads(json.loads(result)["content"][0]["text"])


# Slots with a bonus buy whose default RTP is at least 96.5%
found = payload(tools["search_slots"].invoke(search="olympus", has_bonus_buy="true", rtp_min=96.5, page_size=5))
for slot in found["results"]:
    print(f'{slot["name"]:32} {slot["provider"]["name"]:16} RTP {slot["rtp_default"]}  {slot["volatility"]}')

# One slot in full: every RTP variant captured from the provider's demo
slot = payload(tools["get_slot"].invoke(slug=found["results"][0]["slug"]))["data"]
print(f'\n{slot["name"]}: RTP by mode')
for v in slot["rtp_variants"]:
    print(f'  {v["variant"]:14} {v["rtp"]}  {v["condition_note"]}')
