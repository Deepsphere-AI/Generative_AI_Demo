# Import the Speech-to-Text client library
# from google.cloud import aiplatform
#import vertexai
#from vertexai.language_models import TextGenerationModel
import openai
import os
#from google.cloud import speech
#from google.cloud import texttospeech

openai.api_key = os.environ["API_KEY"]

def generate_response4(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-4",
    temperature=0,
    max_tokens=3500,
    messages=[{'role':'user','content':prompt}],
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    )
    return response['choices'][0]['message']['content']

def generate_response3_5(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0.2,
    max_tokens=3000,
    messages=[{'role':'user','content':prompt}],
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    )
    return response['choices'][0]['message']['content']

def generate_response3(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.2,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    return response["choices"][0]["text"]


def model_tts(prompt,voice_out):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=prompt)
    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="es-US",
        name=voice_out,
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        speaking_rate=1
    )
    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )
    # The response's audio_content is binary.
    with open("result/output.mp3", "wb") as out:
        out.write(response.audio_content)


# def model_stt(audio_content):
#     # Instantiates a client
#     client = speech.SpeechClient()
#     # The content of the audio file to transcribe
#     audio_content = audio_content
#     # transcribe speech
#     audio = speech.RecognitionAudio(content=audio_content)

#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=24000,
#         language_code="en-US",
#         model="default",
#         audio_channel_count=1,
#         enable_word_confidence=True,
#         enable_word_time_offsets=True,
#     )

    # # Detects speech in the audio file
    # operation = client.long_running_recognize(config=config, audio=audio)

    # # print("Waiting for operation to complete...")
    # response = operation.result(timeout=90)
    # for result in response.results:
    #     print("Transcript: {}".format(result.alternatives[0].transcript))

def model_img(prompt):
  response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  return (image_url)
