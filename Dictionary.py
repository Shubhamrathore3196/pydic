import json
from difflib import get_close_matches
data = json.load(open('data.json'))

word = input('enter a word')
def translator(word):
    if word in data:
       return data [word]
    elif word.lower() in data:
        return data [word.lower()]
    elif word.upper() in data:
        return  data[word.upper()]
    elif (len(get_close_matches(word,data)))>0:
        print("did you mean %s instead" % get_close_matches(word, data.keys())[0])
        warning = input("y to continue n to break out")
        if warning == 'y':
            print((get_close_matches(word,data)))
        else:
            print('Sorry no matches found try again')
    else:
        print('type other word please')

output= translator(word)
print(output)

