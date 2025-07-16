import os
import uvicorn
from ag_ui_crewai.endpoint import add_crewai_flow_fastapi_endpoint
from fastapi import FastAPI
from dotenv import load_dotenv
from sample_agent.crews.sample_crew.sample_crew import SampleAgentFlow

load_dotenv()

app = FastAPI()
add_crewai_flow_fastapi_endpoint(app, SampleAgentFlow(), "/")

def main():
  """Run the uvicorn server."""
  port = int(os.getenv("PORT", "8000"))
  uvicorn.run(
    "sample_agent.main:app",
    host="0.0.0.0",
    port=port,
    reload=True,
  )

def kickoff():
    agent_flow = SampleAgentFlow()
    agent_flow.kickoff()

def plot():
    agent_flow = SampleAgentFlow()
    agent_flow.plot()

if __name__ == "__main__":
    kickoff()