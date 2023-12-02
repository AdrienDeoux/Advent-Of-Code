# @Author : Adrien Déoux

########################################################################
# Functions definitions
########################################################################

def replace_str_in_word(word):
    """
    :param word: a string object containing at least one number
    :return: same word but adding actual int to string number when they are spelled

    :example: 'twone3four' will return '2tw1one34four'
    """
    new_word = ''
    length_word = len(word)
    i = 0

    while(i < length_word):
        idx = i
        if word[idx:idx+3] == ('one'):
            new_word += '1'
        elif word[idx:idx+3] == ('two'):
            new_word += '2'
        elif word[idx:idx+3] == ('six'):
            new_word += '6'
        elif word[idx:idx+4] == ('zero'):
            new_word += '0'
        elif word[idx:idx+4] == ('four'):
            new_word += '4'
        elif word[idx:idx+4] == ('five'):
            new_word += '5'
        elif word[idx:idx+4] == ('nine'):
            new_word += '9'
        elif word[idx:idx+5] == ('three'):
            new_word += '3'
        elif word[idx:idx+5] == ('seven'):
            new_word += '7'
        elif word[idx:idx+5] == ('eight'):
            new_word += '8'
        new_word += word[idx]
        i += 1
    return new_word

def get_nbr(word):
    """
    :param word: a string object containing at least one number
    :return: first and last digit number showing in word will return a new number
    and if there is only one number in word then first number takes both roles

    :example: 'dathreefg1fdsgdf5gdf' will return 35
    """
    new_word = word
    nombre = '0123456789'
    first = -1
    second = -1
    for i in new_word:
        if i in nombre:
            if first == -1:
                first = int(i)
            else:
                second = int(i)
    if second == -1:
        return 10 * first + first
    else :
        return 10 * first + second

if __name__ == '__main__':
    # open input from AoC
    file = open('input.txt', 'r')

    # make a classic list of str from file to be easily treated
    list_of_file = [i for i in file]

    sum = 0 # first star solution
    sum2 = 0 #second star solution
    for i in list_of_file:
        sum += get_nbr(i)
        sum2 += get_nbr(replace_str_in_word(i))

    print('The solution to get first star is : ' + str(sum))
    print('The solution to get second star is : ' + str(sum2))
