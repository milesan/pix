"""Supplement Analysis App

This script provides a minimal skeleton for generating supplement data
using LLM queries. The ``call_gemini`` function attempts to invoke the
Gemini 2.5 API via the ``google-generativeai`` client. If the library
or an API key is unavailable, a ``RuntimeError`` is raised.
"""
from dataclasses import dataclass, asdict
from typing import List, Dict, Any
import json


@dataclass
class SupplementResult:
    supplement: str
    efficacy: int | None = None
    safety: int | None = None
    evidence_strength: int | None = None
    bioavailability: int | None = None
    cost_eur_per_day: int | None = None
    regulatory_status_eu: str | None = None
    novelty_index: int | None = None
    stack_synergy: int | None = None
    rapid_onset: int | None = None
    psychoactive_intensity: int | None = None
    dosing_elasticity: int | None = None
    diy_formulation: int | None = None
    mitochondrial_drive: int | None = None
    autophagy_trigger: int | None = None
    hormetic_stress: int | None = None
    epigenetic_modulation: int | None = None
    snp_leverage: int | None = None
    anecdotal_roi: int | None = None
    forum_buzz: int | None = None
    key_human_outcomes: List[str] | None = None
    primary_mechanisms: List[str] | None = None
    contraindications: List[Dict[str, Any]] | None = None
    confidence: int | None = None
    citations: List[str] | None = None


def call_gemini(prompt: str, search: bool = False) -> str:
    """Call the Gemini 2.5 API via the ``google-generativeai`` client.

    Parameters
    ----------
    prompt:
        Full prompt to send to the model. A system prompt should be
        prepended by the caller if desired.
    search:
        Whether to use the search-anchored model variant (Flash) or the
        standard model.

    Returns
    -------
    str
        The text content returned by Gemini.
    """
    try:
        import os
        import google.generativeai as genai
    except Exception as exc:  # pragma: no cover - import error
        raise RuntimeError("google-generativeai library is required") from exc

    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY environment variable not set")

    genai.configure(api_key=api_key)
    model_name = (
        "models/gemini-1.5-flash-latest" if search else "models/gemini-1.5-pro-latest"
    )
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    return response.text


def analyze_supplement(name: str) -> SupplementResult:
    """Query the LLM twice (with and without search) and merge results."""
    system_prompt = (
        "You are a transdisciplinary biohacking evidence-engine."
    )

    user_prompt = f"Evaluate {name} and return JSON"

    # Placeholder logic; call_gemini should return the JSON string
    # Without search
    try:
        base_response = call_gemini(system_prompt + user_prompt, search=False)
    except (NotImplementedError, RuntimeError):
        base_response = '{}'

    # With search anchoring
    try:
        search_response = call_gemini(system_prompt + user_prompt, search=True)
    except (NotImplementedError, RuntimeError):
        search_response = '{}'

    # Merge or select better response
    data = json.loads(search_response or base_response)
    if "supplement" not in data:
        data["supplement"] = name
    return SupplementResult(**data)


def save_results(results: List[SupplementResult], path: str) -> None:
    with open(path, 'w') as f:
        json.dump([asdict(r) for r in results], f, indent=2)


def main():
    supplements = [
        "Creatine Monohydrate",
        "Ashwagandha",
        "Resveratrol",
    ]

    results = []
    for name in supplements:
        result = analyze_supplement(name)
        results.append(result)

    save_results(results, 'supplement_results.json')


if __name__ == '__main__':
    main()
