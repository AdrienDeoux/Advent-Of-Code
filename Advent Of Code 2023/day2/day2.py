# @Author : Adrien Déoux

########################################################################
# Functions definitions
########################################################################

def make_bags(string_object):
    """
    :param string_object: a string object containing 1 bag information (see event description)
    :return: number of red, green, blue elements in the bag (string_object

    :example: '13 green, 3 red, 4 blue' will return 3, 13, 4
    """
    splited_string = string_object.split(' ')
    length = len(splited_string)
    red, green, blue = 0, 0, 0
    for idx in range(length):
        if splited_string[idx] in ['red', 'red,', 'red\n']:
            red = int(splited_string[idx - 1])
        elif splited_string[idx] in ['blue', 'blue,', 'blue\n']:
            blue = int(splited_string[idx - 1])
        elif splited_string[idx] in ['green', 'green,', 'green\n']:
            green = int(splited_string[idx - 1])
    return red, green, blue


if __name__ == '__main__':
    # open input from AoC
    file = open('input.txt', 'r')

    # make a classic list of str from file to be easily treated
    list_of_file = [i for i in file]

    one_bag = '4 red, 9 green, 4 blue'
    set_of_bags = 'Game 1: 13 green, 3 red; 4 red, 9 green, 4 blue; 9 green, 10 red, 2 blue'

    sum = 0 # first star solution
    sum2 = 0 #second star solution

    for game in list_of_file:
        # current Game number
        GameID = int(game.partition(': ')[0].partition('Game ')[2])

        #make a list of bags out of each game
        splited_list_of_bags = game.split(';')

        # is game possible as per elf explications
        is_possible = True

        # R G B will contain the highest number of red, green, blue, elements of all bags in one game
        R, G, B = 0, 0, 0

        for bag in splited_list_of_bags:
            red, green, blue = make_bags(bag)
            is_possible = is_possible and (red <= 12) and (green <= 13) and (blue <= 14)
            R, G, B = max(R, red), max(G, green), max(B, blue)

        # Star 1 : if game is possible then add the game number to the count
        if is_possible == True:
            sum += GameID

        # Star 2 : add the multiplication of the highest red, green, blue counts for each game
        sum2 += R*G*B

    print('The solution to get first star is : ' + str(sum))
    print('The solution to get second star is : ' + str(sum2))