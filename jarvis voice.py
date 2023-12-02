import pyttsx3

def speak(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',150)
    engine.say(text)
    engine.runAndWait
speak("Hello world")    