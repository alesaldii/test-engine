"""
sudo apt install python3-pip
pip3 install SpeechRecognition
"""
import speech_recognition as sr

def recognize_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Listen for user input
        audio = recognizer.listen(source)

    # Use Google Web Speech API to recognize speech
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Sorry, an error occurred during the request: {e}")

if __name__ == "__main__":
    recognized_text = recognize_speech()
    if recognized_text:
        print("You said:", recognized_text)
