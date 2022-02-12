import random
import time
import pyttsx3
s=pyttsx3.init()
print("~"*50)
print("               WELCOME TO THE MATHS TEST")
s.say("WELCOME TO THE MATHS TEST")
s.runAndWait()
print("~"*50)

print("RULES:-\n\t1.Don't use the calculator.\n\t2.More than half questions should be correct for being pass!!!!")
s.say("Rules are Don't use the calculator and More than half questions should be correct for being pass")
s.runAndWait()
print("~"*50)

name=input("Enter your name:-")
n=int(input("How many questions do you want:-"))
print("~"*50)

print("Get ready the game is starting")
s.say("Get ready the game is starting")
s.runAndWait()

correct=0
print("-"*50)

def add():
    global correct
    num1=random.randint(1,100)
    num2=random.randint(1,100)
    s = num1 + num2
    inp = int(input("Q."+str(i+1)+":- "+str(num1) + "+"+str(num2) + "= "))
    if s == inp:
        print("Correct ans !!! Nice")
        correct+=1
    else:
        print("Oops!!! you got this one wrong")

def multiply():
    global correct
    num1=random.randint(1,15)
    num2=random.randint(1,15)
    s = num1*num2
    inp = int(input("Q."+str(i+1)+":- "+str(num1) + "x"+str(num2) + "= "))
    if s == inp:
        print("Correct ans !!! Nice")
        correct += 1
    else:
        print("Oops!!! you got this one wrong")

def divide():
    global correct
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    s = round(num1/num2,2)
    inp = eval(input("Q."+str(i+1)+":- "+str(num1) + " / "+str(num2) + "(upto 2 decimal if required) = "))
    if s == inp:
        print("Correct ans !!! Nice")
        correct += 1
    else:
        print("Oops!!! you got this one wrong")

def subtract():
    global correct
    num1=random.randint(1,100)
    num2=random.randint(1,100)
    s = num1-num2
    inp = int(input("Q."+str(i+1)+":- "+str(num1) + "-"+str(num2) + "= "))
    if s == inp:
        print("Correct ans !!! Nice")
        correct += 1
    else:
        print("Oops!!! you got this one wrong")

for i in range(n):
    d=random.randint(0,3)
    # c={1:'add',2:'multiply',3:'divide',4:'subtract'}
    if d==1:
        add()
    elif d==2:
        multiply()
    elif d==3:
        divide()
    else:
        subtract()

half=n/2
if correct>half:
    print("You are passed !!!! Congratulations",name)
    s.say("You are passed !!!! Congratulations"+name)
    s.runAndWait()
    print("CORRECT ANSWER:-", correct)
    print("WRONG ANSWER:-", n - correct)
else:
    print("Oh no !!!! You failed the test ....You need more practise ",name)
    s.say("Oh no !!!! You failed the test ....You need more practise "+name)
    s.runAndWait()
    print("CORRECT ANSWER:-", correct)
    print("WRONG ANSWER:-", n - correct)