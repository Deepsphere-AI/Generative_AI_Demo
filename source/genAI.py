import streamlit as st
from audio_recorder_streamlit import audio_recorder
from source.model import *

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
            vAR_use_case = ["GPT-3","GPT-3.5","GPT-4"]
            vAR_input_use_case = st.radio('',options=vAR_use_case,horizontal=True)
            if vAR_input_use_case == "GPT-3":
                with col1:
                    st.write("")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_text_input=st.text_input("")
                    if vAR_text_input != "":
                        if st.button("Submit"):
                            response_1=generate_response3(vAR_text_input)
                            with cc1:
                                st.markdown("### "+response_1)
            elif vAR_input_use_case == "GPT-3.5":
                with col1:
                    st.write("")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_text_input_2=st.text_input("")
                    if vAR_text_input_2 != "":
                        if st.button("Submit"):
                            response_2=generate_response3_5(vAR_text_input_2)
                            with cc1:
                                st.markdown("### "+response_2)
            elif vAR_input_use_case == "GPT-4":
                with col1:
                    st.write("")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_text_input_3=st.text_input("")
                    if vAR_text_input_3 != "":
                        if st.button("Submit"):
                            response_3=generate_response4(vAR_text_input_3)
                            with cc1:
                                st.markdown("### "+response_3)
        elif vAR_input_app == 'Vision':
            with col1:
                st.write("## ")
                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select a Model</span></p>", unsafe_allow_html=True)
            vAR_use_case = ['Select',"DALL·E"]
            with col2:
                vAR_input_use_case = st.selectbox('',vAR_use_case)
            if vAR_input_use_case == 'DALL·E':
                with col1:
                    st.write("## ")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_text_img = st.text_input("")
                    if vAR_text_img != "":
                        if st.button("Submit"):
                            resp = model_img(vAR_text_img)
                            with cc1:
                                st.image(resp)
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
                    if vAR_voice=='English - Female':
                        voice_out= "en-US-Studio-O"
                    elif vAR_voice=='English - Male':
                        voice_out = "en-US-Studio-M"
                    elif vAR_voice=="Spanish - Male":
                        voice_out="es-US-Studio-B"
                    with col1:
                        st.write("## ")
                        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input</span></p>", unsafe_allow_html=True)
                    with col2:
                        vAR_text = st.text_input("")
                        if vAR_text != "":    
                            if st.button("Submit"):
                                response_4=model_tts(vAR_text,voice_out)
                                
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