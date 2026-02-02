import requests
import os

COPILOT_API_KEY = os.getenv("COPILOT_API_KEY")
COPILOT_ENDPOINT = "https://api.copilot.microsoft.com/v1/chat/completions"

def generate_test_code(test_description: str) -> str:
    prompt = f"""
    Convert this test case into Python Playwright code with pytest:
    {test_description}
    """
    headers = {
        "Authorization": f"Bearer {COPILOT_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4o-mini",   # or whichever Copilot model you’re using
        "messages": [
            {"role": "system", "content": "You are an assistant that generates Playwright test automation code in Python with pytest."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500
    }
    response = requests.post(COPILOT_ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()