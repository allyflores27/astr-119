#string

s = " I am a string."
print(type(s))     # prints out data type, str


#boolean
yes = True
print(type(yes))      

no = False
print(type(no))

#List -- ordered and changeable
alpha_list = ["a","b","c"]    #list initilaliazed
print(type(alpha_list))       #will say tuple
print(type(alpha_list[0]))    #will say string
alpha_list.append("d")        #will add "d" to the list end
print(alpha_list)             #prints list


#Tuple -- ordered and unchangeable
alpha_tuple=("a","b","c") #tuple initialization
print(type(alpha_tuple))  #will say tuple

try:                    #will try following line
	alpha_tuple[2]="d"  #won't work on tuple and raise a TypeError
except TypeError:       #when we get a TypeError
	print("We can't add elements to tuples!")  # prints this message
print(alpha_tuple)       #prints tuple