# 📄 AI-Powered RFP Information Extraction System

An industrial-grade AI document intelligence platform designed to extract structured procurement and Request for Proposal (RFP) information from PDF and HTML documents using Large Language Models (LLMs), NLP techniques, and rule-based extraction pipelines.

---

# 🚀 Project Overview

Organizations receive large procurement and tender documents containing critical information such as:

- Bid numbers
- Submission deadlines
- Contact details
- Requirements
- Supporting documents
- Important dates

Manually extracting this information is time-consuming and error-prone.

This system automates the entire extraction workflow using:
- AI-powered document understanding
- Rule-based entity extraction
- Structured JSON generation
- Interactive industrial UI

---

# 🎯 Key Features

## ✅ Intelligent Document Processing
- AI-based extraction using LLMs
- Rule-based extraction for emails, dates, and phone numbers
- Structured JSON response generation

## ✅ Multi-File Upload
- Upload and process multiple RFP documents simultaneously

## ✅ PDF + HTML Support
Supported formats:
- PDF
- HTML
- HTM

## ✅ Modern Enterprise UI
- Dark / Light Theme
- Responsive Streamlit interface
- Upload history sidebar
- Interactive extraction workflow

## ✅ Export Capabilities
- Download extracted data as:
  - JSON
  - CSV

## ✅ Error Handling
- Empty document validation
- Invalid file detection
- AI response validation
- JSON parsing safeguards

## ✅ Performance Optimizations
- Fast PDF parsing using `pdfplumber`
- Streamlit caching
- Partial page extraction for faster processing

---

# 🧠 AI Extraction Pipeline

```text
User Upload
     ↓
PDF / HTML Parsing
     ↓
Text Extraction
     ↓
Rule-Based NLP Extraction
     ↓
LLM Document Analysis
     ↓
Structured JSON Generation
     ↓
JSON / CSV Export

# System Architecture

1. Frontend
        Streamlit
2. Backend
        Python
3. Parsing Layer
        pdfplumber
        BeautifulSoup
4. AI Layer
        OpenAI / OpenRouter APIs
5. Data Processing
        Pandas
        Regex
        JSON

# Technology Stack

| Technology          | Purpose               |
| ------------------- | --------------------- |
| Python              | Core Backend          |
| Streamlit           | Web Interface         |
| OpenAI / OpenRouter | LLM Processing        |
| pdfplumber          | PDF Parsing           |
| BeautifulSoup       | HTML Parsing          |
| Pandas              | CSV Export            |
| Regex               | Rule-Based Extraction |
| JSON                | Structured Output     |

# Supported Documents

The platform supports:
        Procurement documents
        Government RFPs
        Bid documents
        Tender notices
        Vendor proposals
        Addendum documents

# Extracted Information

The system extracts the following structured information:

📌 Basic Extracted Data
        Emails
        Phone Numbers
        Dates
📌 AI Extracted Data
        Document Classification
        Bid Information
        Organization Name
        Submission Deadline
        Contact Information
        Requirements
        Important Dates
        Metadata Summary

# Example JSON Output

{
  "basic_extracted_data": {
    "emails": [
      "procurement@company.com"
    ],
    "phones": [
      "123-456-7890"
    ],
    "dates": [
      "2026-06-01"
    ]
  },

  "llm_output": {

    "document_classification": {
      "document_category": "RFP",
      "document_type": "Procurement"
    },

    "bid_information": {
      "bid_number": "RFP-001",
      "title": "IT Infrastructure Upgrade",
      "organization": "ABC Corporation",
      "submission_deadline": "2026-06-15"
    },

    "contact_information": {
      "name": "John Doe",
      "email": "john@company.com"
    }
  }
}

# ⚙ Installation Guide

1️⃣ Clone Repository
git clone https://github.com/Chandrikar244/ai-rfp-extraction-system.git

2️⃣ Navigate to Project
cd ai-rfp-extraction-system

3️⃣ Create Virtual Environment
python -m venv venv

4️⃣ Activate Environment
Windows
        venv\Scripts\activate
Mac/Linux
        source venv/bin/activate

5️⃣ Install Dependencies
pip install -r requirements.txt

6️⃣ Configure Environment Variables

Create a .env file in the root directory.
OPENROUTER_API_KEY=your_api_key_here

7️⃣ Run Application
streamlit run app.py

📁 Project Structure

ai-rfp-extraction-system/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── pipeline.py
│   │
│   ├── parsers/
│   │   ├── pdf_parser.py
│   │   └── html_parser.py
│   │
│   ├── extractors/
│   │   ├── rule_extractor.py
│   │   └── llm_extractor.py
│
└── temp/

🎨 UI Highlights
Enterprise-style dashboard
Dark / Light theme toggle
Floating sidebar controls
Upload history tracking
JSON visualization
Professional styling

🚀 Future Enhancements
Planned improvements include:

OCR Support
Multi-LLM Integration
RAG Pipeline
Vector Database Integration
Authentication & User Roles
MongoDB Integration
Cloud Deployment
REST API Support
Document Comparison Engine

🧪 Testing Scenarios

The system has been tested using:

Large procurement PDFs
Empty PDFs
Multi-file uploads
HTML bid pages
Invalid documents
Long RFP documents

🔐 Security Considerations

API keys stored using .env
Temporary files ignored via .gitignore
No sensitive credentials stored in repository

⭐ Project Highlights

This project demonstrates:

AI-powered document intelligence
Industrial-grade JSON architecture
Enterprise UI/UX design
Prompt engineering
NLP workflows
Real-world procurement automation
End-to-end AI pipeline development

📜 License

This project is intended for educational and portfolio purposes.