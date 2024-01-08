# Importing Modules
import pyttsx3
import speech_recognition as sr
import wikipedia  

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wiki(query=""):
    print("Hey, Welcome to Riya's Voice assistant model")
    speak("Hey, Welcome to Riya's Voice assistant model")
    
    if not query:
        speak("What would you like to search?")
        print("What would you like to search?")
        query = takecommand()  # Get the user's search query
    
    result = wikipedia.summary(query, sentences=2) 
    speak(f"Here are your results about{query}")
    speak("According to Wikipedia")
    print(result)
    speak(result) # Adding this line to make the assistant speak the Wikipedia result

def takecommand():
    r = sr.Recognizer()  # it will try to recognize the voice
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1  # it will wait for a second and convert it to text
        audio = r.listen(source)
    
    try:
        print("Wait for a sec. I'm recognising......")
        query = r.recognize_google(audio, language='en-in')  # Correct parameter name
        print(f"You said: {query}")
        return query

    except Exception as e:
        print(e)
        print("Try again!")
        speak("Didn't get that, try again")
        return "None"

# Calling the function 
wiki()
