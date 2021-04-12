#function takes a string and a character and print the location of that character in the string

def Find_Char(string,char):  
      return[i for i, x in enumerate(string) if x == char]


#print(list(enumerate('Google')))
print(Find_Char('Google','o')) 