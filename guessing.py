i = 1
while i <= 5:
	user = int(raw_input("enter your number"))
	if user == 5:
		print "right guess"
		break
	else:
		print "wrong guess"
		i = i + 1