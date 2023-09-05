import streamlit as st
import PyPDF2
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
import os
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = os.environ["API_KEY"]

def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF using the newer PdfReader."""
    with open("temp.pdf", "wb") as out_file:
        out_file.write(uploaded_file.getbuffer())
    
    with open("temp.pdf", "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

# Download embeddings from OpenAI
embeddings = OpenAIEmbeddings()




st.title("PDF Question Answering using OpenAI")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file is not None:
    raw_text = extract_text_from_pdf(uploaded_file)
    # We need to split the text using Character Text Split such that it sshould not increse token size
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 800,
        chunk_overlap  = 200,
        length_function = len,
    )
    texts = text_splitter.split_text(raw_text)
    question = st.text_input("Ask a question about the uploaded document:")

    if question:
        document_search = FAISS.from_texts(texts, embeddings)
        chain = load_qa_chain(OpenAI(), chain_type="stuff")
        docs = document_search.similarity_search(question)
        answer = chain.run(input_documents=docs, question=question)
        st.write("Answer:", answer)