from openpyxl import load_workbook #This loads a library that allows me to read/write excel files

wb = load_workbook(filename = 'database.xlsx') #Tell the program what file i'm using
sheet = wb['Main'] #Tells the program which sheet in the document i'm using

row_num = 4 #Needs to be updated depending on the amount of questions
letters = ["A","B","C","D","E","F","G","H","I","K","J","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#letters for the cell values

def training_bot(name): #Start of the function
    count = 0
    loop = 0
    cell = 1
    x = 1 #Used to represent the row number in the for loop
    print("Lets start training the Chatbot")
    print("His name is " + name)
    for i in range(0,row_num): #goes through all the rows in the Column A
        xstr = str(x) #converts an int to str
        question = letters[0] + xstr #Creates a cell position (Here is always A + num)
        x = x + 1
        answer = str(input(sheet[question].value + ": ")) #user enters an answer
        free_cell = letters[25] + xstr #Gets the value that knows which cell doesnt have anything on it
        free_cell_int = int(sheet[free_cell].value) #converts the number to an integer
        #print(free_cell_int)
        question = letters[free_cell_int] + xstr #new cell is selected in the database
        sheet[question].value = answer #value is stored in the database
        temp = int(sheet[free_cell].value) + 1 #Updates the number of the next free cell
        strtemp = str(temp) #converts it to a string
        sheet[free_cell].value = strtemp #stores it the same place it came from
        print(answer)
        wb.save('database.xlsx') #document is saved
    return;
