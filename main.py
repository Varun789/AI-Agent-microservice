from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import run_agent

# Initialize the FastAPI app
app = FastAPI(
    title="DevOps AI Agent API",
    description="A containerized AI Agent microservice",
    version="1.0.0"
)

# Pydantic models define the structure of our incoming and outgoing JSON data
class AgentRequest(BaseModel):
    query: str

class AgentResponse(BaseModel):
    reply: str

@app.get("/health")
def health_check():

    return {"status": "healthy", "service": "ai-agent"}

@app.post("/chat", response_model=AgentResponse)
def chat_with_agent(request: AgentRequest):
    if not request.query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    # Call the agent logic from agent.py
    ai_reply = run_agent(request.query)
    
    return AgentResponse(reply=ai_reply)