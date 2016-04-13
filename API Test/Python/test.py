# For some documentation on this API:
#    https://github.com/Schmavery/facebook-chat-api/blob/master/DOCS.md
# Although it's for the Java version it is still useful
# This just means we need to try and convert the code to Python


import fbchat

# Initilaise the API
api = fbchat.Client("13393724@students.lincoln.ac.uk", "group9")

# Start the while loop which listens for events
while True:
    metadata = api.listen()

    if metadata != None:
        mid     = metadata['message']['mid']
        message = metadata['message']['body']
        fbid    = metadata['message']['sender_fbid']
        name    = metadata['message']['sender_name']
    
        print(mid)
        print(message)
        print(fbid)
        print(name)

        api.send(fbid, message) 
    else:
        print("None")
