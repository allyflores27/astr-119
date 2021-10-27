import numpy as np

def main():
	i=0      #declaring an int w/ a number
	n=10     #same as above but for below
	x=119.0  #floating point num declared with "."

	#delaring an array  with 10 zeros as floats
	y= np.zeros(n,dtype=float)

	#function says that
	#for i in range [0,n-1], set index i in y as 2i+1
	for i in range(n):
		y[i]=2.0 * float(i) +1     

	#print each element in y[i]
	for y_element in y:
		print(y_element)

#main function
if __name__ == "__main__":
	main()