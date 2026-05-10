import streamlit as st 
import json 
import sys 
import os 
import pandas as pd 
import time 
from datetime import datetime 

sys.path.append(os.path.abspath("src"))

from pipeline import process_uploaded_file 

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI RFP Extraction System",
    page_icon="📄",
    layout="wide"
)

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "upload_history" not in st.session_state:
    st.session_state.upload_history = []

if "total_processed" not in st.session_state:
    st.session_state.total_processed = 0

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:
    dark_mode = st.toggle("🌙 Dark Mode", value=False)

st.set_page_config(
    page_title="AI RFP Extraction System",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# DARK THEME
# ---------------------------------------------------

if dark_mode:

    st.markdown("""
    <style>

    /* REMOVE TOP HEADER SPACE */

    [data-testid="stHeader"] {
        background: transparent;
        height: 0px;
    }

    /* HIDE DEPLOY BUTTON */

    .stDeployButton {
        display: none !important;
    }

    /* MAIN APP */

    .stApp {
        background: linear-gradient(to bottom right, #0F172A, #111827);
        color: #E2E8F0;
    }

    /* MAIN CONTENT */

    .block-container {
        padding-top: 2rem !important;
    }

    /* SIDEBAR */

    section[data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #334155;
    }

    /* TEXT */

    h1, h2, h3, h4, h5, h6,
    p, label, div, span {
        color: #E2E8F0 !important;
    }

    /* FILE UPLOADER */

    [data-testid="stFileUploader"] {
        background-color: #1E293B;
        padding: 20px;
        border-radius: 18px;
        border: 2px dashed #475569;
        font-color: black;        
    }

    /* DRAG & DROP TEXT */

[data-testid="stFileUploader"] * {
    color: #000000 !important;
}

/* BROWSE FILE BUTTON */

[data-testid="stFileUploader"] button {
    color: #000000 !important;
    background-color: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
}

    /* BROWSE BUTTON HOVER */

    [data-testid="stFileUploader"] button:hover {
        color: #000000 !important;
        background-color: #F1F5F9 !important;
    }

    /* FILE NAME TEXT */

    [data-testid="stFileUploaderFile"] {
        color: #FFFFFF !important;
    }

    /* BUTTONS */

    .stButton > button {
        background: linear-gradient(135deg, #6366F1, #8B5CF6);
        color: white !important;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 600;
        width: 100%;
        transition: 0.3s;
        font-color:black        
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #4F46E5, #7C3AED);
        transform: scale(1.02);
        color: white !important;
    }

    /* DOWNLOAD BUTTON */

    .stDownloadButton > button {
        background-color: #059669;
        color: white !important;
        border-radius: 12px;
        border: none;
        padding: 10px 20px;
        font-weight: 600;
        width: 100%;
    }

    /* ALERTS */

    .stAlert {
        border-radius: 12px;
    }

    /* JSON OUTPUT CONTAINER */

    [data-testid="stJson"] {
        background: #FFFFFF !important;
        border: 1px solid #334155 !important;
        border-radius: 14px !important;
        padding: 15px !important;
    }

    /* JSON TEXT */

    [data-testid="stJson"] * {
        color: black !important;
        font-weight: 500 !important;
    }

    /* JSON KEYS */

    [data-testid="stJson"] label {
        color: black !important;
    }

    /* JSON CODE */

    [data-testid="stJson"] code {
        color: black !important;
        background: transparent !important;
    }

    /* EXPANDER */

    details {
        background-color: #FFFFFF !important;
        border-radius: 12px !important;
        padding: 10px !important;
    }

    /* EXPANDER TITLE */

    details summary {
        color: black !important;
        font-weight: 600 !important;
    }
    /* UPLOAD ONE OR MORE PDF/HTML FILES TEXT */

    [data-testid="stFileUploader"] label,
    [data-testid="stFileUploader"] small,
    [data-testid="stFileUploader"] p {
        color: #FFFFFF !important;
        font-weight: 500 !important;
    }
    
    /* SELECTED FILE NAME TEXT */

    [data-testid="stFileUploaderFileName"] {
        color: #FFFFFF !important;
        font-weight: 500 !important;
    }

    /* FILE SIZE TEXT */

    [data-testid="stFileUploaderFile"] small {
        color: #FFFFFF !important;
    }

    /* FILE ICON */

    [data-testid="stFileUploaderFile"] svg {
        color: #FFFFFF !important;
        fill: #FFFFFF !important;
    }
    
    /* REMOVE FILE (X) BUTTON */

    [data-testid="stFileUploaderDeleteBtn"] {
        color: #000000 !important;
    }

    [data-testid="stFileUploaderDeleteBtn"] svg {
        color: #000000 !important;
        fill: #000000 !important;
    }

    /* SIDEBAR COLLAPSE BUTTON */

    [data-testid="collapsedControl"] {
        position: fixed !important;
        top: 18px !important;
        left: 18px !important;
        z-index: 999999 !important;

        pointer-events: none !important;
        background: transparent !important;
    }

    /* BUTTON */

    [data-testid="collapsedControl"] button {
        pointer-events: auto !important;

        width: 55px !important;
        height: 55px !important;

        background: #6366F1 !important;
        border-radius: 14px !important;
        border: none !important;

        display: flex !important;
        align-items: center !important;
        justify-content: center !important;

        cursor: pointer !important;

        box-shadow: 0 4px 12px rgba(0,0,0,0.25) !important;

        transition: 0.2s !important;
    }

    /* BUTTON HOVER */

    [data-testid="collapsedControl"] button:hover {
        background: #4F46E5 !important;
        transform: scale(1.05);
    }

    /* ICON */

    [data-testid="collapsedControl"] svg {
        width: 30px !important;
        height: 30px !important;
        color: white !important;
    }

    </style>
    """, unsafe_allow_html=True)
# ---------------------------------------------------
# LIGHT THEME
# ---------------------------------------------------

else:

    st.markdown("""
    <style>

    /* REMOVE TOP HEADER SPACE */

    [data-testid="stHeader"] {
        background: transparent;
        height: 0px;
    }

    /* HIDE TOOLBAR + DEPLOY */

    .stDeployButton {
        display: none !important;
    }

    

    /* MAIN APP */

    .stApp {
        background: #F8FAFC;
        color: #0F172A;
    }

    /* SIDEBAR */

    section[data-testid="stSidebar"] {
        background-color: #E2E8F0;
        border-right: 1px solid #CBD5E1;
    }

    /* TEXT */

    h1, h2, h3, h4, h5, h6 {
        color: #0F172A !important;
    }

    p, label, div, span {
        color: #334155 !important;
    }

    /* FILE UPLOADER */

    [data-testid="stFileUploader"] {
        background-color: white;
        padding: 20px;
        border-radius: 18px;
        border: 2px dashed #94A3B8;
    }

    /* BUTTONS */

    .stButton > button {
        background: linear-gradient(135deg, #6366F1, #8B5CF6);
        color: white !important;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 600;
        width: 100%;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #4F46E5, #7C3AED);
        transform: scale(1.02);
        color: white !important;
    }

    /* DOWNLOAD BUTTON */

    .stDownloadButton > button {
        background-color: #059669;
        color: white !important;
        border-radius: 12px;
        border: none;
        padding: 10px 20px;
        font-weight: 600;
        width: 100%;
    }

    /* ALERTS */

    .stAlert {
        border-radius: 12px;
    }

    /* JSON BOX */

    [data-testid="stJson"] {
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 14px !important;
        padding: 18px !important;
    }

    /* JSON TEXT */

    [data-testid="stJson"] * {
        color: #111827 !important;
        font-weight: 500 !important;
    }

    /* EXPANDER */

    details summary {
        color: #111827 !important;
        font-weight: 600 !important;
    }

    /* FIX CLICK BLOCKING */

    [data-testid="collapsedControl"] {
        position: fixed !important;
        top: 18px !important;
        left: 18px !important;
        z-index: 999999 !important;

        pointer-events: none !important;
        background: transparent !important;
    }

    /* ONLY BUTTON SHOULD BE CLICKABLE */

    [data-testid="collapsedControl"] button {
        pointer-events: auto !important;

        width: 55px !important;
        height: 55px !important;

        background: #6366F1 !important;
        border-radius: 14px !important;
        border: none !important;

        display: flex !important;
        align-items: center !important;
        justify-content: center !important;

        cursor: pointer !important;

        box-shadow: 0 4px 12px rgba(0,0,0,0.25) !important;

        transition: 0.2s !important;
    }

    /* HOVER */

    [data-testid="collapsedControl"] button:hover {
        background: #4F46E5 !important;
        transform: scale(1.05);
    }

    /* ICON */

    [data-testid="collapsedControl"] svg {
        width: 30px !important;
        height: 30px !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)
    

# ---------------------------------------------------
# SIDEBAR CONTENT
# ---------------------------------------------------

with st.sidebar:

    st.title("AI RFP Extractor")

    st.markdown("---")

    st.subheader("Recent Uploads")

    if st.session_state.upload_history:

        for file_name in reversed(st.session_state.upload_history[-5:]):
            st.markdown(f"📄 {file_name}")

    else:
        st.info("No files uploaded yet")

    st.markdown("---")

    st.subheader("Statistics")

    st.metric(
        "Files Processed",
        st.session_state.total_processed
    )

    if st.session_state.upload_history:

        st.metric(
            "Last Uploaded",
            st.session_state.upload_history[-1][:20]
        )

    st.markdown("---")

    st.info("Industrial AI Document Intelligence System")

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("📄 AI-Powered RFP Information Extraction System")

st.markdown("""
Upload procurement/RFP documents and extract structured information using AI.
""")

st.markdown("---")

# ---------------------------------------------------
# FILE UPLOADER
# ---------------------------------------------------

st.subheader("📂 Upload Documents")

uploaded_files = st.file_uploader(
    "Upload one or more PDF/HTML files",
    type=["pdf", "html", "htm"],
    accept_multiple_files=True
)

st.markdown("---")

# ---------------------------------------------------
# PROCESS FILES
# ---------------------------------------------------

if uploaded_files:

    st.success(f"{len(uploaded_files)} file(s) uploaded successfully")

    st.markdown("## Uploaded Files")

    for uploaded_file in uploaded_files:

        if uploaded_file.name not in st.session_state.upload_history:
            st.session_state.upload_history.append(uploaded_file.name)

        st.session_state.total_processed += 1

        with st.container():

            st.markdown(f"### 📄 {uploaded_file.name}")

            col1, col2 = st.columns([2, 1])

            with col1:

                st.write(f"**File Size:** {round(uploaded_file.size / 1024, 2)} KB")
                st.write("**Status:** Ready for Extraction")

            with col2:

                extract_clicked = st.button(
                    "Extract Information",
                    key=uploaded_file.name
                )

            # ---------------------------------------------------
            # EXTRACTION
            # ---------------------------------------------------

            if extract_clicked:

                start_time = time.time()

                with st.spinner(f"Analyzing {uploaded_file.name}..."):

                    result = process_uploaded_file(uploaded_file)

                end_time = time.time()

                processing_time = round(end_time - start_time, 2)

                st.success("Extraction Completed Successfully")

                st.info(f"Processed in {processing_time} seconds")

                # ---------------------------------------------------
                # ERROR HANDLING
                # ---------------------------------------------------

                if "error" in result:

                    st.error(result["error"])

                    if "message" in result:
                        st.warning(result["message"])

                else:

                    # ---------------------------------------------------
                    # JSON OUTPUT
                    # ---------------------------------------------------

                    st.subheader("Extracted Structured Data")

                    st.json(result)

                    # ---------------------------------------------------
                    # JSON DOWNLOAD
                    # ---------------------------------------------------

                    json_data = json.dumps(result, indent=4)

                    st.download_button(
                        label="⬇ Download JSON",
                        data=json_data,
                        file_name=f"{uploaded_file.name}.json",
                        mime="application/json",
                        key=f"json_{uploaded_file.name}"
                    )

                    # ---------------------------------------------------
                    # CSV EXPORT
                    # ---------------------------------------------------

                    try:

                        flattened_data = {}

                        for key, value in result.get("basic_extracted_data", {}).items():

                            flattened_data[key] = ", ".join(map(str, value))

                        llm_output = result.get("llm_output", {})

                        for section, content in llm_output.items():

                            if isinstance(content, dict):

                                for sub_key, sub_value in content.items():

                                    flattened_data[f"{section}_{sub_key}"] = str(sub_value)

                            elif isinstance(content, list):

                                flattened_data[section] = ", ".join(map(str, content))

                            else:

                                flattened_data[section] = str(content)

                        df = pd.DataFrame([flattened_data])

                        csv_data = df.to_csv(index=False)

                        st.download_button(
                            label="⬇ Download CSV",
                            data=csv_data,
                            file_name=f"{uploaded_file.name}.csv",
                            mime="text/csv",
                            key=f"csv_{uploaded_file.name}"
                        )

                    except Exception as e:

                        st.error(f"CSV Export Error: {str(e)}")

                    # ---------------------------------------------------
                    # METADATA
                    # ---------------------------------------------------

                    with st.expander("Processing Metadata"):

                        metadata = {
                            "processed_at": str(datetime.now()),
                            "model_used": "openai/gpt-3.5-turbo",
                            "document_type": uploaded_file.type
                        }

                        st.json(metadata)

            st.markdown("---")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")

st.caption("Built using AI + NLP + Document Intelligence Pipeline")