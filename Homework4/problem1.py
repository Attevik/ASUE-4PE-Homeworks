import random

num_of_iterations = int( input( 'How many iterations?' ) )
num_of_wins = 0
change = 0
no_change = 0

while num_of_iterations > 0:
    List = [1, 2, 3]
    num_of_iterations -= 1
    prize = random.choice(List)
    guess = int( input('Guess a door between 1,2,3?'))
    List.remove(prize)
    rem = random.choice(List)
    List.remove(rem)
    if rem != guess:
        print('Host removed the door number: ', rem)
    else:
        print('Host removed the door number: ', List[0])
    answer = (input('Do you want to change your choice?, Answer yes or no'))
    if answer == 'yes':
        if guess == prize:
            print('You lose')
        else:
            change += 1
            num_of_wins += 1
            print('You won')
    if answer == 'no':
        if guess == prize:
            no_change += 1
            num_of_wins += 1
            print('You won')
        else:
            print('You lose')
print('Probability of winning when changing:', change/num_of_wins*100)
print('Probability of winning when NOT changing:', no_change/num_of_wins*100)
