import random

print('ROCK PAPER SCISSOR GAME!\n' + 
      'Game Rules \n'+
      'Rock vs Paper --> paper Wins\n '+
      'Rock vs Scissor --> Rock Wins\n' +
      'paper vs Scissor --> Scissor Wins\n')

while True:
    print('Enter Your Choice: \n 1. Rock \n 2. Paper \n 3. Scissor\n')
    choice= int(input('Enter Your Choice: '))
    
    while choice>3 or choice<1:
        choice= int(input('Please Enter Valid Choice: '))
    if choice==1:
        choice_name='Rock'
    elif choice==2:
        choice_name='Paper'
    else:
        choice_name='Scissor'
        print('User Choice is:',choice_name)
        print('Now its computer turn:')
        
    comp_choice= random.randint(1,3)
    while comp_choice==choice:
        comp_choice=random.randint(1,3)

    if comp_choice==1:
        comp_choice_name='Rock'
    elif comp_choice==2:
        comp_choice_name='Paper'
    else:
        comp_choice_name='Scissor'

        print('Computer choice is:',comp_choice_name)
        print(comp_choice_name,'VS',choice_name)

    if comp_choice==choice:
        print('Match Draw',end='')
        Result='Draw'
            
    if (choice==1 and comp_choice==2):
        print('Paper win:',end='')
        result='paper'

    elif (choice==2 and comp_choice==1):
        print('Paper Wins',end='')
        result='paper'
            
    if(choice==1 and comp_choice==3):
        print('Rock wins',end='')
        result='Rock'

    if(choice==3 and comp_choice==1):
        print('Rock Wins',end='')
        result='Rock'

    if(choice==2 and comp_choice==3):
        print('Scissor Win',end='')
        result='scissor'

    if(choice==3 and  comp_choice==2):
        print('Scissor Win:',end='')
        result='Scissor'

    if result== 'Draw':
        print("<== Its a Tie ==>")
    if result == choice_name:
        print("<== User Wins ==>")
    else:
        print("<==Computer Wins ==>")
        answer= input('Do YOU WANT TO CONTINUE (Y/N): ')
    if answer=='n':
        break
    else:
        continue