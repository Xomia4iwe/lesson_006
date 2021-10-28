from random import randint


def make_a_number():
    global _number
    _number = []
    _number.append(str(randint(1, 9)))
    while len(_number) < 4:
        random_number = str(randint(0, 9))
        if random_number not in _number:
            _number.append(random_number)



def check_the_number(guess_number):
    dict_bulls_cows = {'bulls': 0, 'cows': 0}
    for i in range(4):
        if guess_number[i] in _number:
            if guess_number[i] == _number[i]:
                dict_bulls_cows['bulls'] += 1
            else:
                dict_bulls_cows['cows'] += 1

    return print(' быки -', dict_bulls_cows['bulls'], ', коровы -', dict_bulls_cows['cows'])
