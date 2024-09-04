from gtts import gTTS
import os
from playsound import playsound

# opening the text to read the file
audiobook = open(r'emails.txt', encoding="utf8")
audiobook_text = audiobook.read()

# converting text to speech and saving it as an mp3 file
tts = gTTS(text=audiobook_text, lang='en', slow=False)  # You can change the 'lang' for different voices
tts.save("audiobook.mp3")

# # Play the generated audio file using a media player like VLC or playsound
# playsound("audiobook.mp3")

# open the mp3 file in the default mp3 player on your device, you can use either of the next lines.
# os.startfile("audiobook.mp3")
os.system("start audiobook.mp3")



# if you have a mac osx comment out the two lines above, and uncomment the following line
# os.system("open audiobook.mp3")