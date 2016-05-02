import aiml
import time

kernel = aiml.Kernel()
kernel.bootstrap(learnFiles = "std-project.xml", commands = "load aiml b")

kernel2 = aiml.Kernel()
kernel2.bootstrap(learnFiles = "std-project.xml", commands = "load aiml b")

response = "Hello!"
responseList = []
while True:
    response = kernel.respond(response).strip()
    responseList.append(response)
    for item in responseList:
        print(item)
    
    response = kernel2.respond(response).strip()
    responseList.append(response)
    for item in responseList:
        print(item)
    
    
    if response == "":
        response = "Hello!"
