#MYRESUME.ai
REsume Analysis

### Step for Creating the Project
* Create the Virtual environment ``python -m venv .venv``
* Activate the virtual environment`` source .venv/Script/activate``
* Create the .env file to store the API key
* Create the requirements.txt file and add liberaries for installation``pip install -r requirememnts.txt``

### About Project 
* WE want to create an application that will analysis the resume of the candidate using the Gen Ai model with the Job Description and provide the  insights:-
-ATS Score
-Probablity of getting hired
-Keyword Analysis
-SWOT Analysis
-Suggest for Overall Improvements

### Architecture
* app.py: Front end creation and output of Genai Model.
It will have a feature of capturing the information such as Resume and JD
* Information we are capturing is ``REsume.pdf`` and ``job_desc``.
* pdf.py that will process the information in pdf and that why we have installed ``pypdf``
* analysis.py that will triangulate the pdf information and the JD and will provide insights and next step.