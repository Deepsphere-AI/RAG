import streamlit as st
from src.utiles import *
from src.OpenAI import Openai_embeddings
from src.GCP_model import GCP_Embedding

def file_process(vAR_input_vendor):
    w1,col1,col2,w2=st.columns((1.5,3,4,.1))
    cc2,cc1,cc3=st.columns((2,6,0.2))
    col11,col22,col33=st.columns((2,8,0.2))
    with col1:
        st.write("## ")
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Upload Type</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_input_type = ['Passage','File Upload','Web URL']
        vAR_user_input_type = st.radio(' ',vAR_input_type,horizontal=True)
    # Passage
    if vAR_user_input_type == "Passage":
        with col1:
            st.write("## ")
            st.write("## ")
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Input Passage</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_user_input_passage = st.text_area(' ')
        if vAR_user_input_passage != "":
            with col1:
                st.write("# ")
                st.write("# ")
                st.write("### ")
                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>What your Question?</span></p>", unsafe_allow_html=True)
            with col2:
                vAR_user_Question = st.text_input("")
                if vAR_user_Question != "":
                    if vAR_input_vendor == 'Openai':
                        vAR_answer = Openai_embeddings(vAR_user_input_passage,vAR_user_Question)
                        with col2:
                            st.success(vAR_answer)

                    if vAR_input_vendor == 'Google':
                        vAR_answer = GCP_Embedding(vAR_user_input_passage,vAR_user_Question)
                        with col2:
                            st.success(vAR_answer)
    
    if vAR_user_input_type == "File Upload":
        with col1:
            st.write("## ")
            st.write("## ")
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input (File Upload)</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_user_input_file = st.file_uploader("", type=['pdf', 'txt'])
        if vAR_user_input_file is not None:
            if 'txt' in str(vAR_user_input_file):
                vAR_textfile_content = vAR_user_input_file.getvalue().decode("utf-8")
                if vAR_textfile_content !=[]:
                    with col1:
                        st.write("# ")
                        st.write("# ")
                        st.write("### ")
                        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>What your Question?</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_user_Question = st.text_input("")
                    if vAR_user_Question != "":
                        if vAR_input_vendor == 'Openai':
                            vAR_answer = Openai_embeddings(vAR_textfile_content,vAR_user_Question)
                            with col2:
                                st.success(vAR_answer)

                        if vAR_input_vendor == 'Google':
                            vAR_answer = GCP_Embedding(vAR_textfile_content,vAR_user_Question)
                            with col2:
                                st.success(vAR_answer)
            else:
                header_footer_cuter(vAR_user_input_file)
                vAR_pdf_file_content = pdf_text()
            if vAR_pdf_file_content !=[]:    
                with col1:
                        st.write("# ")
                        st.write("# ")
                        st.write("### ")
                        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>What your Question?</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_user_Question = st.text_input("")
                    if vAR_user_Question != "":
                        if vAR_input_vendor == 'Openai':
                            vAR_answer = Openai_embeddings(vAR_pdf_file_content,vAR_user_Question)
                            with col2:
                                st.success(vAR_answer)

                        if vAR_input_vendor == 'Google':
                            vAR_answer = GCP_Embedding(vAR_pdf_file_content,vAR_user_Question)
                            with col2:
                                st.success(vAR_answer)
            
    if vAR_user_input_type == "Web URL":
        with col1:
            st.write("## ")
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Input URL</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_user_input_passage = st.text_input(' ')
        if vAR_user_input_passage != '':
            vAR_retrivetext_url = get_paragraphs(vAR_user_input_passage)
            if vAR_retrivetext_url !=[]:   
                with col1:
                    st.write("## ")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>What your Question?</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_user_Question = st.text_input("")
                    if vAR_user_Question != "":
                        if vAR_input_vendor == 'Openai':
                            vAR_answer = Openai_embeddings(vAR_retrivetext_url,vAR_user_Question)
                            with col2:
                                st.success(vAR_answer)

                        if vAR_input_vendor == 'Google':
                            vAR_answer = GCP_Embedding(vAR_retrivetext_url,vAR_user_Question)
                            with col2:
                                st.success(vAR_answer)