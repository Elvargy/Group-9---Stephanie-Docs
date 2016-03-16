import aiml
import os

kernel = aiml.Kernel()

#if os.path.isfile("bot_brain.brn"):
#    kernel.bootstrap(brainFile = "bot_brain.brn")
#else:
#kernel.bootstrap(learnFiles = "std-test.xml", commands = "load aiml b")
#    kernel.saveBrain("bot_brain.brn")

#kernel.bootstrap(learnFiles = "std-test.xml", commands = "load aiml b")


print ("Choose a brain file:")
print ("[1] Standard")
print ("[2] Test\n")
if input("Brain #: ") == "1":
    kernel.bootstrap(brainFile = "standard.brn")
else:
    kernel.bootstrap(brainFile = "test.brn")


class Response:
    def command_ping(self):
        print("ping")
    
    def command_quit(self):
        exit(0)
        
    def command_learntest(self):
        kernel.bootstrap(learnFiles = "std-test.xml", commands = "load aiml b")
        
    def command_learnstandard(self):
        kernel.bootstrap(learnFiles = "std-all.xml", commands = "load aiml b")
            
    def command_save(self):
        kernel.saveBrain("bot_brain.brn")

    def command_(self):
        bot_response = kernel.respond(message)

r = Response()

while True:
    message = input(">>: ")
    try:
        command = getattr(r, "command_" + message)()
    except:
        print (kernel.respond(message))


