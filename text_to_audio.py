from gtts import gTTS

def text_to_audio(text, output_file):
    tts = gTTS(text)
    tts.save(output_file)

if __name__ == "__main__":
    input_text = "text.txt"
    output_file = "output_audio.mp3"

    text_to_audio(input_text, output_file)
