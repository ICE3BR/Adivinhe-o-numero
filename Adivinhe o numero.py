import random

def guess (x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Adivinhe um numero entre 1 e {x}: '))
        if guess < random_number:
            print('Desculpe, Adivinhe novamente. Muito baixo.')
        elif guess > random_number:
            print('Desculpe, Adivinhe novamente. Muito Alto.')

    print(f'BOA, Parabens. Você conseguiu adivinhar o numero {random_number} !!')


def computer_guess (x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess =  low
        feedback = input(f'Seria {guess} ? ; Muito Alto (H), Muito Baixo (L), ou Correto (C): ')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'BOA, Parabens. O computador adivinhou seu numero, {guess}, corretamente !!')

computer_guess (10)
guess (20)