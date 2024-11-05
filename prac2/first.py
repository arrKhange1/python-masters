import random

def gen_four_unique_digit_number():
    first_digit = 0
    while first_digit == 0:
        first_digit, second_digit, third_digit, fourth_digit = random.sample(range(10), 4)
    return 1000*first_digit + 100*second_digit + 10*third_digit + fourth_digit

def count_cows_and_bulls(guessed_number: int, expected_number: int):
    cows = 0
    bulls = 0
    guessed_number_str = str(guessed_number)
    expected_number_str = str(expected_number)
    for i in range(len(guessed_number_str)):
       
       if guessed_number_str[i] == expected_number_str[i]:
           cows += 1
       elif guessed_number_str[i] in expected_number_str:
           bulls += 1 
    return (cows, bulls)

expected_number = gen_four_unique_digit_number()
print('expected: ', expected_number)
count_tries = 0
win = False
while win != True:
    guessed_number = int(input('Make a guess: '))
    count_tries += 1
    cows, bulls = count_cows_and_bulls(guessed_number, expected_number)
    print('Cows: ', cows, ' Bulls: ', bulls)
    if cows == 4:
        win = True
        print('You won!')
        print('Tries used: ', count_tries)