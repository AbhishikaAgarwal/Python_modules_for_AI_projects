import speech_recognition as sr
def take_cmd():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold= 1
        audio = r.listen(source)
    try:
        print("Recognizing the voice")
        query = r.recognize_google(audio, language="en-in")
        print(query)
    except Exception as e:
        print(e)
        print("Say it clearly.....")
    return query
while True:
    take_cmd()