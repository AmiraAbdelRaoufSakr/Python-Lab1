from collections import Counter

words = [];  

file = open("data.txt", "r")  

for line in file:   
    string = line.lower().replace('?','').replace(',','').replace('.','').split(" ");  
    for s in string:  
        words.append(s);  

Counter = Counter(words)
most_occur = Counter.most_common(20)

f = open("popular_word.txt",'w')
f.write( str(most_occur))
f.close()

file.close();  
