import json

#Load the data from dictionary.json
data = json.load(open("dictionary.json"))

#function for retreiving word meaning
def get_meaning(word):
    return data[word]

#get user input
users_word = input("Enter a word: ")

#get word meaning using function and print it
print(get_meaning(users_word))