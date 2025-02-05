import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import os
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Sonu, skilled in general tasks like Alexa and Google Cloud."},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content

def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in command.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com")
    elif "open snapchat" in command.lower():
        webbrowser.open("https://snapchat.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in command.lower():
        api_key = os.getenv("5e4d92dcfe074ad6b5922b2ebb28e454")
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
    else:
        output = aiProcess(command)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Sonu...")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                word = recognizer.recognize_google(audio)
                if word.lower() == "sonu":
                    speak("Ya")
                    with sr.Microphone() as source:
                        print("Sonu Active...")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)
        except Exception as e:
            print("Error: {0}".format(e))
