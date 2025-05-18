# Gemini API CLI

This repository includes a simple CLI script to send prompts to the Gemini API.
The script supports Gemini **2.5 Pro** and **2.5 Flash** models. The API key
must be supplied in the `GEMINI_API_KEY` environment variable. These models are
called using their preview endpoints:

```
models/gemini-2.5-pro-preview-05-06
models/gemini-2.5-flash-preview-04-17
```

## Usage

```bash
export GEMINI_API_KEY=your_key_here
python gemini_cli.py "Your prompt here" --model pro   # Use the 2.5 Pro model
python gemini_cli.py "Another prompt" --model flash  # Use the 2.5 Flash model
```

The script prints the JSON response from the API.
