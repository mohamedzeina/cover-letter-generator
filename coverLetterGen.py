import streamlit as st
import pdfplumber
import docx2txt
import io
import logging as log
import os
import ollama


def extractText(file):
    if file.type == "application/pdf":
        with pdfplumber.open(file) as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return docx2txt.process(file)
    else:
        return "Unsupported file type."

def generateUserPrompt(resumeText, jobTitle, companyName, jobDesc):
    
   userPrompt = (
    f"You are reviewing a candidate applying for the position of '{jobTitle}' at '{companyName}'.\n\n"
    f"📄 Job Description:\n{jobDesc}\n\n"
    f"📑 Resume:\n{resumeText}\n\n"
    "✉️ Based on the resume, job title, company, and job description above, generate a personalized, professional cover letter tailored to this role. "
    "Highlight relevant experience and skills from the resume that align with the job requirements. "
    "Use a confident and engaging tone. Keep the letter concise and structured in 3–5 paragraphs."
)
   
   return userPrompt

def generateSystemPrompt():
    return """You are a helpful assistant that specializes in generating professional cover letters. Given a person's resume, the company name, the job title they are applying for, and the job description, your task is to write a personalized cover letter tailored to the job. The tone should be professional, confident, and aligned with the role. Highlight relevant experience and skills from the resume that match the job description. Keep the letter concise, typically within 3-5 paragraphs"""


def generateCoverLetter(resumeText, jobTitle, companyName, jobDesc):
    userPrompt = generateUserPrompt(resumeText, jobTitle, companyName, jobDesc)
    systemPrompt = generateSystemPrompt()
    
    messages = [{"role": "system", "content": systemPrompt}, {"role": "user", "content": userPrompt}]
    response = ollama.chat(model="llama3.2", messages = messages)
    coverLetter = response['message']['content']
    
    return coverLetter
    
    
    
st.title("📄 AI Cover Letter Generator")

uploadedFile = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])
jobTitle = st.text_input("Job Title")
companyName = st.text_input("Company Name")
jobDesc = st.text_area("Paste the Job Description")

if st.button("Generate Cover Letter"):
    if uploadedFile and jobTitle and companyName and jobDesc:
        resumeText = extractText(uploadedFile)
        coverLetter = generateCoverLetter(resumeText, jobTitle, companyName, jobDesc)
        st.subheader("📬 Your Cover Letter")
        
        st.text_area("Generated Letter", coverLetter, height=300)
    else:
        st.error("Please fill in all fields and upload your resume.")