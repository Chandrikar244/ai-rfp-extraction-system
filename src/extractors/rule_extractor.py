import re

def extract_basic_fields(text):

    emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)

    phones = re.findall(r'\+?\d[\d -]{8,}\d', text)

    dates = re.findall(r'\d{1,2}/\d{1,2}/\d{2,4}', text)

    return {
        "emails": emails,
        "phones": phones,
        "dates": dates
    }