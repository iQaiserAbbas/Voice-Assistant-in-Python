import pyttsx3  # pip install pyttsx3

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
