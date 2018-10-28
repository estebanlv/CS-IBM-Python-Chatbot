from openpyxl import load_workbook #This loads a library that allows me to read/write excel files
import trainingbot

wb = load_workbook(filename = 'database.xlsx') #Tell the program what file i'm using
sheet = wb['Main'] #Tells the program which sheet in the document i'm using

#answer = sheet["B1"].value
#print(sheet['A1'].value)
#print(answer)

counter = 0

while(counter < 1):
    print("Welcome to my chatbot program")
    print("Please choose an option below:")
    print("PRESS 1 TO: Train the Chatbot")
    print("PRESS 2 TO: See all the questions")
    print("PRESS 3 TO: Exit")
    choice = int(input("Enter an option"))
    if choice == 1:
        print("You chose Option 1")
        print("")
        trainingbot.training_bot("Esteban")
    elif choice == 2:
        print("You chose Option 2")
        print("")
    elif choice == 3:
        counter = counter + 2
    else:
        print("Invalid choice.")
        print("")
