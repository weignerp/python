import sys
import queue
import threading
from moviepy.editor import VideoFileClip


def convert_video_to_audio(file, callback_queue):
    video = VideoFileClip(file)
    audio_filename = file.replace(".mp4", ".mp3")
    video.audio.write_audiofile(audio_filename)
    callback_queue.put((audio_filename, True))


def main():
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
