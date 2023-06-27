# Import the Speech-to-Text client library
# from google.cloud import aiplatform
# import vertexai
# from vertexai.language_models import TextGenerationModel
from google.cloud import speech
from google.cloud import texttospeech

def model_tts(prompt,voice):
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=prompt)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="es-US",
        name="es-US-Studio-B",
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        speaking_rate=1
    )
    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )
    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        return ('Audio content written to file "output.mp3"')


def model_stt(audio_content):
    # Instantiates a client
    client = speech.SpeechClient()
    # The content of the audio file to transcribe
    audio_content = audio_content
    # transcribe speech
    audio = speech.RecognitionAudio(content=audio_content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=24000,
        language_code="en-US",
        model="default",
        audio_channel_count=1,
        enable_word_confidence=True,
        enable_word_time_offsets=True,
    )

    # Detects speech in the audio file
    operation = client.long_running_recognize(config=config, audio=audio)

    # print("Waiting for operation to complete...")
    response = operation.result(timeout=90)
    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

