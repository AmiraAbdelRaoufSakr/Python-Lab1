#function takes a list of numbers and reduces all similar elements to a single element
def Unique_List(list):
  uniquelist=set(list)
  return uniquelist 

print(Unique_List([1,2,2,3,2]))

