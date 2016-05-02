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
        print(paused[0])

        try:
            time.sleep(int(paused[1]))
        except:
            print("[p]#[/p] error")
            
        try:
            if paused[2] != "":
                print (paused[2])
        except:
            pass
    else:
        print(line)

while True:
    inp = input(":> ")
    response = kernel.respond(inp)

    if response != "":
        time.sleep(len(response) / 5)
        if "\\n" in response:
            lines = response.split(" \\n ")
            for l in lines:
                pause_in_line(l)
        else:
            pause_in_line(response)
    
    else:
        print("No message found")
