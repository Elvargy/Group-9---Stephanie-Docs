import os
import aiml
import fbchat
import random

kernel = aiml.Kernel()
kernel.bootstrap(learnFiles = "std-project.xml", commands = "load aiml b")

fallback = [
    "Sorry I didn't understand that, could you please clarify your question?",
    "I don't understand",
    "Suck my dick you pixie wanker"
    ]

while True:
    inp = input(":> ")
    response = kernel.respond(inp)
                    
    if response != "":
        print(response)
    else:
        print(random.choice(fallback))
    


