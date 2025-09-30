import random

print("---------------------")
print(" ROCK PAPER SCISSCORS")
print("----------------------")
print("                      ")
print("1) Rock ✊") #beats scissor 
print("2) Paper ✋ ") #beats rock 
print("3) Scissor ✌️ ") #beats paper 

wins = 0


while(wins<3):



    CPU = random.randint(1,3)
    if(CPU ==1):
        emoji_cpu = '✊'
    elif(CPU ==2):
        emoji_cpu= '✋'
    elif(CPU ==3):
        emoji_cpu= '✌️'

    playerinput = int(input("Pick a number:  "))
    if(playerinput ==1):
        emoji = '✊'
    elif(playerinput ==2):
        emoji = '✋'
    elif(playerinput ==3):
        emoji = '✌️'

    if(playerinput>3):
        print(f'Player:{emoji}') 
        print("Invalid entry")
        print(f'wins:{wins}')
    elif(playerinput<1):
        print(f'Player:{emoji}')
        print('Invalid entry')
        print(f'wins:{wins}')
    elif(playerinput == CPU):
        print(f'Player:{emoji}')
        print(f'CPU: {emoji_cpu}')
        print("Result: DRAW")
        print(f'wins:{wins}')
    elif(playerinput==1 and CPU ==2):
        print(f'Player:{emoji}')
        print(f'CPU: {emoji_cpu}')
        print("Result : CPU WINS")
        wins -= 1
        print(f'wins:{wins}')
    elif(playerinput==1 and CPU ==3):
        print(f'Player:{emoji}')
        print(f'CPU: {emoji_cpu}')
        print("Result : PLayer WINS")
        wins +=1
        print(f'wins:{wins}')
    elif(playerinput==2 and CPU ==1):
        print(f'Player:{emoji}')
        print(f'CPU: {emoji_cpu}')
        print("Result : Player WINS")
        wins +=1
        print(f'wins:{wins}')
    elif(playerinput==2 and CPU ==3):
        print(f'Player:{emoji}')
        print(f'CPU: {emoji_cpu}')
        print("Result : CPU WINS")
        wins -= 1
        print(f'wins:{wins}')
    elif(playerinput==3 and CPU ==1):
        print(f'Player:{emoji}')
        print(f'CPU: {emoji_cpu}')
        print("Result : CPU WINS")
        wins -= 1
        print(f'wins:{wins}')
    elif(playerinput==3 and CPU ==2):
        print(f'Player:{emoji}')
        print(f'CPU: {emoji_cpu}')
        print("Result : PLayer WINS")
        wins +=1
        print(f'wins:{wins}')
    

print("Thanks for PLAYING")