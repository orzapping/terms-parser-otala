
import streamlit as st
from PyPDF2 import PdfReader

st.title("Issue Terms Parser – Streamlit MVP")

uploaded_file = st.file_uploader("Upload a PDF issue terms document", type="pdf")
if uploaded_file:
    st.success("File uploaded. Parsing...")
    st.write("**Uploaded File:**", uploaded_file.name)
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    st.subheader("Extracted Text (First 1000 chars):")
    st.code(text[:1000])
    st.subheader("Parsing Results (Placeholder)")
    st.info("This is where parsed clauses, confidence scores, and highlights will be shown.")
