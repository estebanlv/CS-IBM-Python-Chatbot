from openpyxl import load_workbook #This loads a library that allows me to read/write excel files
wb = load_workbook(filename = 'wordsdatabase.xlsx') #Tell the program what file i'm using
sheet = wb['main'] #Tells the program which sheet in the document i'm using
letters = ["A","B","C","D","E","F","G","H","I","K","J","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#These variable above is for cell values


print("This program will read anything on a text file and save the words into a database")

text_file = open("texttoread.txt", "r") #opens the text file to read it
lines = text_file.readlines() #reads every line in the file and stores it in a list
for x in lines: #for every line in the list...
    print (x) #prints all the lines
text_file.close() #closes the file
