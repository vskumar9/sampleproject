from random import choice
def game(chance):
    listc=['r','p','s']
    user=0
    comp=0
    i=1
    while i<=chance:
        computer=str(choice(listc))
        userc=input('Enter the any one "r","p","s" : ').lower()
        if userc==computer:
            print('Tie')
        elif userc=='r':
            if computer=='p':
                print('you lose computer choice is paper')
                comp+=1
            else:
                print('you win, computer choice : ',computer)
                user+=1
        elif userc=='p':
            if computer=='s':
                print('you lose, computer choice is scissor')
                comp+=1
            else:
                print('you win, computer choice : ',computer)
                user+=1
        elif user=='s':
            if computer=='r':
                print('you lose, computer choice is rock')
                comp+=1
            else:
                print('you win, computer choice : ',computer)
                user+=1

        print()
        print('----------------score board---------------')
        print('\tyou:{} | computer:{}'.format(user,comp))
        print()
        print('game no:{}'.format(i))
        i+=1
    print('-----------------Game over-----------------')
    if user<comp:
        print('computer win the game computer score : ',computer)
    elif user==comp:
        print('Game is Tie')
    else:
        print('you win you score : ',user)
game(chance=int(input('Enter how times play game: ')))
                
            
