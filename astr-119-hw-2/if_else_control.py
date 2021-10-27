
#define a function

def flow_control(k):
	#define a string based on the valie of k
	if(k==0):
		s = "variable k = %d equals 0" % k
	elif(k==1):
		s = "variable k = %d equals 1" % k
	else:
		s= "variable k = %d does not equal 0 or 1" % k
	#print variable
	print(s)


#define the main function
def main():

	i=0
	flow_control(i)
	i=1
	flow_control(i)
	i=2
	flow_control(i)


#run the program

if __name__ == "__main__":
	main()