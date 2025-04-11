# Cover Letter Generator

Welcome to the **Cover Letter Generator** repository! This project is a lightweight, AI-powered web app that helps users create personalized, professional cover letters. By uploading a resume and entering job-specific details, the app generates a tailored cover letter using **LLaMA 3.2 running locally** — no internet or API keys required.

![Screenshot](assets/screenshot.png)

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Installation](#installation)
- [LLaMA 3.2 Setup via Ollama](#LLaMA-3.2-Setup-via-Ollama)

## Features

- **Resume Parsing**
  - Supports `.pdf` and `.docx` resume uploads.
  - Automatically extracts and formats resume content.

- **Cover Letter Generation**
  - Uses local LLaMA 3.2 LLM for generating cover letters.
  - Tailors content based on:
    - Job Title
    - Company Name
    - Job Description

- **Streamlit Web Interface**
  - Clean, responsive UI for a smooth user experience.
  - Text preview of generated cover letters.
  - Copy and reuse output instantly.

- **Private & Local**
  - No external API calls or cloud storage.
  - All processing happens on your machine.

## Tech Stack

- **Frontend/UI:** Streamlit
- **AI Model:** LLaMA 3.2 (running locally)
- **Document Parsing:** 
  - `pdfplumber` for PDF resumes
  - `docx2txt` for Word resumes
- **Language:** Python 3.8+

## Architecture

This project follows a modular architecture:

- **UI Layer:** Built with Streamlit, collects user inputs and displays output.
- **Resume Parser:** Extracts raw text from uploaded files.
- **Prompt Engine:** Constructs structured prompts for LLaMA.
- **LLM Backend:** LLaMA 3.2 handles natural language generation locally.

## LLaMA 3.2 Setup via Ollama

This app uses **LLaMA 3.2**, running locally through [Ollama](https://ollama.com), allowing fast, private, and offline AI generation — no API keys required.

### Steps to Install LLaMA Locally

1. **Install Ollama**  
   Visit [https://ollama.com](https://ollama.com) and download the installer for your operating system (macOS, Windows, or Linux).

2. **Start the Ollama Server**  
   After installation, the server typically starts automatically.  
   To confirm, open your browser and go to:  
   [http://localhost:11434](http://localhost:11434)

   You should see the message:
   Ollama is running
   
3. **If the server isn't running, start it manually in a terminal**:
   
    ```bash
    ollama serve
    ```
  
4. **Download the LLaMA 3.2 model in another terminal**:
   
    ```bash
    ollama pull llama3.2
    ```
5. **Once the model is downloaded, your local LLaMA server will be ready to respond to AI generation requests at**:
     http://localhost:11434

## Installation

1. **Clone the repository**:
   
     ```bash
     git clone https://github.com/mohamedzeina/cover-letter-generator.git
     cd cover-letter-generator
     ```
2. **Create the Conda environment** \
    Make sure you have [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed. \
    Create the environment using the provided `environment.yaml` file:
   
    ```bash
    conda env create -f environment.yaml
    ```
3. **Activate the environment**

    ```bash
    conda activate cov-letter-gen
    ```
4. **Run the Streamlit app**

   ```bash
    streamlit run coverLetterGen.py
    ```

   
   
   
