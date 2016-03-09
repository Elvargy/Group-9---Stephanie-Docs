from os import listdir
from os.path import isfile, join


path = input("Directory >: ")
file_list = [f for f in listdir(path) if isfile(join(path, f))]

f = open("filesindir.txt", 'w')
for file in file_list:
    string = "<learn>standard/" + file + "</learn>\n"
    print(string)
    f.write(string)

f.close()
