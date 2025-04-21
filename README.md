# AI-Tool-Calling-Agent-with-LangChain-MCP

# 🧠 AI Tool-Calling Agent with LangChain & MCP

An autonomous AI agent built using **LangChain’s ReAct framework** and **Model Context Protocol (MCP)**. This project demonstrates how an LLM can reason and interact with external tools like math operations and weather forecasting through tool-calling.
---

## 🚀 Project Overview

This project showcases how to build an **AI agent that can "think" and "act"** by:

- **Interpreting user questions**
  
- **Deciding what tool to use**
  
- **Calling external tools** (like a calculator or weather app)
  
- **Returning a final answer**, combining LLM reasoning with tool outputs
  
---

## 🛠️ Features

✅ Tool-calling agent powered by **LangChain ReAct Agent**  
✅ Custom tools defined and served via **MCP Server**  
✅ Uses **asynchronous MCP client** to fetch tool capabilities  
✅ Seamlessly integrates tools like `add`, `multiply`, and `get_weather_forecast(city)`  
✅ Runs on **Groq LLaMA 3 70B Versatile** via `langchain-groq`

---

## 📦 Tech Stack

| Layer            | Tool / Library                              |
|------------------|----------------------------------------------|
| 🧠 LLM           | Groq - LLaMA 3 70B Versatile                 |
| 🧩 Agent         | LangChain - ReAct Agent                     |
| 🔗 Tool Protocol | MCP (Model Context Protocol)                |
| 🔌 Tools Adapter | `langchain_mcp_adapters`                    |
| 🔁 Async Client  | `ClientSession` + `stdio_client` (MCP)      |
| 🐍 Language      | Python 3.10+                                |

---

## 🧪 Example Prompt

What's the current weather condition in Chennai?

Behind the scenes:
The LLM receives the prompt.

It decides to call the get_weather_forecast(city) tool.

Tool gets invoked from the MCP Server.

Result is returned and combined into a natural response by the agent.

How It Works
🔨 Step 1: Define MCP Tools

# math_server.py

@math_mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@math_mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b

🔗 Step 2: Connect AI Agent to MCP Server

async with stdio_client(server_parameters) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        mcp_tools = await load_mcp_tools(session)
        ai_agent = create_react_agent(llm_model, mcp_tools)
        response = await ai_agent.ainvoke({"messages": prompt})

🧭 Running the Project

Start MCP Server:

python mcp_server.py

Run the AI Agent:

python run_agent.py

🧰 Tool Debugging with MCP Inspector (Optional)

Install and run the visual MCP Inspector:

npx mcp inspector

This launches a local web app where one can test the tool interface visually.

✔ Learnings and Key takeaways from Implementing this Simple Agent:

- Understanding of LangChain's ReAct Agent architecture

- Tool-Calling design using Model Context Protocol (MCP)

- Practical use of async programming and agent-to-tool messaging

- Combining LLMs + Tools to create semi-autonomous AI systems

📌 Credits

LangChain

Model Context Protocol

Groq - blazing fast inference

LangChain MCP Adapters
