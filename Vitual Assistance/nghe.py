import speech_recognition
import distutils
robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot: Listening...")
    audio = robot_ear.listen(mic)
try:        
    you = robot_ear.recognize_google(audio)
except:
    you =""
print("You: " + you)