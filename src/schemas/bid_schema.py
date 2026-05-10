from pydantic import BaseModel
from typing import List

# ---------------------------------------------------
# DOCUMENT CLASSIFICATION
# ---------------------------------------------------

class DocumentClassification(BaseModel):
    document_category: str
    document_type: str

# ---------------------------------------------------
# BID INFORMATION
# ---------------------------------------------------

class BidInformation(BaseModel):
    bid_number: str
    title: str
    organization: str
    issue_date: str
    submission_deadline: str

# ---------------------------------------------------
# CONTACT INFORMATION
# ---------------------------------------------------

class ContactInformation(BaseModel):
    name: str
    email: str
    phone: str

# ---------------------------------------------------
# METADATA
# ---------------------------------------------------

class Metadata(BaseModel):
    summary: str

# ---------------------------------------------------
# FINAL SCHEMA
# ---------------------------------------------------

class BidSchema(BaseModel):

    document_classification: DocumentClassification

    bid_information: BidInformation

    contact_information: ContactInformation

    requirements: List[str]

    documents_required: List[str]

    important_dates: List[str]

    metadata: Metadata