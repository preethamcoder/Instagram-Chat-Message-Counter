#Opening the file and reading its contents
f = open("path_of_file", "r")
#Assigning the contents of the file to a variable "g"
g = f.readlines()
#Creating an initial counter variable
c = 0
#Iterating through the lines of the code to find a specific sequence
for i in g:
    #The next statement is optional, but it helps to make the data cryptic and challenging to read
    print(i[::-1].swapcase().replace("NAM", "###").split())
    #Incrementing the message count
    c += i.count("sender_name")
#Printing out the final number of messages 
print("There are", c, "messages between you and the interested party!")
