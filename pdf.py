# Defactor
# methodology of handeling the pdf
from pypdf import PdfReader

def process_pdf(pdf_doc): # pdf_doc which was created in app.py
    pdf=PdfReader(pdf_doc)# objective is to extract the text and save in a var.
    raw_text=" "
    # index of pdf page and page content
    for index, page in enumerate(pdf.pages):
        content=page.extract_text()
        if content:
            raw_text += content
    return (raw_text)
