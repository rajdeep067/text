from gtts import gTTS
import os

def Speak(text, filename):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        print(f"Audio has been saved to '{filename}'")
        # Check if the file was actually created
        if os.path.exists(filename):
            print(f"File '{filename}' exists in the container.")
        else:
            print(f"File '{filename}' was not created.")
    except Exception as e:
        print("An error occurred:", e)
        print("Current directory:", os.getcwd())
        print("Files in directory:", os.listdir())

# Get the text input
text = input("Enter your text now: ")

# Get the custom filename
filename = input("Enter the filename (with .mp3 extension): ")

# Ensure the filename has a .mp3 extension
if not filename.endswith(".mp3"):
    filename += ".mp3"

Speak(text, filename)
