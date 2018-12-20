x = 0 #variable for a loop
i = 0 #variable for a loop
text = input("Enter a message: ") #String input
newtext = list(text) #creates a list with all the characters in the string
lmessage = len(newtext) #counts the characters in the message
print(newtext)
print(lmessage)
for i in range(lmessage): #loop to go through all the characters in the list
    #This code deletes all the punctuation characters in the list
    if "," in newtext:
        newtext.remove(",")
    elif "." in newtext:
        newtext.remove(".")
    elif ":" in newtext:
        newtext.remove(":")
    elif "!" in newtext:
        newtext.remove("!")
    elif "?" in newtext:
        newtext.remove("?")
    elif "(" in newtext:
        newtext.remove("(")
    elif ")" in newtext:
        newtext.remove(")")
    elif "/" in newtext:
        newtext.remove("/")
    elif "'" in newtext:
        newtext.remove("'")
    elif "[" in newtext:
        newtext.remove("[")
    elif "]" in newtext:
        newtext.remove("]")
    elif "=" in newtext:
        newtext.remove("=")
    elif "+" in newtext:
        newtext.remove("+")
    elif "£" in newtext:
        newtext.remove("£")
    elif "$" in newtext:
        newtext.remove("$")
    elif "*" in newtext:
        newtext.remove("*")
    elif ";" in newtext:
        newtext.remove(";")
print(newtext)
solvedtext = ''.join(newtext) #joins the list to create a string
print(solvedtext)
word = solvedtext.split()#Splits the string at every space
lword = len(word) #Counts the words within the list
for x in range(lword):
    print(word[x]) #prints all the words in the sentence
