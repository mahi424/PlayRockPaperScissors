import random
msg="This is a simple simulation of rock paper scissors game\nYou will play against the software\nYou will be given 5 chances\nif you or software achieves winning lead game can stop before five chances"
print(msg)

input_map={
	'r': 1,
	'R': 1,
	'1': 1,

	'p':2,
	'P':2,
	'2':2,

	'S':3,
	's':3,
	'3':3,
}

def rps():
	inp=input("Please enter your choice \n(enter r/R/1 for rock or p/P/2 for paper or s/S/3 for scissors)\n")
	while inp not in ['r','R','1','p','P','2','s','S','3']:
		print("Invalid choice")
		inp=input("Please enter your choice \n(enter r/R/1 for rock or p/P/2 for paper or s/S/3 for scissors)\n")
	# print(inp,input_map[inp])
	rand=random.randint(1, 3)
	inp=int(input_map[inp])
	while int(inp)==int(rand):
		rand=random.randint(1, 3)
	
	rand=int(rand)
	print(inp,rand)
	if inp==1:
		print("You chose rock")
	elif inp==2:
		print("You chose paper")
	elif inp==3:
		print("You chose scissors")

	if rand==1:
		print("Computer chose rock")
	elif rand==2:
		print("Computer chose paper")
	elif rand==3:
		print("Computer chose scissors")
		
	if inp==3:
		if rand==1:
			return 1,0
		elif rand==2:
			return 0,1
		else:
			return 0,0
	elif rand==3:
		if inp==1:
			return 0,1
		elif inp==2:
			return 1,0
		else:
			return 0,0
	else:
		if rand>inp:
			return 1,0
		return 0,1

print("#####################################################")
score1,score2=0,0


while score1<3 and score2<3:
	a,b=0,0
	a,b=rps()
	print("you get"+str(b))
	print("com get"+str(a))
	score1+=a
	score2+=b
	print(score1,score2)
# for x in range(1,5):
# 	score1,score2=rps()
if score1>score2:
	print("Computer Win")
elif score1<score2:
	print("You win")