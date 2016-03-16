import aiml
import os

kernel = aiml.Kernel()


print ("Choose a brain file:")
print ("[1] Standard")
print ("[2] Test")
print ("[3] Both")
print ("[4] None\n")

invalidSelection = True
path = ""

while invalidSelection:
    
    print("Please select a number between 1 and 4")
    
    inp = input(": ")
    
    if inp == "1":
        path = "brains\\standard.brn"
        
        if os.path.isfile(path):
            kernel.bootstrap(brainFile = path)
        else:
            kernel.bootstrap(learnFiles = "std-all.xml", commands = "load aiml b")
            kernel.saveBrain(path)

        invalidSelection = False
    
    elif inp == "2":
        path = "brains\\test.brn"
        
        if os.path.isfile(path):
            kernel.bootstrap(brainFile = path)
        else:
            kernel.bootstrap(learnFiles = "std-test.xml", commands = "load aiml b")
            kernel.saveBrain(path)

        invalidSelection = False
    
    elif inp == "3":
        path = "brains\\both.brn"
        
        if os.path.isfile(path):
            kernel.bootstrap(brainFile = path)
        else:
            kernel.bootstrap(learnFiles = "std-test.xml", commands = "load aiml b")
            kernel.bootstrap(learnFiles = "std-all.xml", commands = "load aiml b")
            kernel.saveBrain(path) 
        
        invalidSelection = False

    elif inp == "4":
        print ("No brain loaded")
        invalidSelection = False

    elif inp == "5":
        kernel.bootstrap(learnFiles = "std-test.xml", commands = "load aiml b")
        invalidSelection = False



class Commands:
    
    def command_ping(self):
        print("ping")
    
    def command_quit(self):
        exit(0)
        
    def command_learntest(self):
        kernel.bootstrap(learnFiles = "std-test.xml", commands = "load aiml b")
        
    def command_learnstandard(self):
        kernel.bootstrap(learnFiles = "std-all.xml", commands = "load aiml b")
            
    def command_save(self):
        if os.path.isfile(path): 
            kernel.saveBrain(path)

    def command_(self):
        bot_response = kernel.respond(message)

c = Commands()

while True:
    message = input(">>: ")
    try:
        command = getattr(c, "command_" + message)()
    except:
        print (kernel.respond(message))


