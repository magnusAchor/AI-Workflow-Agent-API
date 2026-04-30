import os
from dotenv import load_dotenv
from openrouter import OpenRouter

load_dotenv()

client = OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# Ordered fallback models (best → worst or fastest → slowest)
MODELS = [
    "poolside/laguna-xs.2:free",
    "poolside/laguna-m.1:free",
    "google/gemma-4-26b-a4b-it:free",
    "nvidia/nemotron-3-super-120b-a12b:free",
    "minimax/minimax-m2.5:free",
    "liquid/lfm-2.5-1.2b-thinking:free",
    "qwen/qwen3-next-80b-a3b-instruct:free",
    "openai/gpt-oss-120b:free",
    "openai/gpt-oss-20b:free",
    "z-ai/glm-4.5-air:free"
]


def call_llm(prompt: str) -> str:
    errors = []

    for model in MODELS:
        try:
            print(f"[LLM] Trying model: {model}")

            response = client.chat.send(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            # Defensive parsing (avoid crashes if structure changes)
            if response and response.choices:
                content = response.choices[0].message.content
                if content:
                    print(f"[LLM] Success with: {model}")
                    return content

            errors.append(f"{model}: Empty response")

        except Exception as e:
            error_msg = f"{model}: {str(e)}"
            print(f"[LLM ERROR] {error_msg}")
            errors.append(error_msg)

    # If ALL models fail
    return {
        "error": "All LLM providers failed",
        "details": errors
    }