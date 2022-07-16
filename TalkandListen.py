import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()  # to understand what the user is saying.
engine = pyttsx3.init()  # text to speech initialized.Engine speaks the text out

# this speaks the text sent as a parameter
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Gets the user's speech
def get_info():
    try:
        with sr.Microphone() as source:  # laptop's mic is the source for speech.
            print('Listening...')
            talk('Now Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)  # speech to text function
            print(info, '\n')
            return info.lower()  # converts to lower case
    except:
        pass

