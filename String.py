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


"aman" > "vinay" #false   
"aman" < "Aakash" #false  as  py check it by lexiographically

mytext= r"hello this is \n raw text" #hello this is \n raw text
myunicode= u"\U0001f600" #😀
a= True + 5 #6


a = "@352523"
print(a[-1])



not "" #true
not "hello" #false
"" or "something"  #OUTPUT:True  as ("" -> False)  or  ("something" -> True)  which gives (0 or 1) = 1 (True)
"someting1" or ("something2") #OUTPUT: something1  as or condition will just check the first condition (which is true)
"someting1" and ("something2") #OUTPUT: something2 as result needs both conditions to be true. so it will last fall at condition2 


S = "my_name_is_Vinay"
S.split("_") #['my', 'name', 'is', 'Vinay']


data = "   email   is invalid     "
data.strip()  #'email   is invalid'


l = ["a", "b", "c", "d"]
"".join(l) #abcd
"2".join(l) #a2b2c2d


my_string = "This is a sample string with spaces"
my_list = my_string.split() #['This', 'is', 'a', 'sample', 'string', 'with', 'spaces']


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
