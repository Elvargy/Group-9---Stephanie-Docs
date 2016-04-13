import os
import aiml
import fbchat
import random

kernel = aiml.Kernel()

print ("Choose a brain file:")
print ("[1] Standard")
print ("[2] Project")
print ("[3] Both")
print ("[4] None\n")

invalidSelection = True
path = "notafile.brn"

while invalidSelection:
    
    print("Please select a number between 1 and 4")
    
    inp = input(": ")
    
    if inp == "1":
        path = "brains\\_standard.brn"
        
        if os.path.isfile(path):
            kernel.bootstrap(brainFile = path)
        else:
            kernel.bootstrap(learnFiles = "std-standard.xml", commands = "load aiml b")
            kernel.saveBrain(path)

        invalidSelection = False
    
    elif inp == "2":
        path = "brains\\_project.brn"
        
        if os.path.isfile(path):
            kernel.bootstrap(brainFile = path)
        else:
            kernel.bootstrap(learnFiles = "std-project.xml", commands = "load aiml b")
            kernel.saveBrain(path)

        invalidSelection = False
    
    elif inp == "3":
        path = "brains\\_both.brn"
        
        if os.path.isfile(path):
            kernel.bootstrap(brainFile = path)
        else:
            kernel.bootstrap(learnFiles = "std-project.xml", commands = "load aiml b")
            kernel.bootstrap(learnFiles = "std-standard.xml", commands = "load aiml b")
            kernel.saveBrain(path) 
        
        invalidSelection = False

    elif inp == "4":
        print ("No brain loaded")
        invalidSelection = False

    elif inp == "5":
        print(";)")
        kernel.bootstrap(learnFiles = "std-project.xml", commands = "load aiml b")
        
        invalidSelection = False



class Commands:

    def __init__(self, path):
        self.path = path
        
    def command_ping(self):
        # Tests responsiveness
        print("ping")
    
    def command_quit(self):
        # Quits the bot
        exit(0)
        
    def command_learntest(self):
        # Loads the aiml files for the project folder
        kernel.bootstrap(learnFiles = "std-project.xml", commands = "load aiml b")
        
    def command_learnstandard(self):
        # Loads the aiml files for the standard folder
        kernel.bootstrap(learnFiles = "std-standard.xml", commands = "load aiml b")
            
    def command_save(self):
        # Saves the currently loaded aiml files to the brain file
        # assuming one was selected at the beginning)
        # if not then you are asked to name the new brain file
        
        if os.path.isfile(self.path): 
            kernel.saveBrain(self.path)
        else:
            print("Name new brain file")
            inp = input(": ")
            self.path = "brains\\%s.brn" % inp
            kernel.saveBrain(self.path)
            
            
    def command_tlr(self):
        # Test location responses
        
        inp = ""
        for question in questionList:
            print(question)
            print(kernel.respond(question))
            print()
                                      
    def command_(self):
        bot_response = kernel.respond(message)

c = Commands(path)

locationList = [
    "Student Union",
    "Minerva Building",
    "Main Building"
    ]

questionList = []
for location in locationList:
    # Directions
    questionList.append("Directions %s" % location)
    questionList.append("Can you tell me directions %s?" % location)
    
    questionList.append("Directions to %s" % location)
    questionList.append("Can you tell me directions to %s?" % location)
    
    questionList.append("Directions for %s" % location)
    questionList.append("Can you tell me directions for %s?" % location)
    
    questionList.append("Get to %s" % location)
    questionList.append("Can you tell me how to get to %s?" % location)
    
    questionList.append("Where is %s?" % location)
    questionList.append("Hey, where is %s?" % location)
    questionList.append("Can you tell me where %s is?" % location)
    
    questionList.append("Where's %s?" % location)
    questionList.append("Hey, where's %s?" % location)

    # About
    questionList.append("About %s" % location)
    questionList.append("Can you tell me about %s?" % location)
    
    questionList.append("What is %s?" % location)
    questionList.append("Hey, what is %s?" % location)
    questionList.append("Can you tell me what %s is?" % location)

    questionList.append("Information for %s" % location)
    questionList.append("Can you give me information for %s?" % location)


fallback = [
    "Sorry I didn't understand that, could you please clarify your question?",
    "I don't understand",
    "Suck my dick you pixie wanker"
    ]

api = fbchat.Client("13393724@students.lincoln.ac.uk", "group9")

while True:
    metadata = api.listen()

    if metadata != None :
        if 'message' in metadata:
            mid     = metadata['message']['mid']
            message = metadata['message']['body']
            fbid    = metadata['message']['sender_fbid']
            name    = metadata['message']['sender_name']
            
            if 'thread_fbid' in metadata['message']:
                tid     = metadata['message']['thread_fbid']
            else:
                tid = None
        
            print (mid)
            print (message)
            print (fbid)
            print (name)
            print (metadata)            

            if tid != None and fbid != 100011744288479:
                try:
                    command = getattr(c, "command_" + message)()
                    response = ""
                except:
                    response = kernel.respond(message)
                
                if response != "":
                    print (response)
                    api.send(tid, response)
                else:
                    api.send(tid, random.choice(fallback))
    
            else:
                print("None")
    


