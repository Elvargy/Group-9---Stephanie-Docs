# For some documentation on this API:
#    https://github.com/Schmavery/facebook-chat-api/blob/master/DOCS.md
# Although it's for the Java version it is still useful
# This just means we need to try and convert the code to Python


import fbchat

# Initilaise the API
api = fbchat.Client("USERNAME", "PASSWORD")

# Start the while loop which listens for events
api.listen()
