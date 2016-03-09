# General How-To:

Run 'runbot.bat' to start the bot. 
(The bot could also be run from the 'bot.py' file through the Shell if you'd prefer)

.

The 'std-test.xml' and 'std-all.xml' files will load the aiml files into the bot using the <learn> tags.
Additional aiml file can be implemented by adding another '<learn>file.aiml</learn>' line to these .xml files.

I added extra python commands that can be used in addition the the general aiml responses.
The bot will inherit aiml files from 'std-test.xml' to begin with but I have added commands to use the standard folder too:

.

Commands:

'ping' - Returns a 'ping' message from the bot to test responsiveness

'quit' - Quits the 'bot.py' program

'learntest' - Adds aiml files from 'std-test.xml' (The test folder)

'learnstandard' - Adds aiml files from 'std-all.xml' (The standard folder)

'save' - Saves the current aiml files being used by the bot to the 'brain.brn' file allowing for a quicker startup

.

The 'getfiles.py' file is a simple program I made to output the file names of a folder into a text file. Literally made this because I'm lazy and wanted an easy way to add all the aiml files to 'std-all.xml'   lamo exdee
