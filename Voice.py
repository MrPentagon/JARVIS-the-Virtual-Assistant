import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

volume=engine.getProperty('volume')
#print(volume)
listener = sr.Recognizer()

#engine.setProperty('volume',level)
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 200)     # setting up new voice rate


def ChangeVolume(command):
    command=command.replace("set volume to","")
    if 'zero' in command or 'mute' in command:
        level=0.0
    elif 'one' in command:
        level=1.0
    elif'two' in command:
        level=2.0
    elif 'three' in command:
        level=3.0
    elif 'four' in command:
        level=4.0
    elif 'five' in command:
        level=5.0
    elif 'six' in command:
        level=6.0
    elif 'seven' in command:
        level=7.0
    elif 'eight' in command:
        level=8.0
    elif 'nine' in command:
        level=9.0
    elif '10' in command:
        level=10.0
        
    else:
        print("Incorrect input")
        talk("Kindly Repeat")
    level=level/10   
    engine.setProperty('volume',level)
    talk(f"The volume is now {int(level*10)}")
    print(f"The Volume is {level*10} ")                                                                    



def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    #global command
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            print("working")
            command = listener.recognize_google(voice) 
            print("working")
            command = command.lower() 
            if 'alexa' in command:
                command = command.replace('alexa', '')
                #print(command)
            return command                
    except:
        print("No sound Detected")
        #talk('No Microphone Detected')
    return command 

