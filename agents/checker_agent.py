import requests

def fact_check(text: str) -> str:
    prompt = (
        "Review the following summary for bias, hallucinations, or missing "
        "context. Suggest improvements:\n\n"
        f"{text}"
    )

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"].strip()
