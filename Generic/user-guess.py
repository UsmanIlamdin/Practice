import random 
print(random.randint(1,5))  # Generate random number between 1 and 5 '''

def guess(X):
    random_number = random.randint(1 , X)
    user_guess = 0
    while random_number != user_guess:
        user_guess = int(input('Enter your guess number'))
        
        if user_guess > random_number:
            print('Too High')
        elif user_guess < random_number:
            print('Too Low')
        
    
    print(f'Yah you win your guess number is {random_number}')

upper_bound = int(input('Enter upper bound number'))
  # add upper bounf from users
guess(upper_bound)




