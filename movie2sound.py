from moviepy.editor import VideoFileClip
from pathlib import Path
import sys
import threading
import queue
import time
import speech_recognition as sr
import os
from pdf2docx import Converter
import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment
import json


def convert_video_to_audio(file, callback_queue):
    video = VideoFileClip(file)
    audio_filename = file.replace(".mp4", ".mp3")
    video.audio.write_audiofile(audio_filename)
    callback_queue.put((audio_filename, True))

    # obtain path to "english.wav" in the same folder as this script

    AUDIO_FILE = Path(__file__).parent / "english.wav"
    # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
    # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Microsoft Azure Speech
    AZURE_SPEECH_KEY = "d04b64bd9c814b4fa15319c5e0a75c41"  # Microsoft Speech API keys 32-character lowercase hexadecimal strings
    SERVICE_REGION = "eastus"
    try:
        print(
            "Microsoft Azure Speech thinks you said "
            + r.recognize_azure(audio, key=AZURE_SPEECH_KEY, location=SERVICE_REGION)
        )
    except sr.UnknownValueError:
        print("Microsoft Azure Speech could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Microsoft Azure Speech service; {0}".format(
                e
            )
        )


# Create an empty list to store the transcription results
transcriptions = []


# Define an event handler for continuous recognition
def continuous_recognition_handler(evt):
    if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
        transcriptions.append(
            {
                "duration": evt.result.duration
                / 10**7,  # convert from nanoseconds to seconds
                "offset": evt.result.offset
                / 10**7,  # convert from 1/100 nanoseconds to seconds
                "text": evt.result.text,
            }
        )


def recognize_from_file():
    AZURE_SPEECH_KEY = "d04b64bd9c814b4fa15319c5e0a75c41"
    SPEECH_REGION = "eastus"
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    """ subscription=os.environ.get(AZURE_SPEECH_KEY),
        region=os.environ.get(SPEECH_REGION), """
    speech_config = speechsdk.SpeechConfig(
        subscription=AZURE_SPEECH_KEY,
        region=SPEECH_REGION,
        speech_recognition_language="cs-CZ",
    )
    # speech = AudioSegment.from_file("D:/Hlas_003_sd.m4a", format="m4a")
    # speech.export("D:/Hlas_003_sd.wav", format="wav")
    # audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    audio_config = speechsdk.audio.AudioConfig(filename="D:/Hlas_003_sd.wav")
    speech_config.output_format = speechsdk.OutputFormat.Detailed
    speech_config.request_word_level_timestamps()

    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_config, language="cs-CZ"
    )

    print("Speak into your microphone.")
    # speech_recognition_result = speech_recognizer.recognize_once_async().get()
    # speech_recognition_result = result = speech_recognizer.recognize_once()
    # Start continuous recognition
    speech_recognizer.recognized.connect(continuous_recognition_handler)
    speech_recognizer.start_continuous_recognition()

    # Wait for the recognition to complete
    timeout_seconds = (
        12  # Set a timeout value (in seconds) based on your audio file length
    )
    timeout_expiration = time.time() + timeout_seconds

    while time.time() < timeout_expiration:
        time.sleep(1)  # Adjust the sleep duration as needed

    # Stop continuous recognition
    speech_recognizer.stop_continuous_recognition()

    # Combine transcriptions into a single string
    transcription_json = json.dumps(transcriptions, indent=4, ensure_ascii=False)

    # Write the transcription to a file
    output_file = "d:/Hlas_003_sd_transcription.txt"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(transcription_json)

    print("Transcription saved to: " + output_file)


"""
    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))

        # Time units are in hundreds of nanoseconds (HNS), where 10000 HNS equals 1 millisecond
        print("Offset: {}".format(result.offset))
        print("Duration: {}".format(result.duration))

        # Now get the detailed recognition results from the JSON
        json_result = json.loads(result.json)

        # The first cell in the NBest list corresponds to the recognition results
        # (NOT the cell with the highest confidence number!)
        print(
            "Detailed results - Lexical: {}".format(json_result["NBest"][0]["Lexical"])
        )
        # ITN stands for Inverse Text Normalization
        print("Detailed results - ITN: {}".format(json_result["NBest"][0]["ITN"]))
        print(
            "Detailed results - MaskedITN: {}".format(
                json_result["NBest"][0]["MaskedITN"]
            )
        )
        print(
            "Detailed results - Display: {}".format(json_result["NBest"][0]["Display"])
        )

        # Print word-level timing. Time units are HNS.
        words = json_result["NBest"][0]["Words"]
        print("Detailed results - Word timing:\nWord:\tOffset:\tDuration:")
        for word in words:
            print(f"{word['Word']}\t{word['Offset']}\t{word['Duration']}")

        # You can access alternative recognition results through json_result['NBest'][i], i=1,2,..

    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print(
            "No speech could be recognized: {}".format(
                speech_recognition_result.no_match_details
            )
        )
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
"""


def convertPDFtoDocx(pdf_file):
    cv = Converter(pdf_file)
    doc_file = pdf_file.replace(".pdf", ".docx")
    cv.convert(doc_file)
    cv.close()


def main():

    if False:
        pdf_file = "D:/Users/PWeigner/Downloads/bp.pdf"
        convertPDFtoDocx(pdf_file)
        sys.exit(0)

    recognize_from_file()
    # exit code
    sys.exit(0)

    # list all arguments
    print(sys.argv)

    if len(sys.argv) <= 2:
        print("Usage: python movie2sound.py <filepath>")
        return
    filepath = sys.argv[1]
    callback_queue = queue.Queue()
    thread = threading.Thread(
        target=convert_video_to_audio, args=(filepath, callback_queue)
    )
    thread.start()
    while True:
        audio_filename, success = callback_queue.get()
        if success:
            print(f"Conversion finished, saved as {audio_filename}")
            break


if __name__ == "__main__":
    main()
