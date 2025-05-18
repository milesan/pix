import os
import json
import urllib.request
import argparse

ENDPOINTS = {
    # Actual endpoints for the preview 2.5 models
    "pro": "models/gemini-2.5-pro-preview-05-06:generateContent",
    "flash": "models/gemini-2.5-flash-preview-04-17:generateContent",
}

API_BASE = "https://generativelanguage.googleapis.com/v1beta/"


def generate_content(prompt: str, model: str = "pro") -> dict:
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise EnvironmentError("GEMINI_API_KEY environment variable not set")
    if model not in ENDPOINTS:
        raise ValueError(f"Unknown model '{model}'. Available: {', '.join(ENDPOINTS)}")

    url = f"{API_BASE}{ENDPOINTS[model]}?key={key}"
    req_body = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode("utf-8")
    req = urllib.request.Request(url, data=req_body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    parser = argparse.ArgumentParser(description="Send a prompt to the Gemini API")
    parser.add_argument("prompt", help="Prompt text to send to the model")
    parser.add_argument("--model", choices=list(ENDPOINTS.keys()), default="pro",
                        help="Model to use: 'pro' or 'flash'. Default is 'pro'.")
    args = parser.parse_args()
    response = generate_content(args.prompt, args.model)
    print(json.dumps(response, indent=2))


if __name__ == "__main__":
    main()
