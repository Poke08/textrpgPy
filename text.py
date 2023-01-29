playing = False

setting = ''
lame_unlocked = False
Stupid_unlocked = False
loyal_unlocked = False

Endings = []
allEndings = ["lame","Stupid","Loyal"]
max_ending = len(allEndings)

def checkContinue():
    for ending in allEndings:
        if ending not in Endings:
            return True
    print(f"{name} you have beat the game!")
    return False

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
                        print('You go back to the footprints and decide to follow them...')
                        print('You follow the footprints for a while and you find the water bottle your tour guide was drinking from earlier...')
                        bottle = input('Do you pick it up or leave it? ')

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
    