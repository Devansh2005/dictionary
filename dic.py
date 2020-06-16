import json
from difflib import get_close_matches

file=json.load(open("original.json","r"))
word=input("Enter the word : \n")
word= word.lower()
def dic_word(words):
    if word in file:
        return file[word]

    elif word.title() in file:
        return file[word.title()]

    elif( word.capitalize() in file):
        return file[word.capitalize()]
        
    elif word.upper() in file:
        return file[word.upper()]

    elif len(get_close_matches(word,file.keys())) > 0:
        print("Did you mean %s instead" %get_close_matches(word,file.keys())[0])
        decide=input("Press y for Yes and n for NO \n")
        if decide =="y" or "Y":
            return file[get_close_matches(word,file.keys())[0]]
        elif decide=="n" or "N":
            print("Word does not exist")
        else:
            print("Abey Y ya N type krna tha bc")

    else:
        print("We dont have this word in the dictionary")

output= dic_word(word)
if type(output)==list:
    for item in output:
 
        print(item)
else:

    print(output)