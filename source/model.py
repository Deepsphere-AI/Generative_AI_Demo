# Import the Speech-to-Text client library
# from google.cloud import aiplatform
import vertexai
from vertexai.language_models import TextGenerationModel
import openai
import os


# openAI Key 
openai.api_key = os.environ["API_KEY"]

# GPT-4 model 
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
 
# GPT- 3.5 model
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

# GPT-3 model 
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

# model for Text to Speech
def model_tts(prompt,voice_out):
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=prompt)
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
    with open("result/output.mp3", "wb") as out:
        out.write(response.audio_content)

# model for Speech to  Text
def model_stt(audio_file):
    transcript = openai.Audio.translate("whisper-1", audio_file)
    return transcript['text']

# model for image generation
def model_img(prompt):
  response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  return (image_url)