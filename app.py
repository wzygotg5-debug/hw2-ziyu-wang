import os
from google import genai

PROMPT = """
You help organize discussion notes into a clearer summary.

Please write the result in these four parts:

Summary:
Key Points:
Action Items:
Risks or Uncertainty:

Please keep these things in mind:
- Only use information that is in the notes.
- If something is not clear, do not make it sound certain.
- If an idea is only a possibility, do not write it like a final decision.
- Keep the writing clear and easy to follow.
"""

NOTES = """
Client discussion notes:
- The client was not very satisfied with the current timeline
- The pricing part may need some revision
- A revised version may be sent this week
- There will probably be a follow-up discussion on Friday
"""

def main():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY is not set.")
        print('Run this first in Terminal:')
        print('export GEMINI_API_KEY="your_api_key_here"')
        return

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"{PROMPT}\n\nNotes:\n{NOTES}",
    )

    print("\n===== GENERATED OUTPUT =====\n")
    print(response.text)

if __name__ == "__main__":
    main()