import os
import aiml
import fbchat
import random

kernel = aiml.Kernel()
kernel.bootstrap(learnFiles = "std-project.xml", commands = "load aiml b")

while True:
    inp = input(":> ")
    response = kernel.respond(inp)
                    
    if response != "":
        print(response)
    else:
        print("No message found")
    


