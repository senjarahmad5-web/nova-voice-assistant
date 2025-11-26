import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as ts
import musiclibrary
import requests


r = sr.Recognizer()
ttsx = ts.init()
newsapi = "c5917392d29447119d9b1ad705e54b62"

def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()

def processCmd(c):
    if "open google" in c.lower():
        wb.open("https://www.google.com")
    elif "open facebook" in c.lower():
        wb.open("https://www.facebook.com")
    elif "open linkedin" in c.lower():
        wb.open("https://in.linkedin.com")
    elif "open youtube" in c.lower():
        wb.open("https://www.youtube.com")
    elif "open gmail" in c.lower():
        wb.open("https://mail.google.com/mail/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        wb.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            print("Request successful!")
            
            data = r.json()  # Convert response to dictionary

            # Extract the articles
            articles = data.get('articles', [])

            # print the headlines
            for article in articles:
                speak(article['title'])

    else:
        # Let OpenAi handle the request
        pass


if __name__ == "__main__":
    speak("Initializing Nova Assistant....")
    # Listen for the wake word "SENJAR"
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        

        print("Recognizing...") #It will show us how much time it takes to listen and recognize.

        # recognize speech using Google Speech Recognition
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "nova"):
                speak("Yes, How may I help you today?")
                # Listen for command
                with sr.Microphone() as source:
                    print("Nova Assistant Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCmd(command)


        except Exception as e:
            print("Error; {0}".format(e))


