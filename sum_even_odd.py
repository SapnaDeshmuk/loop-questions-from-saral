list=[5,10,15,9,6,12]
i=0
count=0
counter=0
while i<len(list):
	if list[i]%2==0:
		print "even number hai",list[i]
		count=count+1
	else:
		print"odd number hai",list[i]
		counter=counter+1
	i=i+1