import requests

def generate_report(summary: str, corrections: str) -> str:
    prompt = f"""
Using the summary and fact-checker feedback below, write a polished research report.

Summary:
{summary}

Fact-Checker Feedback:
{corrections}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"].strip()
