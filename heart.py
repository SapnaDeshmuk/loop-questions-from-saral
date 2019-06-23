row=0
while row<=6:
	column=0
	while column<=7:
	if (row==0 and column%3!=0) or (row==1 and column%3==0) or (row-colunm==2) or (row + column==8):
		print ("*",end="")
		column=column+1
	else:
		print("",end="")
	row=row+1
	print()
