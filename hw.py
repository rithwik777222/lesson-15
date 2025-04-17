with open('file1..txt','w') as file:
    file.write('this is a write mode change!')
file.close()

with open('file1..txt','r') as file:
    d = file.readlines()
    print('words in this file are')
    for line in d:
        word = line.split()
        print(word)
file.close()

nf = open('file7.txt','x')
nf.close()

import os
print("checking if file exists or not")
if os.path.exists("file4.txt"):
    os.remove("file4.txt")
else:
    print("file does not exist")

mf = open("file6.txt",'w')
mf.write("new fileeeeeee")
mf.close()

os.remove("deleting2.txt")

os.rmdir("folder")