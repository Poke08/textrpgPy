ending_count = 0
Stupid_unlocked = 'false'
lame_unlocked = 'false'
name = input('Enter your name! ')
print(f'Greetings {name}!')
start = input('Would you rather play the game or perish? ')
if start == 'play':
    print('Come on then, what are we waiting for!')
    setting = input(f'Ok {name}! Wanna go to the jungle or the desert? ')
else:
    print('Lame. You\'re dead...')
    if lame_unlocked == 'true':
        print('You have already unlocked this ending!')
        quit()
    else:
        print('You have unlocked the "Lame" ending!')
        ending_count = +1
        print(f'You have unlocked {ending_count}/2 endings!')
        lame_unlocked = 'true'
        quit()

if setting == 'jungle':
    print(f'Welcome {name}, to the almighty jungle! Your tour guide took you to a nice looking waterfall...') 
    print('He told you to sit down and wait for him to go do something...')
    response = input('Your tour guide has been gone for a while... Follow him or wait here?')
    if response == 'follow':
        print('You follow him into the jungle...')
    elif response == 'wait':
        print('You wait for another 30 minutes, and he is still gone...')
    else:
        print('Invalid response! You lose...')
        if Stupid_unlocked == 'true':
            print('You have already unlocked this ending!')
            quit()
        else:
            print('You have unlocked the "Stupid" ending!')
            ending_count = +1
            print(f'You have unlocked {ending_count}/2 endings!')
            Stupid_unlocked = 'true'
            quit()

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
        if Stupid_unlocked == 'true':
            print('You have already unlocked this ending!')
            quit()
        else:
            print('You have unlocked the "Stupid" ending!')
            ending_count = +1
            print(f'You have unlocked {ending_count}/2 endings!')
            Stupid_unlocked = 'true'
            quit()

else:
    print('Invalid response! You lose...')
    if Stupid_unlocked == 'true':
        print('You have already unlocked this ending!')
        quit()
    else:
        print('You have unlocked the "Stupid" ending!')
        ending_count = +1
        print(f'You have unlocked {ending_count}/2 endings!')
        Stupid_unlocked = 'true'
        quit()