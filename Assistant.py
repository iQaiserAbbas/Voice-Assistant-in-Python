import pyttsx3  # pip install pyttsx3
import datetime
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  #getting details of current voice
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    """
This method will allow Zira to speak, It take our voice as an argument
    """
    engine.say(audio)
    engine.runAndWait() #Without this command, speech will not be audible to us.


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
            
        elif 'quit' in query:
            exit()
