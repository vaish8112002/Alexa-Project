import pyttsx3 #pip install pyttsx3
import speech_recognition as sr   #pip install speech recognition
import datetime
import wikipedia   #pip install wikipedia
import webbrowser
import os
import smtplib
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    speak("Hello, I am alexa ,Vaishnavi how may i help you ? ")
    
def takeCommand():
    #It takes microphone input from the user and returns string output
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold =1
        audio = r.listen(source)
    
    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        #print(e)
        print("Sorry say it again please....")
        return "None"
    return query

def get_random_advice():
    res =requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

if __name__=="__main__":
    wishme()
    #if 1:
    query =takeCommand().lower()
    
    
    #logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query=query.replace("wikipedia", "")
        results=wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        
    elif 'hello' in query:
        speak("yes shraddha how may i help u!!")
        
    elif 'open google' in query:
        webbrowser.open("https://www.google.com/")
        
        
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")   
        
        
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    
    elif "advice" in query:
        speak(f"Here's an advice for you")
        advice=get_random_advice()
        speak(advice)
        speak("For your convenience, I am printing it on the screen buddy")
        print(advice)
        
    elif 'the time' in query:
        strTime= datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Ok The time is {strTime}")
    
    elif 'how are you ' in query:
        speak("I am good what about you !!!")
    
        
    elif 'logout' in query:
        speak("Thank You!!!!!!!!!!!")
        exit()