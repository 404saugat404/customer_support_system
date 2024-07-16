from gtts import gTTS
import os

def text_to_audio(text, output_file_path):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file_path)

# Example usage
if __name__ == "__main__":
    text_to_audio("Your account balance is $1,234.56.", "response_audio.mp3")
    os.system("start response_audio.mp3")
