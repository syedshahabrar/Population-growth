def listofwords(text):
    listofwords = text.split()
    for i in range(len(listofwords)):
        string = listofwords[i]
        alphanumeric = ""
        for char in string:
            if char.isalnum(): #used to remove all other characters as ':)' acted as a word
                alphanumeric += char
        listofwords[i] = alphanumeric
    listofwords.remove('') #used to remove space item from the list
    return listofwords
     
def wordcount(listofwords):
    return len(listofwords)

def frequency(listofwords):
    frequency = {}
    for items in listofwords:
        frequency[items] = listofwords.count(items) #forms dictionary with all words with their frequencies
    return frequency

def specialcharacters(text):
    special = []
    for i in range(len(text)):
        if text[i].isalpha() or text[i].isdigit() or text[i]==" ":
            continue #ignores alphanumeric and space characters
        else: 
            special.append(text[i]) #lists the specials
    return special

def mostfrequentletter(text):
    frequency = {}
    for i in text:
        if i != ' ': #ignores space as it would have been considered
            if i in frequency:
                frequency[i] += 1 #iterates the count for that character
            else: frequency[i] = 1 #adds new entry
    mostfrequent = max(frequency, key = frequency.get) #gets key of the max value
    print('The letter that is repeated the most is the letter:', mostfrequent , 'repeated', text.count(mostfrequent), 'times')

def textAnalyser(text):
    words = listofwords(text)
    print('Your text has:', wordcount(words), 'words')
    for i in frequency(words):
        print(i, ': repeated', frequency(words)[i], 'times') #lists all words with their frequencies
    print('Your text has', len(specialcharacters(text)), 'special characters:', ' '.join(specialcharacters(text))) #used join function to avoid the brackets from just printing  a list
    mostfrequentletter(text) #I only call function as itself outputs the two values in the string

textAnalyser('Hello class, I hope that you are enjoying this class! :)') #tester