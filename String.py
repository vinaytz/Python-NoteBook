s = "vinaytz"
s.capitalize()  #Vinaytz
s.upper()       #VINAYTZ
s.lower()       #vinaytz


mystr = "Hello" 
mystr[0:2] #He

mystr = "Hello" 
mystr[2:] #llo

myName = "Cosmos"
myName[::-1]   #somsoC


s = "hey"
"he" in s #Ture

S = "my_name_is_Vinay"
S.split("_") #['my', 'name', 'is', 'Vinay']


data = "   email   is invalid     "
data.strip()  #'email   is invalid'


l = ["a", "b", "c", "d"]
"".join(l) #abcd
"2".join(l) #a2b2c2d


varialbe = "Hello SR, How are you!"
varialbe.find("SR") #6
varialbe.find("SR5") #-1

s = "subsub"
s.rfind("sub")

name = "Cosmos"
name.count("o") #2
name.count("2") #0


myvar = "1 is not 1, it's 1.1"
myvar.replace("1", "2")      #2 is not 2, it's 2.2
myvar.replace("1", "2", 1)   #2 is not 1, it's 1.1  


abc = "Hello there! acha Bye"
abc.startswith("Hello") #True
abc.startswith("Vinay") #False


abc.endswith("Bye") #True
abc.endswith("Ok") #False


text = "don't take her very seriously"
text.title()  #Don'T Take Her Very Seriously


#Happy Leaning :)