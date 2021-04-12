import math
#function takes a strings and split them into 2 halves

def Split_String(string):
    if(len(string)%2 == 0):
       front = string[0:int(len(string)/2)]
       back = string[int(len(string)/2):]
    else:
        front = string[0: math.ceil(len(string)/2)]
        back = string[int(len(string)/2)+1:]
    
    return [front,back]

#function takes 2 lists each list consist of 2 elements and concatenate between them
def Concatenate(list1,list2):
    a_front,a_back=list1[0],list1[1]
    b_front,b_back=list2[0],list2[1]

    return (a_front+b_front)+\
           (a_back+b_back)
           


string_1 = input("Enter case1: ")
string_2 = input("Enter case2: ")

print(Concatenate(\
      Split_String(string_1),\
      Split_String(string_2)\
       ))


  
