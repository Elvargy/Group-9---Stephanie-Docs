import os
import aiml
import fbchat
import random
import time

kernel = aiml.Kernel()
kernel.bootstrap(learnFiles = "std-project.xml", commands = "load aiml b")

while True:
    inp = input(":> ")
    response = kernel.respond(inp)

    time.sleep(len(response) / 5)

    if response != "":
        print(response)
    else:
        print("No message found")
    



