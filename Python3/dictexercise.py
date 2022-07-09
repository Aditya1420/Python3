#Creating dictionary of linux commands and adding meaning of the words

words={"pwd":"Will show present directory",
       "ls":"list all items in directory",
       "cd":"to change directory",
       "rm":"will remove all the files",
       "vim":"to open file in editor mode",
       "touch":"to create file",
       "mkdir":"to create directory"}
searchWord=input("Enter the word you want to search:") #taking input from user
print(words[searchWord]) #printing the meaning of the given word

#Checking