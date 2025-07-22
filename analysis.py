import google.generativeai as genai
from pdf import process_pdf
import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
# Configure genai and model 
genai.configure(api_key=os.getenv('GOOGLE-API-KEY'))
model=genai.GenerativeModel('gemini-1.5-flash') # flash is good for pdf

def analyse_profile(job_desc,pdf_doc):
    if pdf_doc is not None:
        pdf=process_pdf(pdf_doc)
        st.sidebar.markdown('Upload Successful ✅️')
    else:
        st.warning('Upload the Resume')

    good_fit= model.generate_content(f'''Compare the {job_desc} with the 
                                      resume {pdf} and suggest if I 
                                      am a good fit for the role''')
    ats_score= model.generate_content(f'''Compare the {job_desc} with the 
                                      resume {pdf} and suggest the ATS Score 
                                      of the Resume''')
    probability= model.generate_content(f'''Compare the {job_desc} with the 
                                      resume {pdf} and suggest the probablity
                                        of getting hired in percentage ''')
    keyword_analysis= model.generate_content(f'''Compare the {job_desc} with the 
                                      resume {pdf} and do keyword analysis in both 
                                      and mention the keywords and give me the keywords 
                                      shown in job description but missing in resume''')
    SWOT_analysis= model.generate_content(f'''Compare the {job_desc} with the 
                                      resume {pdf} and give me SWOT Analysis followed 
                                      by actionable insights in bullet points''')
    projects= model.generate_content(f'''Compare the {job_desc} with the 
                                      resume {pdf} and suggest the projects that are 
                                      alligned with the job description & the role in bullet 
                                      points along with chances of getting selected''')
    return (st.write(good_fit.text),
            st.write(ats_score.text),
            st.write(probability.text),
            st.write(keyword_analysis.text),
            st.write(SWOT_analysis.text),
            st.write(projects.text))