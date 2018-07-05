from easygui import *
import random
score1,score2=0,0
title = "RockPaperScissors"
msg="This is a simple simulation of rock paper scissors game\nYou will play against the software\nYou will be given 5 chances\nif you or software achieves winning lead, game can stop before five chances"
def rps():
	msg ="Choose Your Bet?"
	
	choices = ["Rock", "Paper", "Scissors"]
	choice = choicebox(msg, title, choices)
	d={
	"Rock":1, "Paper":2, "Scissors":3
	}
	inp=int(d[choice])
	print(inp)

	rand=random.randint(1, 3)
	# inp=int(input_map[inp])
	while int(inp)==int(rand):
		rand=random.randint(1, 3)
	
	rand=int(rand)
	print(inp,rand)
	if inp==1:
		print("You chose rock")
		s1="You chose rock"
	elif inp==2:
		print("You chose paper")
		s1="You chose paper"
	elif inp==3:
		print("You chose scissors")
		s1="You chose scissors"

	if rand==1:
		print("Computer chose rock")
		s2="Computer chose rock"
	elif rand==2:
		print("Computer chose paper")
		s2="Computer chose paper"
	elif rand==3:
		print("Computer chose scissors")
		s2="Computer chose scissors"
	if ccbox(s1+"\n"+s2, title):
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

		



if ccbox(msg, title):
	while score1<3 and score2<3:
		a,b=0,0
		a,b=rps()
		if a==1:
			m="Computer won this game"
		elif b==1:
			m="You won this game"
		# rps()
		# print("you get"+str(b))
		# print("com get"+str(a))
		msgbox(m,title)
			
		score1+=a
		score2+=b
		print(score1,score2)
	# for x in range(1,5):
	# 	score1,score2=rps()
	if score1>score2:
		print("Computer Win")
		msgbox("Computer Win",title)
	elif score1<score2:
		print("You win")
		msgbox("You win",title)