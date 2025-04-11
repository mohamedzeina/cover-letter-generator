import streamlit as st
import io




st.title("📄 AI Cover Letter Generator")

uploadedFile = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])
jobTitle = st.text_input("Job Title")
companyName = st.text_input("Company Name")
jobDesc = st.text_area("Paste the Job Description")

if st.button("Generate Cover Letter"):
    if uploadedFile and jobTitle and companyName and jobDesc:
        #resume_text = extract_text(uploaded_file)
        #cover_letter = generate_cover_letter(resume_text, job_title, company_name, job_description)
        st.subheader("📬 Your Cover Letter")
        st.text_area("Generated Letter", "cover_letter", height=300)
    else:
        st.error("Please fill in all fields and upload your resume.")