import numpy as np


#integer
i=10
print(type(i))            #prints out data types

a_i=np.zeros(i,dtype=int) #declare array of ints
print(type(a_i))          #returns nd array
print(type(a_i[0]))       #returns int64

#floats

x=119.0           #float
print(type(x))    #prints data type of x

y = 1.19e2        #float number in scientific notation
print(type(y))    #prints data type of x

z=np.zeros(i,dtype=float)  #declare array of floats
print(type(z))             #returns nd array
print(type(z[0]))          #returns int64