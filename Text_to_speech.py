import pyttsx3

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

speak('I am Abhishika Agarwal')
speak('Name of my brother is Samarpit Agarwal')