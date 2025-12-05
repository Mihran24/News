import os
import time
from google import genai
from google.genai import types
import config

# To run this code, install the required dependency:
# pip install google-genai

def generate_response(prompt, temperature=0.5):
    """Generate a response from Gemini API with a specified temperature."""
    try:
        # Initialize the client with API key from config module
        client = genai.Client(api_key=config.GEMINI_API_KEY)

        # Create the content structure
        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=prompt),
                ],
            ),
        ]

        # Configure generation parameters
        generate_content_config = types.GenerateContentConfig(
            temperature=temperature,
            response_mime_type="text/plain",
        )
        response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=contents,
        config=generate_content_config,
        )

        return response.text
    except Exception as e:
        return f"Error generating response:{str(e)}"

def temperature_prompt_activity():
    """Interactive activity to explore temperature settings and instruction-based prompts."""

    print("=" * 80)

    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE & INSTRUCTION-BASED PROMPTS")

    print("=" * 80)

    print("\nIn this activity, we'll explore:")

    print("1. How temperature affects AI creativity and randomness")

    print("2. How instruction-based prompts can control AI outputs")


    # Part 1: Temperature Exploration

    print("\n" + "-" * 40)

    print("PART 1: TEMPERATURE EXPLORATION")

    print("-" * 40)


instructions = [

f"Summarize the key facts about {topic} in 3-4 sentences.",

f"Explain {topic} as if I'm a 10-year-old child.",

f"Write a pro/con list about {topic}.",

f"Create a fictional news headline from the year 2050 about {topic}."

]

for i, in instruction in enumerate(instructions,1):
    print(f"\n--- INSTRUCTION {i}, {instructions} ---- ")
    print(response)
    time.sleep(1)