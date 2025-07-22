from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from pdf import process_pdf
from analysis import analyse_profile


# Create the front end of application here
st.header('💼SCAN MY :blue[CV.AI]📝', divider='green')
st.subheader('Tips for using the Application')
notes=f'''
* **Upload Resume:** Upload the Resume in PDF format only.
* **Paste the JD:** Paste the job description below.
* Use the power of LLMs to derive the insight about resume and compare it with JD.
'''
st.write(notes)

#Sidebar
st.sidebar.subheader('Upload the Resume')
pdf_doc=st.sidebar.file_uploader('Upload the Resume',type=['pdf'])
st.sidebar.write('Created By :red[Aseem Gulati] 👩🏻‍💻')


# Job Desription
st.subheader('✅Enter the Job Descrpition',divider=True)
job_desc=st.text_area(label='Enter the Job Description from job Board(eg. Linkedin)',
             max_chars=10000)
submit=st.button(label='Get AI Powered Insights')
if submit:
    st.markdown(analyse_profile(pdf_doc=pdf_doc,job_desc=job_desc))
