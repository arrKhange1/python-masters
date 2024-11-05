import random

def construct_validate_word(positions_list, guessed_word):
    validated_word_letters = []
    for idx, pos_status in enumerate(positions_list):
        if pos_status == 0:
            validated_word_letters.append(guessed_word[idx])
        elif pos_status == 1:
            validated_word_letters.append(f'({guessed_word[idx]})')
        elif pos_status == 2:
            validated_word_letters.append(f'[{guessed_word[idx]}]')
    return ''.join(validated_word_letters)

def validate_word(guessed_word, expected_word):
    positions_list = [0,0,0,0,0] # 0 - not guessed, 1 - partially guessed, 2 - fully guessed
    for i in range(len(guessed_word)):
        if guessed_word[i] == expected_word[i]:
            positions_list[i] = 2
        elif guessed_word[i] in expected_word:
            positions_list[i] = 1
    print(positions_list)
    return construct_validate_word(positions_list, guessed_word)

tries = 5
win = False
expected_word = 'joker'
while tries and not win:
    guessed_word = input('Make a guess: ')
    validated_word = validate_word(guessed_word, expected_word)
    print('Result for the try: ', validated_word)
    if guessed_word == expected_word:
        win = True
        print('You won!')
    tries -= 1