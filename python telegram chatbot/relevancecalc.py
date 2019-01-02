import time
from openpyxl import load_workbook #This loads a library that allows me to read/write excel files

start = time.time()

wb = load_workbook(filename = 'wordsdatabase.xlsx') #Tell the program what file i'm using
sheet = wb['main'] #Tells the program which sheet in the document i'm using
secsheet = wb['secondary']
total = wb['total']
letters = ["A","B","C","D","E","F","G","H","I","K","J","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#These variable above is for cell values

def mainalgorithm(no_of_apps, ystr):
    percentage_cell = letters[2] + ystr
    topics_cell = letters[4] + ystr
    apps_percentage = float(sheet[percentage_cell].value)
    no_of_topics = int(sheet[topics_cell].value)
    relevance = 1000 * ((1 - (no_of_topics/10)) ** apps_percentage)
    relevance = relevance - (no_of_apps * 0.5)
    relevance_cell = letters[3] + ystr
    relevance_str = str(relevance)
    sheet[relevance_cell].value = relevance_str

def primaryrelevance():
    nothing = 0
    for y in range(2,10001):
        ystr = str(y) #transforms the value into a string in order to create the cell
        cell = letters[1] + ystr #creates the cell for the new word
        no_of_apps = int(sheet[cell].value) #saves the value from the cell inside a local variable
        if no_of_apps == 0:
            nothing = 1
        else:
            mainalgorithm(no_of_apps, ystr)

print('Welcome to thee relevance calculator')
primaryrelevance()
wb.save("wordsdatabase.xlsx")

end = time.time()
print(end - start) #time taken for the program to run
