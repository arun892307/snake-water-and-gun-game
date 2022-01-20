# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 07:15:14 2021

@author: Ajay Kumar
"""

import random
print("welcome to snake ,water and Gun game code by arun Kumar")
print("Dear player remember you play with Computer:\n So best of lack:")
print("You have 10 chance:")
list= ["Snake","Water","Gun"]
ch=10
your_score=0
computer_score=0


while(ch!=0):
    
    print("Select a option:\n1.Sanke\n2.water\n3.Gun")
    rand=random.choice(list)
    num= int(input("Enter your choice:"))
    print("You choose:",num)
    print("Compuer choose:",rand)
    if((num==1 and rand=="snake") or (num==2 and rand=="Water") or (num==3 and rand=="Gun")):
        print("Sorry computer choose same option ,No points are assign anyone")
        
    elif(num==1 and rand=="Water"or num==2 and rand=="Gun" or num==3 and rand=="Snake"):


        print("You won this chance:\n")
        your_score=your_score+1
        
    else:
        print("Computer Won this chance:\n")
        computer_score=computer_score + 1
    ch=ch-1
    print("now you have ",ch,"chance") 
print("\n")
print("your score:",your_score) 
print("Computer score:",computer_score)
if(your_score>computer_score):
    print("Congratulations you won ths game")
elif(your_score==computer_score):
    print("Computer won this game")
else:
    print("Soory you failed \n Try again with your best ")    
print("\nthanks for playing and wait for result:")


