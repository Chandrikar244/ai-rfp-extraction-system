import json
import tempfile

from parsers.pdf_parser import parse_pdf
from parsers.html_parser import parse_html

from extractors.rule_extractor import extract_basic_fields
from extractors.llm_extractor import extract_with_llm


def process_uploaded_file(uploaded_file):

    suffix = uploaded_file.name.split('.')[-1]

    # ---------------------------------------------------
    # SAVE TEMP FILE
    # ---------------------------------------------------

    with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{suffix}') as temp_file:

        temp_file.write(uploaded_file.read())

        temp_path = temp_file.name

    text = ""

    # ---------------------------------------------------
    # PARSE FILE
    # ---------------------------------------------------

    if uploaded_file.name.endswith('.pdf'):

        text = parse_pdf(temp_path)

    elif uploaded_file.name.endswith('.html'):

        text = parse_html(temp_path)

    # ---------------------------------------------------
    # EMPTY DOCUMENT VALIDATION
    # ---------------------------------------------------

    if not text or len(text.strip()) < 10:

        return {
            "error": "Empty or unreadable document",
            "message": "The uploaded file does not contain enough readable text for AI extraction."
        }

    # ---------------------------------------------------
    # RULE-BASED EXTRACTION
    # ---------------------------------------------------

    basic_data = extract_basic_fields(text)

    # ---------------------------------------------------
    # LLM EXTRACTION
    # ---------------------------------------------------

    llm_output = extract_with_llm(text)

    # ---------------------------------------------------
    # FINAL RESULT
    # ---------------------------------------------------

    result = {
        "basic_extracted_data": basic_data,
        "llm_output": llm_output,
        "metadata": {
            "processed_file": uploaded_file.name,
            "document_type": uploaded_file.type
        }
    }

    return result