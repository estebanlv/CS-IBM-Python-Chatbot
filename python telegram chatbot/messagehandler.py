import time
from openpyxl import load_workbook #This loads a library that allows me to read/write excel files

wb = load_workbook(filename = 'wordsdatabase.xlsx') #Tell the program what file i'm using
sheet = wb['main'] #Tells the program which sheet in the document i'm using
secsheet = wb['secondary']
total = wb['total']
letters = ["A","B","C","D","E","F","G","H","I","K","J","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#These variable above is for cell values

def removepunctuation():
    output = open('dissectedmessage.txt', 'a') #opens file to append it.
    with open('message.txt', buffering = 20000000) as f: #opens the text file
        for line in f: #for every line in the file...
        #this code below is used to remove the punctuation from the text
            saveline = line.replace('.',' ')
            saveline = saveline.replace(',','')
            saveline = saveline.replace(':','')
            saveline = saveline.replace(';','')
            saveline = saveline.replace('!','')
            saveline = saveline.replace('?','')
            saveline = saveline.replace('"','')
            saveline = saveline.replace('#','')
            saveline = saveline.replace('-','')
            saveline = saveline.replace('_','')
            saveline = saveline.replace('=','')
            saveline = saveline.replace('+','')
            saveline = saveline.replace('@','')
            saveline = saveline.replace('(','')
            saveline = saveline.replace(')','')
            saveline = saveline.replace('[','')
            saveline = saveline.replace(']','')
            saveline = saveline.replace('*','')
            saveline = saveline.replace('%','')
            saveline = saveline.replace('£','')
            saveline = saveline.replace('$','')
            saveline = saveline.replace('  ',' ')
            saveline = saveline.replace('\n',' ')
            #saveline = saveline.rstrip() #removes all the newlines \n
            saveline = saveline.replace(' ','\n') #puts every word in a different line
            saveline = str.lower(saveline) #converts everything to lowercase
            output.write(saveline)
    output.close() #saves and closes the file

def joinandsplitspace(word_list):
    joined_text = ''.join(word_list) #joins the list to create a string
    #print(joined_text)
    list_of_words = joined_text.split()#Splits the string at every space
    lword_list = len(list_of_words) #Counts the words within the list
    #for x in range(lword_list): #for every word in this list...
        #print(list_of_words[x]) #prints all the words in the sentence
    return list_of_words;

def readfile():
    topic = input("Enter the main topic of this text:")
    text_file = open("dissectedmessage.txt", "r") #opens the text file to read it
    word_list = text_file.read()
    print("read")
    return word_list;

def writemessagetofile(messagetext):
    message_file = open("message.txt", "w")
    message_file.write(messagetext)
    message_file.close()

def start(messagetext):
    print("Lets start the search")
    writemessagetofile(messagetext)
    removepunctuation()
    word_list = readfile()
    list_of_words = joinandsplitspace(word_list)
    print(list_of_words)
