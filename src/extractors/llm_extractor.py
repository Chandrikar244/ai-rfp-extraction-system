import os
import json
import re

from dotenv import load_dotenv
from openai import OpenAI

# ---------------------------------------------------
# LOAD ENV VARIABLES
# ---------------------------------------------------

load_dotenv()

# ---------------------------------------------------
# OPENROUTER CLIENT
# ---------------------------------------------------

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def extract_with_llm(text):

    prompt = f"""
You are an enterprise AI document intelligence system.

Analyze the uploaded document carefully and extract structured information.

Return ONLY valid JSON.

Use this EXACT schema:

{{
    "document_classification": {{
        "document_category": "",
        "document_type": ""
    }},

    "bid_information": {{
        "bid_number": "",
        "title": "",
        "organization": "",
        "issue_date": "",
        "submission_deadline": ""
    }},

    "contact_information": {{
        "name": "",
        "email": "",
        "phone": ""
    }},

    "requirements": [],

    "documents_required": [],

    "important_dates": [],

    "metadata": {{
        "summary": ""
    }}
}}

Rules:
- Return ONLY valid JSON
- No markdown
- No explanations
- No comments
- Ensure arrays contain only values
- Ensure proper commas
- Use double quotes only
- Do not generate invalid JSON

DOCUMENT:
{text[:12000]}
"""

    try:

        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0,
            max_tokens=1500
        )

        content = response.choices[0].message.content.strip()

        # ---------------------------------------------------
        # REMOVE MARKDOWN IF PRESENT
        # ---------------------------------------------------

        content = re.sub(r"```json", "", content)
        content = re.sub(r"```", "", content)

        # ---------------------------------------------------
        # PARSE JSON SAFELY
        # ---------------------------------------------------

        parsed_json = json.loads(content)

        # ---------------------------------------------------
        # ENSURE ARRAYS ARE VALID
        # ---------------------------------------------------

        if not isinstance(parsed_json.get("requirements", []), list):
            parsed_json["requirements"] = []

        if not isinstance(parsed_json.get("documents_required", []), list):
            parsed_json["documents_required"] = []

        if not isinstance(parsed_json.get("important_dates", []), list):
            parsed_json["important_dates"] = []

        return parsed_json

    except json.JSONDecodeError as e:

        return {
            "error": "Invalid JSON returned by model",
            "details": str(e)
        }

    except Exception as e:

        return {
            "error": str(e)
        }