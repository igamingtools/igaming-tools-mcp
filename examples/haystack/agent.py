"""A Haystack Agent that answers questions about slot games with iGaming Tools data.

The agent gets all 17 tools of the free iGaming Tools MCP server (slots, RTP variants,
providers, series, regulators, news, jobs, search demand). Needs OPENAI_API_KEY.
Run: pip install -r requirements.txt && python agent.py "your question"
"""
import sys

from haystack.components.agents import Agent
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.dataclasses import ChatMessage
from haystack_integrations.tools.mcp import MCPToolset, StreamableHttpServerInfo

toolset = MCPToolset(server_info=StreamableHttpServerInfo(url="https://mcp.i-gaming.tools/mcp"))

agent = Agent(
    chat_generator=OpenAIChatGenerator(),
    tools=toolset,
    system_prompt=(
        "You answer questions about online slot games using the iGaming Tools tools. "
        "Look up data instead of guessing, and say which slot or provider each number comes from."
    ),
)

question = " ".join(sys.argv[1:]) or "Which Gates of Olympus games have a different RTP when you buy the bonus?"
result = agent.run(messages=[ChatMessage.from_user(question)])
print(result["messages"][-1].text)
