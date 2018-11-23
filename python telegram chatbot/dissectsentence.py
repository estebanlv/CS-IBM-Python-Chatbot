text = 'International Business Machines Corporation es una reconocida empresa multinacional estadounidense de tecnología y consultoría'
x = 0
# Splits at space 
word = text.split(' ')
lword = len(word)
for x in range(lword):
    print(word[x])
