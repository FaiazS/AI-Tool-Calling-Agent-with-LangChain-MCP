# Defining a Model Context Protocol Server

# Model Context Protocol Server that can Add and Multiply Numbers

#math_server.py

from mcp.server.fastmcp import FastMCP

math_mcp = FastMCP("Math")

@math_mcp.tool()

def add(a: int, b: int) -> int:

  return a + b

@math_mcp.tool()

def multiply(a: int, b: int) -> int:

  return a * b

#Model Context Protocol Server that gets the Weather Conditon of a particular city.

weather_mcp = FastMCP("Weather")

@weather_mcp.tool()

def get_weather_forecast(city : str) -> str:

  return f"The climate for the {city} is sunny"

if __name__  == "__main__":

  weather_mcp.run(transport = "stdio")