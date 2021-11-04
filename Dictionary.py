import json
from difflib import get_close_matches

data = json.load(open("Desktop/PYTHON/08 Application 1 Building an Interactive Dictionary/076 data.json"))

def wordbook(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        recheck = input("Did you mean %s instead? If yes enter Y but if No enter N? " % get_close_matches(word,data.keys())[0])
        if recheck == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif recheck == "N":
            return "The word does not exist, check your spelling."
        else:
            return "Check your response again."
    else:
        return "The word does not exist, check your spelling."
ctrl = input("Enter a word: ")

output = wordbook(ctrl)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)

