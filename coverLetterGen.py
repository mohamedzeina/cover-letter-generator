import streamlit as st
import pdfplumber
import docx2txt
import io
import logging as log
import os

def extractText(file):
    if file.type == "application/pdf":
        with pdfplumber.open(file) as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return docx2txt.process(file)
    else:
        return "Unsupported file type."




st.title("📄 AI Cover Letter Generator")

uploadedFile = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])
jobTitle = st.text_input("Job Title")
companyName = st.text_input("Company Name")
jobDesc = st.text_area("Paste the Job Description")

if st.button("Generate Cover Letter"):
    if uploadedFile and jobTitle and companyName and jobDesc:
        resumeText = extractText(uploadedFile)
        #cover_letter = generate_cover_letter(resume_text, job_title, company_name, job_description)
        st.subheader("📬 Your Cover Letter")
        st.text_area("Generated Letter", resumeText, height=300)
    else:
        st.error("Please fill in all fields and upload your resume.")