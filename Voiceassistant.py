# Importing Modules
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia  

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    print("Hey, Welcome to Riya's Voice assistant model")
    speak("Hey, Welcome to Riya's Voice assistant model")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    print(Time)
    speak(f"The Current time is {Time}. Thank you")

def wiki():
    query = "Iphone"
    result = wikipedia.summary(query, sentences=3) 
    speak("You've asked a question?")
    speak(f"I got it, your question is about {query}! Here are your results")
    speak("According to Wikipedia")
    print(result)
    speak(result)


def takecommand():
    r = sr.Recognizer()  # it will try to recognize the voice
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1  # it will wait for a second and convert it to text
        audio = r.listen(source)
    
    try:
        print("Wait for a sec. I'm recognising......")
        query = r.recognize_google(audio, language='en-in')  # Correct parameter name
        print(f"Riya Said: {query}\n")
        speak(f"You said: {query}")
        

    except Exception as e:
        print(e)
        print("Try again!")
        speak("Didn't get that, try again")
        return "None"
    return query

# Calling the function 
time()
wiki()
takecommand()
