
# Jump Statement Assignment


# Founding Letter

def searchLetter(word, letter) :
    position = -1
    for i in range(len(word)) :
        if word[i] == letter :
            position = i
            break
    return position

userInput1 = input("Enter a Word : ")
wordLower = userInput1.lower()
userInput2 = input("Enter a letter : ")
letterLower = userInput2.lower()

print(searchLetter(wordLower, letterLower))




# Process a List

def processArray(array, value):
    for n in array:
        if n == value:
            return False
        print(n)

userValue = int(input("Enter a Number : "))
print(processArray([5, 10, 15, 20, 25, 30, 35, 0, 40, 45, 50], userValue))



# Function that Counts Non-Space and Skip Vowels

def checkSkip(sentence) :
    count_non_space = 0
    vowels = "aeiou"
    for i in sentence :
        if i in vowels :
                continue
        if i != " " :
            count_non_space += 1
    return print(count_non_space)

userSentence = input("Enter a Sentence : ")
sentenceLower = userSentence.lower()
checkSkip(sentenceLower)

