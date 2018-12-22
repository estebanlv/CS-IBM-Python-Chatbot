from openpyxl import load_workbook #This loads a library that allows me to read/write excel files
wb = load_workbook(filename = 'wordsdatabase.xlsx') #Tell the program what file i'm using
sheet = wb['main'] #Tells the program which sheet in the document i'm using
secsheet = wb['secondary']
total = wb['total']
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
            character_list.remove("$")
        elif "*" in character_list:
            character_list.remove("*")
        elif ";" in character_list:
            character_list.remove(";")
    print (character_list)
    text_file.close() #closes the file
    return character_list; #returns the list of character for the next section

def joinandsplitspace(character_list):
    joined_text = ''.join(character_list) #joins the list to create a string
    print(joined_text)
    list_of_words = joined_text.split()#Splits the string at every space
    lword_list = len(list_of_words) #Counts the words within the list
    for x in range(lword_list): #for every word in this list...
        print(list_of_words[x]) #prints all the words in the sentence
    return list_of_words;

def dostats(ystr):
    #number of apparitions statistics
    cell = letters[1] + ystr #creates the cell e.g. [B2]
    apps_number = int(sheet[cell].value) #saves the number in a integer variable
    apps_number =  apps_number + 1 #adds 1 to the variable
    apps_num_str = str(apps_number) #stores it as a string
    sheet[cell].value = apps_num_str #stores the updated number in the same cell it came from e.g. [B2]
    wb.save("wordsdatabase.xlsx")

def wordcheck(words_list):
    word_list_length = len(words_list) #checks the number of words in the list
    print(word_list_length)
    for x in range(word_list_length): #for evry word in the list do
        print(words_list[x])
        for y in range(2,10001): #repeat 10000 times. so every word is checked
            ystr = str(y)
            cell = letters[0] + ystr #creates the cell for the new word
            word_from_database = sheet[cell].value
            #print(word_from_database)
            if words_list[x] == word_from_database: #checks to see if the word is the same that the one in the database
                print("same")
                dostats(ystr) #if it is, then do the statistics part


print("This program will read anything on a text file and save the words into a database")
char_list = removepunctuation() #saves the list from the other def in another list
word_list = joinandsplitspace(char_list) #saves the word list from the procedure into another global variable
wordcheck(word_list) #calls the wordcheck function to run the words through a database


#text_file = open("texttoread.txt", "r") #opens the text file to read it
#lines = text_file.readlines() #reads every line in the file and stores it in a list
#for x in lines: #for every line in the list...
    #print (x) #prints all the lines
#text_file.close() #closes the file
