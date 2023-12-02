from JARVIS import run_jarvis
from Voice import take_command

#print("Hi, this is Alexa. How can I help you today?")
#say("Hi, this is Alexa. How can I help you Today?")

while True:
    command=take_command()
    command=str(command)
    print(command)
    while command!="None":
        if 'stop' in command:
            quit()
        else:    
            run_jarvis(command)


