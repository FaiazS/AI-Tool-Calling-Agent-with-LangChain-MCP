from mcp import ClientSession

from mcp import StdioServerParameters

from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools

from langgraph.prebuilt import create_react_agent

from langchain_groq import ChatGroq

from dotenv import load_dotenv

import os

import asyncio

load_dotenv()

llm_model = ChatGroq(
  
  model = "llama-3-3-70b-versatile",

  api_key = os.getenv("API_KEY")

)

llm_model_response = llm_model.invoke("Explain Model Context Protocol")

print(llm_model_response.content)

server_parameters = StdioServerParameters(

                                         command ="python",

                                         args = ["../Model_Context_Protocol/mcp_server.py"]
)
async def run_ai_agent():
  
  async with stdio_client(server_parameters) as (read , write) :

      async with ClientSession(read, write) as session:

       #Initializing connection between the MCP Server and MCP Client
         await session.initialize()

         #Getting tools from the MCP Server

         mcp_tools = await load_mcp_tools(session)  

         #Define and run the AI agent

         ai_agent = create_react_agent(llm_model, mcp_tools)

         ai_agent_response = await ai_agent.ainvoke({"messages" : "What's the current weather condition in Chennai?"})

         return ai_agent_response
   
  
if __name__ == "__main__":
  
 ai_agent_result = asyncio.run(run_ai_agent())

print(ai_agent_result['messages'][2].content)
