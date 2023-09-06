import streamlit as st
import openai
from src.file_processing import file_process

def prev1():
    st.session_state['preview1']="No"
def prev2():
    st.session_state['preview2']="No"
def prev3():
    st.session_state['preview3']="No"

def QuestionAnswering():
    w1,col1,col2,w2=st.columns((1.5,3,4,.1))
    cc2,cc1,cc3=st.columns((2,6,0.2))
    col11,col22,col33=st.columns((2,8,0.2))
    with col1:
        st.write("## ")
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Vendor</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_app = ['Openai','Google']
        vAR_input_vendor = st.radio(' ',vAR_app,horizontal=True)
    
    if vAR_input_vendor == 'Openai':
        with col1:
            st.write("## ")
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Model</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_input_model = st.selectbox('',options=['Select','text-embedding-ada-002'])

        if vAR_input_model == 'text-embedding-ada-002':
            file_process(vAR_input_vendor)

    elif vAR_input_vendor == 'Google':
        with col1:
            st.write("## ")
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Model</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_input_model = st.selectbox('',options=['Select',"text-bison@001"])

        if vAR_input_model == "text-bison@001":
            file_process(vAR_input_vendor)