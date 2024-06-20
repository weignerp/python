import time
from pathlib import Path
import json
import azure.cognitiveservices.speech as speechsdk

transcriptions = []
filename = "D:/Hlas_003_sd.wav"


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


def recognize_from_file(file_name):
    AZURE_SPEECH_KEY = "SECRET_KEY"
    SPEECH_REGION = "REGION_NAME"
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"

    speech_config = speechsdk.SpeechConfig(
        subscription=AZURE_SPEECH_KEY,
        region=SPEECH_REGION,
        speech_recognition_language="cs-CZ",
    )
    # speech = AudioSegment.from_file("D:/Hlas_003_sd.m4a", format="m4a")
    # speech.export("D:/Hlas_003_sd.wav", format="wav")
    # audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    audio_config = speechsdk.audio.AudioConfig(filename=file_name)
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
    output_file = Path(file_name).stem + ".json"

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(transcription_json)

    print("Transcription saved to: " + output_file)


def main():
    recognize_from_file(filename)


if __name__ == "__main__":
    main()
