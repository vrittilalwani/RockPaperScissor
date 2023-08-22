import random
dic={
    'Rock':'🪨 -> Rock',
    'Paper':'📜 -> Paper',
    'Scissors':'✂️-> Scissors'
    }
l=['Rock','Paper','Scissors']
won=0
Lose=0
Draw=0
while True:
    print('Choose:','🪨 -> Rock','📜 -> Paper','✂️-> Scissors')
    user_choose=input()
    print
    if user_choose!='Rock' and user_choose!='Paper' and user_choose!='Scissors':
        print("Invalid input try another")
        continue
    elif user_choose=='Rock' or user_choose=='Paper' or user_choose=='Scissors':
        print('user_choose->',dic[user_choose])
        computer_choose=random.choice(l)
        print('computer_choose->',dic[computer_choose]) 
        if user_choose== computer_choose:
            Draw+=1
            print(f"Both players selected {user_choose}. It's a tie!")
            print('win=',won,'|','Lose=',Lose,'|','Draw=',Draw)
        elif user_choose == "Rock":
            if computer_choose == "Scissors":
                print('You win!😀😁')
                won+=1
                print('win=',won,'|','Lose=',Lose,'|','Draw=',Draw)
            else:
                print("You lose😟☹️")
                Lose+=1
                print('win=',won,'|','Lose=',Lose,'|','Draw=',Draw)
        elif user_choose == "Paper":
            if computer_choose == "Rock":
                print('You win!😀😁')
                won+=1
                print('win=',won,'|','Lose=',Lose,'|','Draw=',Draw)
            else:
                print("You lose😟☹️")
                Lose+=1
                print('win=',won,'|','Lose=',Lose,'|','Draw=',Draw)
        elif user_choose == "Scissors":
            if computer_choose == "Paper":
                print('You win!😀😁')
                won+=1
                print('win=',won,'|','Lose=',Lose,'|','Draw=',Draw)
            else:
                print("You lose😟☹️")
                Lose+=1
                print('win=',won,'|','Lose=',Lose,'|','Draw=',Draw)  
        print('----------------------------------------------------------')   
    check=input('Do you want to continue game->Yes/No:- ')
    if check!="Yes":
        break
        
print('🔴🟡🟣🔵🎉Final Result Of The Player🎉🔴🟡🟣🔵')
if won==0:
    print('win:','0️⃣')  
if won>0:
    print('win:',won*'🟩'+'('+str(won)+')')
if Lose==0:
    print('Lose:','0️⃣')
if Lose>0:
    print('Lose:',Lose*'🟥'+'('+str(Lose)+')')
if Draw==0:
    print('Draw:','0️⃣')
if Draw>0:
    print('Draw:',Draw*'🟨'+'('+str(Draw)+')')
print('🔚🔚🛑Game End🛑🔚🔚')
