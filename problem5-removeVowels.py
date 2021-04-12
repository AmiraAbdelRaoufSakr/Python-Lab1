#function takes a string and removes the vowel characters

def Remove_Vowels(string):
    vowels=['a','e','i','o','u']
    for char in string.lower():
        if char in vowels:
            string = string.replace(char,"")
    
    print(string)

string=input("Enter your string: ")


Remove_Vowels(string)