# 📄 resume-analysis.ai

🚀 An AI-powered Resume Screening Web App built using **Streamlit** and **Google Gemini (Generative AI)**. It compares a candidate's resume with a job description and provides insightful metrics such as ATS score, selection probability, missing keywords, SWOT analysis, and project suggestions.

---

## 🔗 Live Demo

<img width="1907" height="846" alt="image" src="https://github.com/user-attachments/assets/a44b7ac3-9fc3-4b82-aa1a-225ccdbc456d" />

---

## 🎯 Project Goal

To build a smart resume analysis tool that leverages **Generative AI** to match a candidate’s resume with a job description and offer real-time, actionable feedback.

---

## 🧠 Project Insights

The app provides the following insights:
- 📊 **ATS Score** – How well your resume passes automated screening
- 📈 **Selection Probability** – Likelihood of being shortlisted
- ✅ **Fit Check** – Are you a good match for the job?
- 🔍 **Keyword Analysis** – Missing or weak areas
- 📌 **SWOT Analysis** – Strengths, Weaknesses, Opportunities, Threats
- 💡 **Improvement Suggestions** – Tailored project recommendations

---

## 🛠️ Tech Stack

| Tool/Library           | Description                              |
|------------------------|------------------------------------------|
| `Streamlit`            | Web app front-end                        |
| `Python`               | Programming language                     |
| `PyPDF`                | Extract text from PDF resumes            |
| `google.generativeai`  | Gemini API for LLM-based insights        |
| `dotenv`               | Manage sensitive environment variables   |

---

## 🏗️ Architecture

resume-analysis.ai/
│
├── app.py # Frontend with Streamlit UI
├── analysis.py # Generates insights using Gemini LLM
├── pdf.py # Extracts text from uploaded PDF resumes
├── requirements.txt # Required dependencies
└── .env # Environment variables (API key)


- `app.py`: Main entry point – handles UI, collects resume & JD, and displays LLM outputs.
- `pdf.py`: Extracts clean text from uploaded PDF resumes using `PyPDF`.
- `analysis.py`: Sends prompts to the Gemini model and returns structured insights.

---

## 🧪 Steps to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/RajatLatwal/resume-analysis.ai.git
   cd resume-analysis.ai
   ```
   
2. **Create a virtual environment**
  ```bash
   python -m venv .venv
```

3. **Activate the virtual environment**
```bash
  .venv\Scripts\activate
```

4. **Install the dependencies**
```bash
  pip install -r requirements.txt
```

5. **Add your Gemini API key**
  * Create a ``.env`` file and add:
```bash
    GOOGLE_API_KEY=your_gemini_api_key
```

6. **Run the app**
  ```bash
  streamlit run app.py
  ```
---
