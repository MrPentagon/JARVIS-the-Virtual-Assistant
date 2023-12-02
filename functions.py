from Voice import talk
import pywhatkit
import wikipedia
import pyjokes
import cv2
import time

def play(command):
    song=command.replace('play','')
    talk('playing ' + song)
    pywhatkit.playonyt(song)

def say(command):
    say=command.replace('say','')   
    talk(say)

def search(command):
    search = command.replace('search', '')
    info = wikipedia.summary(search,1)
    print(info)
    talk(info)

def joke():
    joke=pyjokes.get_joke()  
    print("joke: ",joke)
    talk(joke)

def SetReminder(command):
    reminder=command.replace('set reminder ','')
    print(reminder)
    f=open('Reminder.txt','w')
    f.write(reminder)
    f.close

def ReadReminder():
    #print("this func works")
    f=open('Reminder.txt','r')
    data=f.read()
    f.close
    return data

def clear_reminders():
    f=open('Reminder.txt','w')
    f.writelines("")
    f.close()
    talk("All Reminders cleared")

def cam():
    cam = cv2.VideoCapture(0) 
    while cam.isOpened():
        ret, frame1 = cam.read()
        if cv2.waitKey(10) == ord('q'):
            break
        cv2.imshow('Alexa Cam', frame1)
      
def startTimer():
    global start_time
    start_time=time.time()
    
def endTimer():
    end_time=time.time()-start_time
    return int(end_time)

          