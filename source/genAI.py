import streamlit as st
from audio_recorder_streamlit import audio_recorder
from source.model import *

def features():
    # creating columns 
    w1,col1,col2,w2=st.columns((1.5,3.5,3.5,0.3))
    cc2,cc1,cc3=st.columns((2,6,0.2))
    col11,col22,col33=st.columns((2,8,0.2))

    
    with col1:
        st.write("## ")
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Generate What You Need</span></p>", unsafe_allow_html=True)
    with col2:
        # radio button to select generate what you need
        vAR_app = ['Language','Vision','Voice']
        vAR_input_app = st.radio(' ',vAR_app,horizontal=True)
    
    # code for Language generation
    with col2:
        if vAR_input_app == 'Language':
            with col1:
                st.write("### ")
                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select the Model and API Services</span></p>", unsafe_allow_html=True)
            # radio button for select a model.
            vAR_use_case = ["GPT-3","GPT-3.5","GPT-4"]
            vAR_input_use_case = st.radio('',options=vAR_use_case,horizontal=True)
            if vAR_input_use_case == "GPT-3":
                with col1:
                    st.write("### ")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_text_input=st.text_input("")
                    if vAR_text_input != "":
                        st.write("")

                        # submit button
                        if st.button("Submit"):
                            # Calling the model
                            response_1=generate_response3(vAR_text_input)
                            with cc1:
                                # Displaying the response from model
                                st.markdown(response_1)

            elif vAR_input_use_case == "GPT-3.5":
                with col1:
                    st.write("")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_text_input_2=st.text_input("")
                    if vAR_text_input_2 != "":
                        # submit button
                        if st.button("Submit"):
                            # Calling the model
                            response_2=generate_response3_5(vAR_text_input_2)
                            with cc1:
                                # Displaying the response from model
                                st.markdown("### "+response_2)

            elif vAR_input_use_case == "GPT-4":
                with col1:
                    st.write("")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_text_input_3=st.text_input("")
                    if vAR_text_input_3 != "":
                        # submit button
                        if st.button("Submit"):
                            # Calling the model
                            response_3=generate_response4(vAR_text_input_3)
                            with cc1:
                                # Displaying the response from model
                                st.markdown("### "+response_3)
        
        # code for vision generation
        elif vAR_input_app == 'Vision':
            with col1:
                st.write("## ")
                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select the Model and API Services</span></p>", unsafe_allow_html=True)
            vAR_use_case = ['Select',"DALL·E (OpenAI)"]
            with col2:
                vAR_input_use_case = st.selectbox('',vAR_use_case)
            if vAR_input_use_case == 'DALL·E (OpenAI)':
                with col1:
                    st.write("## ")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_text_img = st.text_input("")
                    if vAR_text_img != "":
                        # submit button
                        if st.button("Submit"):
                            # Calling the model
                            resp = model_img(vAR_text_img)
                            with cc1:
                                # Displaying the generated image from model
                                st.image(resp)
        
        # code for voice generation
        elif vAR_input_app == 'Voice':
            with col1:
                st.write("### ")
                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select the Model and API Services</span></p>", unsafe_allow_html=True)
            vAR_type= ['Text to Speech','Speech to Text']
            vAR_input_use_case = st.radio('',options=vAR_type,horizontal=True)

            # Text to Speech
            if vAR_input_use_case == 'Text to Speech':
                with col1:
                    st.write("### ")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Voice Style</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_voice = st.selectbox("",['Select','English - Female','English - Male','Spanish - Male'])
                if vAR_voice != 'Select':
                    if vAR_voice=='English - Female':
                        voice_out= "en-US-News-K"
                    elif vAR_voice=='English - Male':
                        voice_out = "en-US-Wavenet-D"
                    elif vAR_voice=="Spanish - Male":
                        voice_out="es-US-Studio-B"
                    with col1:
                        st.write("## ")
                        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input</span></p>", unsafe_allow_html=True)
                    with col2:
                        vAR_text = st.text_input("")
                        if vAR_text != "":    
                            if st.button("Submit"):
                                # Calling the model
                                response_4=model_tts(vAR_text,voice_out)
                                audio_file = open('result/output.mp3', 'rb')
                                audio_bytes = audio_file.read()
                                with cc1:
                                    # Displaying the response
                                    st.audio(audio_bytes, format='audio/mp3')

            # Speech to text
            elif vAR_input_use_case == 'Speech to Text':
                with col1:
                    st.write("### ")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input</span></p>", unsafe_allow_html=True)
                with col2:
                    st.write("# ")
                    audio_bytes = audio_recorder("",icon_size="2x")
                    if audio_bytes:
                        with open('result/file.wav', "wb") as f:
                            f.write(audio_bytes)
                        st.audio(audio_bytes, format="audio/wav")
                        if st.button("Submit"):
                            audio_file= open("result/file.wav", "rb")
                            # Calling the model
                            response_5=model_stt(audio_file)
                            with cc1:
                                # Displaying the response
                                st.markdown("### "+response_5)
                            