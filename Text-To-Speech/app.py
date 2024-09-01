from gtts import gTTS
import os
from googletrans import Translator

# Function to convert text to speech and save it as an audio file
def Speak(text, filename, language):
    try:
        # Create a gTTS object with the specified language
        tts = gTTS(text=text, lang=language)
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

# Ask the user in which language the text should be translated
print("In which language do you want to convert the text?")
print("1. English")
print("2. French")
print("3. Spanish")
print("4. German")
print("5. Hindi")
print("6. Bengali")
print("7. Bhojpuri")

translate_choice = input("Enter the number corresponding to your choice: ")

# Map the user's choice to the appropriate language code
translate_map = {
    "1": "en",
    "2": "fr",
    "3": "es",
    "4": "de",
    "5": "hi",
    "6": "bn",
    "7": "bh"
}

translate_language = translate_map.get(translate_choice, "en")  # Default to English if the choice is invalid

# Translate the text
translator = Translator()
translated = translator.translate(text, dest=translate_language).text
print(f"Translated Text: {translated}")

# Get the custom filename
filename = input("Enter the filename (with .mp3 extension): ")

# Ensure the filename has a .mp3 extension
if not filename.endswith(".mp3"):
    filename += ".mp3"

# Ask the user in which language the text should be spoken
print("In which language do you want the text to be spoken?")
lang_choice = input("Enter the number corresponding to your choice: ")

# Get the language for speech
language = translate_map.get(lang_choice, "en")  # Default to English if the choice is invalid

# Call the Speak function with the translated text
Speak(translated, filename, language)

