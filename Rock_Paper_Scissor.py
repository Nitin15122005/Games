import random
import time
print("*"*20)

option=['rock','paper','scissor']
print("    ROCK PAPER SCISSOR    ")
player_points=0
comp_points=0
pname=input("Enter your name:-")
while True:
	popt=input("Choose your option(rock/paper/scissor) :-")
	popt=popt.lower()
	print(pname,"Selected",popt.upper())
	i=random.randint(0,2)
	copt=option[i]
	print("Computer selected",copt.upper())

	if popt==copt:
		print("ROUND DRAW")
	elif popt=="scissor" and copt=="paper":
		print(pname,"Wins the round.")
		player_points+=1
	elif copt=="scissor" and popt=="paper":
		print("Computer Wins the round.")
		comp_points+=1
	elif popt=="rock" and copt=="paper":
		print("Computer Wins the round.")
		comp_points+=1
	elif copt=="rock" and popt=="paper":
		print(pname,"Wins the round.")
		player_points+=1
	elif popt=="scissor" and copt=="rock":
		print("Computer Wins the round.")
		comp_points+=1
	elif copt=="scissor" and popt=="rock":
		print(pname,"Wins the round.")
		player_points+=1

	print("*"*20)
	print("Score of",pname,"is",player_points)
	print("-"*20)
	print("Score of COMPUTER is",comp_points)
	print("-"*20)
	ans=input("Do you want to go for another round(yes/no):-")
	if ans.lower()=="no":
		break
	print("-"*20)

if player_points>comp_points:
	print(pname,"WINS!!!!")
elif player_points==comp_points:
	print("GAME IS A DRAW!!!!")
else:
	print("COMPUTER WINS!!!")