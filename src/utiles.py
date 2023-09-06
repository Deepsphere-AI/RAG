import os
import PyPDF2
import fitz
import re
import newspaper
import streamlit as st


def fullstr(pdf_content):
    with open("Result/newfile.txt","w", encoding='utf-8') as fill_pmt:
        fill_pmt.write(str(pdf_content))
    b=[]
    with open("Result/newfile.txt","r", encoding='utf-8') as r_txt:
        whole=r_txt.read()
        r_txt.seek(0)
        if len(whole) > 3000:
            for i in range(len(whole)//3000):
                a=r_txt.read(3000)
                if len(a)>100:
                    b.append(a)
        else:
            b.append(whole)
    return b

def header_footer_cuter(uploaded_file):
    pdf_reader = PyPDF2.PdfReader (uploaded_file)
    pdf_writer = PyPDF2.PdfWriter ()
    # Remove header and footer from each page
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num] 
        page_media_box = page.mediabox

        # Remove header by adjusting the media box
        header_height = 40
        page_media_box.upper_right = (page_media_box.right, page_media_box.top - header_height)

        # Remove footer by adjusting the media box
        footer_height = 80
        page_media_box.lower_left = (page_media_box.left, page_media_box.bottom + footer_height)

        # Add modified page to output PDF
        pdf_writer.add_page(page)
        

        # Save output PDF file
        output_file = "Result/output.pdf"
        with open(output_file, "wb") as f:
            pdf_writer.write(f)



def pdf_text():
    # File upload
    pdf_file = ("Result/output.pdf")
    if pdf_file is not None:
        text = extract_text(pdf_file)
        os.remove(pdf_file)
    return text

def extract_text(pdf_file):
    with fitz.open(pdf_file) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
        # Replace all numeric values with an empty string
        text = re.sub(r'\d+', '', text)
        return text
    

def get_paragraphs(url):
    # Initialize newspaper's Article object
    article = newspaper.Article(url)
    
    # Download and parse the article
    article.download()
    article.parse()
    
    # Return the extracted article text
    return article.text