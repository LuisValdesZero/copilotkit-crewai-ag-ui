from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class GetWeatherInput(BaseModel):
    """Input schema for GetWeatherTool."""

    location: str = Field(..., description="The city and state, e.g. San Francisco, CA")


class GetWeatherTool(BaseTool):
    name: str = "get_weather"
    description: str = (
        "Get the current weather in a given location"
    )
    args_schema: Type[BaseModel] = GetWeatherInput

    def _run(self, location: str) -> str:
        return f"The weather for {location} is 21 degrees Celsius, clear skies, 45% humidity, 5 mph wind, and feels like 72 degrees." 