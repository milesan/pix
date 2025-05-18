# Supplement Analysis App

This is a skeletal implementation of an application that manages supplement data using an LLM for evidence gathering.

Features include:
- Generating a supplement list (optionally from LLM).
- Querying an LLM with and without search anchoring.
- Storing analysis results in JSON format.
- Simple user profile to rank recommendations based on the analysis.

The ``call_gemini`` function expects the ``google-generativeai`` package and a
``GOOGLE_API_KEY`` environment variable. If either is missing, a
``RuntimeError`` will be raised and empty JSON objects will be returned.

The repository includes a small example supplement list in `supplements.txt` as a placeholder.

## Usage

```bash
export GOOGLE_API_KEY="your-key"
python -m supplement_app.main
```

If the API key or required library is unavailable, the script will still run but the resulting JSON file will contain empty objects.
