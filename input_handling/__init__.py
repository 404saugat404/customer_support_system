import speech_recognition as sr

def audio_to_text(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError:
        return "Sorry, my speech service is down."

# Example usage
if __name__ == "__main__":
    text_input = audio_to_text("path_to_audio_file.wav")
    print(text_input)