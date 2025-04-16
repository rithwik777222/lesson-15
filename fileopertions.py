with open('random.txt','w') as file:
    file.write('this is a write mode change!')
file.close()

with open('random.txt','r') as file:
    d = file.readlines()
    print('words in this file are')
    for line in d:
        word = line.split()
        print(word)
file.close()

    