nf = open('random3.txt','x')
nf.close()

import os
print("checking if file exists or not")
if os.path.exists("random2.txt"):
    os.remove("random2.txt")
else:
    print("file does not exist")

mf = open("my_file.txt",'w')
mf.write("new fileeeeeee")
mf.close()

os.remove("deleting.txt")

os.rmdir("folder")