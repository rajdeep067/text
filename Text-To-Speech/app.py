from gtts import gTTS
import os

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

# Get the custom filename
filename = input("Enter the filename (with .mp3 extension): ")

# Ensure the filename has a .mp3 extension
if not filename.endswith(".mp3"):
    filename += ".mp3"

# Get the language input
print("Choose a language:")
print("1. English")
print("2. French")
print("3. Spanish")
print("4. German")
print("5. Hindi")
print("6. Bengali")
print("7. Bhojpuri")

lang_choice = input("Enter the number corresponding to your choice: ")

# Map the user's choice to the appropriate language code
language_map = {
    "1": "en",
    "2": "fr",
    "3": "es",
    "4": "de",
    "5": "hi",
    "6": "bn",  # Bengali
    "7": "bh"   # Bhojpuri
}

language = language_map.get(lang_choice, "en")  # Default to English if the choice is invalid

# Call the Speak function with the user's inputs
Speak(text, filename, language)

