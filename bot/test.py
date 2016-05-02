import os
import aiml
import time
import fbchat
import random

kernel = aiml.Kernel()
kernel.bootstrap(learnFiles = "std-project.xml", commands = "load aiml b")

def pause_in_line(line):
    if "[p]" in line:
        paused = line.split("[p]")
        
        time.sleep(len(paused[0]) / 6.5)
        print(paused[0])

        try:
            time.sleep(int(paused[1]))
        except:
            print("[p]#[/p] error")
    else:
        time.sleep(len(line) / 6.5)
        print(line)
        
fallthrough = [
        "I'm sorry, I don't understand what you mean...",
        "I'm not sure what you mean by that",
        "Can you explain what you mean?",
        "Could you rephrase that?",
        "I'm not sure I know about that.",
        "What do you mean?",
        "You're not making any sense",
        "Do you actually have a question?",
        "I can't understand you",
        "Is this even English?"
    ]
fallen = 0

responsesList = []
questionsList = []

while True:
    inp = input(":> ")
    response = kernel.respond(inp)
    
    if response in fallthrough:
        fallen += 1
    else:
        fallen = 0

        if response in responsesList:
            response = kernel.respond("23165498649878498")
        else:
            responsesList.append(response)

    if fallen > 3:
        continue
    elif fallen == 3:
        response = kernel.respond("92759827359872985")
        
    if response != "":
        if "\\n" in response:
            lines = response.split(" \\n ")
            for l in lines:
                pause_in_line(l)
        else:
            pause_in_line(response)        
    else:
        print("No message found")

    



        
