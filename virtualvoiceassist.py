import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
def talk(text):
    engine.say(text)          
    engine.runAndWait()

def take_command():
  try:
    with sr.Microphone() as source:
        print("Listening............")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa','')
            print(command)
  except:
    command = "Sorry";
    pass
  return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in  command:
        song = command.replace('play','')
        talk('Playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Current time is ' + time)
        print('Current time is '+ time)
    elif 'who is' in command:
        person = command.replace('who is ','')
        info = wikipedia.summary(person,1)
        talk(info)
    elif 'thanks' in command:
        talk('You are welcome')
    elif 'joke' in command:
       joke = pyjokes.get_joke()
       print(joke)
       talk(joke)
    elif 'bye' in command:
        talk('Bye Durga')
    else:
        talk('Please say the command again')

while True: 
  run_alexa()
