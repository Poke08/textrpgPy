import random
ammoCommand = False
playing = False
setting = ''
lame_unlocked = False
Stupid_unlocked = False
loyal_unlocked = False
venom_unlocked = False

flawLessAchievement = False

fullAchievement = False
Achievements = []
allAchievements = ["flawless"]

Endings = []
allEndings = ["lame","Stupid","Loyal","venom"]
max_ending = len(allEndings)

def checkContinue():
    for ending in allEndings and fullAchievement == True:
        if ending not in Endings:
            return True
    print(f"{name} you have beat the game!")
    return False

def checkAchievement():
    for achievement in allAchievements:
        if achievement not in Achievements:
            fullAchievement = False
        else:
            fullAchievement = True

name = input('Enter your name! ')
print(f'Greetings {name}!')

playing = True

while playing:
    start = input('Would you rather play the game or perish? ')
    if start == 'play':
        print('Come on then, what are we waiting for!')
        setting = input(f'Ok {name}! Wanna go to the jungle or the desert? ')
    else:
        print('Lame. You\'re dead...')
        
        if lame_unlocked == True:
            print('You have already unlocked this ending!')
        else:
            print('You have unlocked the "Lame" ending!')
            Endings.append("lame")
            print(f'You have unlocked {len(Endings)}/{max_ending} endings!')
            lame_unlocked = True

    if setting == 'jungle':
        print(f'Welcome {name}, to the almighty jungle! Your tour guide took you to a nice looking waterfall...') 
        print('He told you to sit down and wait for him to go do something...')
        response = input('Your tour guide has been gone for a while... Follow him or wait here? ')
        if response == 'follow':
            print('You follow him into the jungle...')
            print('You walked the same direction as your tour guide went...')
            Follow = input('You found some footprints leading deeper into the jungle. Follow them or go back? ')
            if Follow == 'follow':
                print('You follow the foot prints for a while and find your tour guides dead body laying up against a tree...')
                dead = input('You check his body and find a gun and a medkit. Do you take the gun or the medkit? ')

                if dead == 'gun':
                    ammo = [5]
                    print('You chose the gun, good choice...')
                    print('It will maybe be handy if whatever killed the tour guide tries to come for you...')
                    print(f'You check the magazine and it has {ammo}/8 ammunition...')
                    print('You see a river nearby...')
                    river = input('Do you check it out, or continue into the jungle? ')
                    
                    if river == 'continue':
                        print('You continue into the jungle...')
                        print('You stumble onto some angry monkeys...')
                        shootMonkey = input ('Do you shoot one, or not? ')

                        if shootMonkey == 'yes':
                            usedShotsList = ['1','2','3','4','5']
                            usedShots = (random.choice(usedShotsList))
                            
                            if usedShots == '1':
                                print('You sucessfully killed one of the monkeys and the others ran in fear...')
                                ammo -= 1
                                print(f'You have {ammo}/8 ammo left...')
                                flawLessAchievement = True
                                print('You\'ve unlocked the "Flawless" achievement!')

                            if usedShots == '2':
                                print('You sucessfully killed one of the monkeys but you used up two shots...')
                                ammo -= 2
                                print(f'You have {ammo}/8 ammo left...')

                            if usedShots == '3':
                                print('You sucessfully killed one of the monkeys but you used up three shots...')
                                ammo -= 3
                                print(f'You have {ammo}/8 ammo left...')
                            
                            if usedShots == '4':
                                print('You sucessfully killed one of the monkeys but you used up four shots...')
                                ammo -= 4
                                print(f'You have {ammo}/8 ammo left...')
                            
                            if usedShots == '5':
                                print('You sucessfully killed one of the monkeys but you used up all five of your shots...')
                                ammo -= 5
                                print('You are now out of ammo!')

                    if river == 'check':
                        print('You found a canoe on the shore of the river...')
                        canoe = input('Do you take it, or go back and continue into the jungle? ')


            elif Follow == 'go back':
                print('You go back to the waterfall and wait...')
                back = input('You wait for 30 minutes, and he is still gone. Do you wait or go back and follow the footprints? ')
                if back == 'wait':
                    wait_more = input('Are you really gonna sit here and wait even longer? ')

                    if wait_more == 'yes':
                        print('You sat and waited for a month and you\'ve starved to death...')
                        print('Well at least your loyal...')
                    if loyal_unlocked == True:
                        print('You have already unlocked this ending!')
                    else:
                        print('You have unlocked the "Loyal" ending!')
                        Endings.append("Loyal")
                        print(f'You have unlocked {len(Endings)}/{max_ending} endings!')
                        loyal_unlocked = True

                    if wait_more == 'no':
                        print('You go back into the jungle, this time you follow the footprints...')
                        print('After a while you stumble onto a venomous snake...')
                        snake = input('Try to kill it, or try to sneak away? ')

                        if snake == 'kill':
                            snakeKillList = ["kill","die"]
                            snakeRandom = (random.choice(snakeKillList))
                            print('You pick up a rock and try to bash its head...')

                            if snakeRandom == "kill":
                                print('You sucessfully killed the snake!')
                            
                            if snakeRandom == "die":
                                print('You missed it and it bit you...')
                                print('The venom is really and you died after screaming for 3 minutes in pain and agony...')
                                if venom_unlocked == True:
                                    print('You have already unlocked this ending!')
                                else:
                                    print('You have unlocked the "Venom" ending!')
                                    Endings.append("venom")
                                    print(f'You have unlocked {len(Endings)}/{max_ending} endings!')
                                    venom_unlocked = True

                        if snake == 'sneak':
                            print('You try to sneak around the snake...')
                            print('The snake sees you and hisses at you...')
                            print('You tried to escape but the snake went in for a bite and hit you in your leg...')
                            print('The venom makes you weaker and weaker as you travel further into the jungle and suddenly you have to sit down up against a rock...')
                            print('Only minutes later you\'re dead...')
                            if venom_unlocked == True:
                                print('You have already unlocked this ending!')
                            else:
                                print('You have unlocked the "Venom" ending!')
                                Endings.append("venom")
                                print(f'You have unlocked {len(Endings)}/{max_ending} endings!')
                                venom_unlocked = True

                    if loyal_unlocked == True:
                        print('You have already unlocked this ending!')
                    else:
                        print('You have unlocked the "Loyal" ending!')
                        Endings.append("Loyal")
                        print(f'You have unlocked {len(Endings)}/{max_ending} endings!')
                        loyal_unlocked = True
                        
        elif response == 'wait':
            print('You wait for another 30 minutes, and he is still gone...')

        else:
            print('Invalid response! You lose...')
            if Stupid_unlocked == True:
                print('You have already unlocked this ending!')
            else:
                print('You have unlocked the "Stupid" ending!')
                Endings.append("stupid")
                print(f'You have unlocked {len(Endings)}/{max_ending} endings!')
                Stupid_unlocked = True
                
    elif setting == 'desert':
        print(f'Welcome {name}, to the almighty desert! Your tour guide took you to a nice looking oasis...') 
        print('He told you to sit down and wait for him to go do something...')
        response = input('Your tour guide has been gone for a while... Follow him or wait here?')
        if response == 'follow':
            print('You follow him over the dunes...')
        elif response == 'wait':
            print('You wait for another 30 minutes, and he is still gone...')
        else:
            print('Invalid response! You lose...')
            if Stupid_unlocked == True:
                print('You have already unlocked this ending!')
                
            else:
                print('You have unlocked the "Stupid" ending!')
                Endings.append("stupid")
                print(f'You have unlocked {len(Endings)}/{max_ending} endings!')
                Stupid_unlocked = True

    elif setting != '':
        print('Invalid response! You lose...')
        if Stupid_unlocked == True:
            print('You have already unlocked this ending!')
            
        else:
            print('You have unlocked the "Stupid" ending!')
            Endings.append("Stupid")
            print(f'You have unlocked {len(Endings)}/{max_ending} endings!')
            Stupid_unlocked = True

    playing = checkContinue()
    