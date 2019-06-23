i=0
sum=0
while i<11:
	a=int(raw_input("enter your no."))
	sum=sum+a
	i=i+1
average=sum/11
print sum
print average
if average%5==0:
	print "5 se multiple h"
else:
	print "5 se multiple nhi h"