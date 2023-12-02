import datetime
from Voice import talk, ChangeVolume,take_command
from functions import play,say,search,joke,SetReminder,ReadReminder,cam, startTimer,endTimer,clear_reminders

def run_jarvis(command):
    try:
        #command=take_command()
        #print(command)
        if 'play' in command:
            play(command)

        elif 'camera' in command:
            cam()

        elif 'say' in command:
            say(command)

        elif "set reminder" in command:
            talk("listening")
            NewCommand=take_command()
            SetReminder(NewCommand)

        elif 'read reminders' in command or 'read reminder' in command:
            data=ReadReminder()
            talk(data)
            print(data)       
        
        elif 'clear reminders' in command:
            clear_reminders()

        elif "start" in command and "timer" in command:
            startTimer()
            talk("The timer has started")

        elif "close" in command and "timer" in command:
            Time=endTimer()
            print(f'{Time} seconds')  
            Time=str(Time) 
            talk(f"Time taken {Time} seconds")

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)

        elif 'set volume to' in command:
            ChangeVolume(command)
 

        elif 'search' in command:
            search(command)

        elif 'joke' in command:
            joke()  

        else:
            talk('Please say the command again.')  
    except:
        pass 


