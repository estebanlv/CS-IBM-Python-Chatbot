print("This program will read anything on a text file and save the words into a database")


text_file = open("texttoread.txt", "r") #opens the text file to read it
lines = text_file.readlines() #reads every line in the file and stores it in a list
for x in lines: #for every line in the list...
    print (x) #prints all the lines
text_file.close() #closes the file
