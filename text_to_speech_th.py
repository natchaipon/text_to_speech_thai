import pyttsx3
engine = pyttsx3.init()

TH_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_THAI"

engine.setProperty('volume', 0.9)  # Volume 0-1
engine.setProperty('rate', 120)  #148

engine.setProperty('voice', TH_voice_id)
engine.say('กินข้าวหรือยัง')

engine.runAndWait()