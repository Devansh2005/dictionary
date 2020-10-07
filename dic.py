import json
from difflib import get_close_matches

file=json.load(open("original.json","r"))  #read the json file
word=input("Enter the word : \n")      #word to be searched
word= word.lower()                
def dic_word(words):
    if word in file:
        return file[word]                   #key se value milli 

    elif word.title() in file:
        return file[word.title()]            

    elif( word.capitalize() in file):
        return file[word.capitalize()]
        
    elif word.upper() in file:
        return file[word.upper()]

    elif len(get_close_matches(word,file.keys())) > 0:                                # close match word
        print("Did you mean %s instead" %get_close_matches(word,file.keys())[0])      #cutoff argument is not present
        decide=input("Press Y for Yes and N for NO \n")
        if decide =="y" or "Y":
            return file[get_close_matches(word,file.keys())[0]]
        elif decide=="n" or "N":
            print("Word does not exist")
        else:
            print("Either Press Y or N")

    else:
        print("We dont have this word in the dictionary")

output= dic_word(word)
if type(output)==list:          
    for item in output:                #if the word has two meaning return a string not a list
 
        print(item)
else:                                       # word has only one meaning

    print(output)