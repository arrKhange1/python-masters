import random
import time

def generate_RPS():
    variants = ['rock', 'paper', 'scissors']
    return random.choice(variants)

def get_game_status(generated_RPS, user_RPS):
    if generated_RPS == user_RPS: return 2
    rps_to_winner = { 'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper' }
    return 1 if rps_to_winner[user_RPS] == generated_RPS else 0

def play_RPS():
    my_RPS = input('Your RPS: ')
    generated_RPS = generate_RPS()
    print('Rock!')
    time.sleep(1)
    print('Paper!')
    time.sleep(1)
    print('Scissors!')
    time.sleep(0.5)
    game_status = get_game_status(generated_RPS, my_RPS)
    print(f'I got {generated_RPS}, {'You won D;' if game_status == 1 else 'You lost ;D' if game_status == 0 else 'Draw'}')

play_RPS()