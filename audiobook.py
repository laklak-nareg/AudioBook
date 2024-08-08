import pyttsx3

audiobook = open(r"example.txt")
audiobook_text=audiobook.readlines()
engine = pyttsx3.init()
for i in audiobook_text:
    engine.say(i)
    engine.runAndWait()