import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    """
This method will allow Zira to speak, It take our voice as an argument
    """
    engine.say(audio)
    engine.runAndWait()


def greetUser():
    """
This method will always greet the user in start.
    """
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 11:
        speak("Good Morning!")

    elif hour >= 11 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("My name is Zira, I am your voice assistant. Please tell me how may I help you?")


def takeCommand():
    """
    It takes microphone input from the user and returns string output, return None in case of any problem
    """

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("how can I help?")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-UK')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    hiding error from console
        print("Speak it again please...")
        return "None"
    return query


if __name__ == "__main__":
    greetUser()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching in Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open university website' in query:
            webbrowser.open("bahria.edu.pk")

        elif 'open stack overflow' or 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'F:\\MP3'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open chrome' in query:
            codePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)

        elif 'open git' in query:
            codePath = "C:\\Program Files\\Git\\git-bash.exe"
            os.startfile(codePath)

        elif 'quit' or 'shut' in query:
            speak("Thanks for giving me your time")
            exit()
