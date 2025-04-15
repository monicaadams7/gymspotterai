import requests

def run_ollama(user_prompt):
    full_prompt = f"""
You are GymSpotterAI, a motivational and smart fitness trainer AI.

A user just said: "{user_prompt}"

Respond like a personal trainer would: 
- Acknowledge what they did (specific exercise, weight, reps).
- Give motivating feedback.
- Suggest what muscle group they trained.
- Keep it short, specific, and friendly.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": full_prompt,
                "stream": False
            }
        )
        return response.json().get("response", "⚠️ LLM returned no response.")
    except Exception as e:
        return f"❌ Ollama API error: {e}"

