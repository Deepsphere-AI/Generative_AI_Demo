import streamlit as st
from audio_recorder_streamlit import audio_recorder
# from source.model import model_tts,model_stt

def features():
    w1,col1,col2,w2=st.columns((1.5,2.5,4,.1))
    cc2,cc1,cc3=st.columns((2,6,0.2))
    col11,col22,col33=st.columns((2,8,0.2))
    with col1:
        st.write("## ")
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select to Generate</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_app = ['Language','Vision','Voice']
        vAR_input_app = st.radio(' ',vAR_app,horizontal=True)
    
    with col2:
        if vAR_input_app == 'Language':
            with col1:
                st.write("## ")
                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select a Model</span></p>", unsafe_allow_html=True)
            vAR_use_case = ["text-bison (latest)","text-bison@001"]
            vAR_input_use_case = st.radio('',options=vAR_use_case,horizontal=True)
            if vAR_input_use_case == "text-bison (latest)":
                with col1:
                    st.write("")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_text_input=st.text_input("")
                    if vAR_text_input != "":
                        if st.button("Submit"):
                            # model()
                            pass
            elif vAR_input_use_case == "text-bison@001":
                with col1:
                    st.write("")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_text_input_2=st.text_input("")
                    if vAR_text_input_2 != "":
                        if st.button("Submit"):
                            # model()
                            pass
        elif vAR_input_app == 'Vision':
            pass
        elif vAR_input_app == 'Voice':
            with col1:
                st.write("## ")
                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select a Model</span></p>", unsafe_allow_html=True)
            vAR_type= ['Text to Speech','Speech to Text']
            vAR_input_use_case = st.radio('',options=vAR_type,horizontal=True)
            if vAR_input_use_case == 'Text to Speech':
                with col1:
                    st.write("### ")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Voice</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_voice = st.selectbox("",['Select','English - Female','English - Male','Spanish - Male'])
                if vAR_voice != 'Select':
                    with col1:
                        st.write("## ")
                        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input</span></p>", unsafe_allow_html=True)
                    with col2:
                        vAR_text = st.text_input("")
                        if vAR_text != "":
                            if st.button("Submit"):
                                # model()
                                pass
            elif vAR_input_use_case == 'Speech to Text':
                with col1:
                    st.write("### ")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Record</span></p>", unsafe_allow_html=True)
                with col2:
                    st.write("# ")
                    audio_bytes = audio_recorder("",icon_size="2x")
                    if audio_bytes:
                        st.audio(audio_bytes, format="audio/wav")
                        if st.button("Submit"):
                            # model()
                            pass