from openpyxl import load_workbook #This loads a library that allows me to read/write excel files
wb = load_workbook(filename = 'wordsdatabase.xlsx') #Tell the program what file i'm using
sheet = wb['main'] #Tells the program which sheet in the document i'm using
letters = ["A","B","C","D","E","F","G","H","I","K","J","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#These variable above is for cell values

def removepunctuation():
    text_file = open("texttoread.txt", "r") #opens the text file to read it
    lines = text_file.read() #reads every line in the file and stores it in a list
    lines = lines.lower() #converts the whole string into lowercase
    character_list = list(lines) #separates the string into characters
    length_character_list = len(character_list) #counts the amount of characters in a list
    for i in range(length_character_list): #loop to go through all the characters in the list
        #This code deletes all the punctuation characters in the list
        if "," in character_list:
            character_list.remove(",")
        elif "." in character_list:
            character_list.remove(".")
        elif ":" in character_list:
            character_list.remove(":")
        elif "!" in character_list:
            character_list.remove("!")
        elif "?" in character_list:
            character_list.remove("?")
        elif "(" in character_list:
            character_list.remove("(")
        elif ")" in character_list:
            character_list.remove(")")
        elif "/" in character_list:
            character_list.remove("/")
        elif "'" in character_list:
            character_list.remove("'")
        elif "[" in character_list:
            character_list.remove("[")
        elif "]" in character_list:
            character_list.remove("]")
        elif "=" in character_list:
            character_list.remove("=")
        elif "+" in character_list:
            character_list.remove("+")
        elif "£" in character_list:
            character_list.remove("£")
        elif "$" in character_list:
            character_listremove("$")
        elif "*" in character_list:
            character_list.remove("*")
        elif ";" in character_list:
            character_list.remove(";")
    print (character_list)
    text_file.close() #closes the file
    return character_list; #retrns the list of character for the next section

def joinandsplitspace(character_list):
    joined_text = ''.join(character_list) #joins the list to create a string
    print(joined_text)
    list_of_words = joined_text.split()#Splits the string at every space
    lword_list = len(list_of_words) #Counts the words within the list
    for x in range(lword_list): #for every word in this list...
        print(list_of_words[x]) #prints all the words in the sentence

print("This program will read anything on a text file and save the words into a database")
char_list = removepunctuation() #saves the list from the other def in another list
joinandsplitspace(char_list)



#text_file = open("texttoread.txt", "r") #opens the text file to read it
#lines = text_file.readlines() #reads every line in the file and stores it in a list
#for x in lines: #for every line in the list...
    #print (x) #prints all the lines
#text_file.close() #closes the file
