#Importing the module to read the path names of all your files containing chats
import sys
#Greeting the user
print("""A warm welcome to the Instagram Chat Message Counter.\nThis program will tell you the number of messages you have exchanged among all chats including requests.\nThe input is a file containing all the absolute pathnames of your chat files.""")
#Opening the file with read access
f = open(sys.argv[1], "r")
#Assigning the contents of the file to a variable "g"
g = f.readlines()
#A counter variable to count the toal messages
mess = 0
#Iterating through the lines of the code to find a specific sequence
for i in g:
    #Getting rid of the new line characters
    i = i.replace("\n", "").replace('"', "")
    #Opening a file given the path
    j = open(i, "r")
    #Reading each individual line and assigning to a variable "k"
    k = j.readlines()
    #Creating an initial counter variable
    c = 0
    #Iterating through the lines of the code to find a specific sequence
    for l in k:
        #The next statement is optional, but it helps to make the data cryptic and challenging to read
        print(l[::-1].swapcase().replace("N", "$").replace("A", "#").split())
        #Incrementing the message count for the specific chat
        c += l.count("sender_name")
        #Incrementing the message count for all chats thus far
        mess += l.count("sender_name")
    #Printing out the final number of messages 
    print("There are", c, "messages between you and the interested party!")
    #Printing blank line
    print("\n")
#Printing all the messages, adding all the chats and requests together!
print("You have", mess, "total sent and received messages on Instagram, including requests!")
