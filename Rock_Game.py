import random
l=["Rock", "Scissor", "Paper"]
while True:
    ucount=0
    ccount=0
    uc=int(input(
        ''' 
        Game start.....
        1. Yes
        2. No | Exit
        '''
    ))
    if uc==1:
        for a in range(1,6):
            print(" ")
            userinput=int(input(''' Enter your choice 
            1. Rock
            2. Scissor
            3. Paper
            '''))
            if userinput==1:
                uchoice="Rock"
            elif userinput==2:
                uchoice="Scissor"
            elif userinput==3:
                uchoice= "Paper"
            Cchoice=random.choice(l)
            if Cchoice == uchoice:
                print(" ")
                print("Computer value is", Cchoice)
                print("Your Choice is ",uchoice)
                print(" ")
                print("         Oops Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif ( uchoice=="Rock" and Cchoice=="Scissor") or ( uchoice=="Paper" and Cchoice=="Rock") or ( uchoice=="Scissor" and Cchoice=="Paper" ):
                print(" ")
                print("Computer value is", Cchoice)
                print("Your Choice is ",uchoice)
                print(" ")
                print("         Wow You Win ")
                ucount=ucount+1
            else:
                print(" ")
                print("Computer value is", Cchoice)
                print("Your Choice is ",uchoice)
                print(" ")
                print("         Sad Computer Win")
                ccount=ccount+1
        if ucount==ccount:
            print(" ") 
            print("     FINAL GAME DRAW......")
            print("     Your Score ", ucount)
            print("     Computer Score ",ccount)
        elif ucount>ccount:
            print(" ")
            print("     Congratulations! YOU WIN THE GAME......")
            print("     Your Score ", ucount)
            print("     Computer Score ",ccount)
        else:
            print(" ")
            print("     Sorry!COMPUTER WIN THE GAME......")
            print("     Your Score ", ucount)
            print("     Computer Score ",ccount)
    else:
        
        break
