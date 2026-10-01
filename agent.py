import os
import google.generativeai as genai

# Configure the Gemini client using the environment variable
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Use the recommended free model
model = genai.GenerativeModel('gemini-3.8-flash')

def run_agent(user_query: str) -> str:
    """Sends the user's query to the Gemini AI model."""
    
    # We give the agent a specific "persona" by prepending it to the prompt
    system_persona = (
        "You are an expert DevOps and SRE AI Assistant. Your job is to help "
        "diagnose server issues, explain Docker/Kubernetes commands, and "
        "analyze log files. Keep answers concise and technical.\n\n"
        f"User Query: {user_query}"
    )

    try:
        response = model.generate_content(system_persona)
        return response.text
    except Exception as e:
        return f"Agent Error: Make sure your GEMINI_API_KEY is valid. Details: {str(e)}"