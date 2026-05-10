import pdfplumber


# ---------------------------------------------------
# FAST PDF TEXT EXTRACTION
# ---------------------------------------------------

def parse_pdf(pdf_path, max_pages=10):

    text = ""

    try:

        with pdfplumber.open(pdf_path) as pdf:

            total_pages = min(len(pdf.pages), max_pages)

            for i in range(total_pages):

                page = pdf.pages[i]

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:

        text = f"PDF Parsing Error: {str(e)}"

    return text