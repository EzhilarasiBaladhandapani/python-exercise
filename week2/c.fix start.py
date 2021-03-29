string = "babble yields babble"

char =string[0]

string = string.replace(char,'*')
string = char + string[1:]
print(string)