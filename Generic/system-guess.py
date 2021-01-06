import random

def system_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low,high)
        feedback = input(f'Is {guess} too High(H) , too Low(L) , Correct guess??').lower()

        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
        
    
    print(f'Yah system just won nad guess the right number {guess}')
system_guess(100)