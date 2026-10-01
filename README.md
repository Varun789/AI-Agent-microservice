# Containerized AI Agent Microservice 🤖🐳

A production-ready blueprint for deploying an AI Agent as a microservice. This project wraps a custom-prompted LLM (Large Language Model) inside a **FastAPI** web server and packages the entire application into a **Docker** container.

Currently, the agent is configured with a **DevOps/SRE persona** to assist with infrastructure queries, but the architecture can be adapted for any AI tool-calling agent.

## 🏗️ Architecture
1. **Model Layer (`agent.py`)**: Uses the OpenAI API to process queries.
2. **API Layer (`main.py`)**: A FastAPI application that exposes the agent via a `/chat` REST endpoint, handles JSON validation, and provides a `/health` endpoint for infrastructure monitoring.
3. **Infrastructure Layer (`Dockerfile` / `docker-compose.yml`)**: Containerizes the application so it can be deployed consistently anywhere (AWS, GCP, Kubernetes, or a local server).

## 🚀 How to Run

### Prerequisites
* Docker and Docker Compose installed.
* An Gemini API Key 

### Step 1: Set your API Key
Create .env folder and 
```GEMINI_API_KEY=your-actual-api-key-here
