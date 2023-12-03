# @Author : Adrien Déoux

########################################################################
# Functions definitions
########################################################################
nombres = '0123456789'
dot = '.'
star = '*'
def check_around_nbr(input_list, i, jmin, jmax):
    length_x = len(input_list)
    length_y = len(input_list[0])

    boolean_check = True
    for idx_i in range (max(0, i - 1), min(length_x, i + 2)):
        for idx_j in range(max(0, jmin - 1), min(length_y-2, jmax + 2)):
            boolean_check = boolean_check and (input_list[idx_i][idx_j] in (nombres + dot))

    return boolean_check

def check_around_star(input_list, i, j):
    length_x = len(input_list)
    length_y = len(input_list[0])

    list_nbr = []
    for idx_i in range (max(0, i - 1), min(length_x, i + 2)):
        idx_j = max(0, j - 1)
        while ((idx_j > 0) and (idx_j < min(length_y - 2,j + 2))):
            min_j, max_j = idx_j, idx_j
            if input_list[idx_i][idx_j] in nombres:
                while ((min_j > 0) and (input_list[idx_i][min_j - 1] in nombres)):
                    min_j -= 1
                while ((max_j < length_y - 2) and (input_list[idx_i][max_j + 1] in nombres)):
                    max_j += 1
                if not check_around_nbr(input_list, idx_i, min_j, max_j):
                    list_nbr.append(int(input_list[idx_i][min_j:max_j+1]))
            idx_j = max_j + 1
    print(list_nbr)
    return list_nbr

def multiply_list_ele(my_list):
    result = 1
    for element in my_list:
        result *= element
    return result

if __name__ == '__main__':
    # open input from AoC
    file = open('input.txt', 'r')
    test = ["467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598.."]

    # make a classic list of str from file to be easily treated
    list_of_file = [line for line in file]

    length_x = len(list_of_file)
    length_y = len(list_of_file[0])

    sum1 = 0 # first star solution
    sum2 = 0 # second star solution

    idx_i = 0
    while (idx_i < length_x):
        idx_j = 0
        while (idx_j < length_y-2):
            input_ij = list_of_file[idx_i][idx_j]
            if (input_ij in nombres):
                temp_nbr = input_ij
                jmin, jmax, i = idx_j, idx_j, idx_i
                while ((idx_j < length_y) and (list_of_file[idx_i][idx_j + 1] in nombres)):
                    idx_j += 1
                    jmax = idx_j
                    temp_nbr += list_of_file[idx_i][idx_j]
                if not check_around_nbr(list_of_file, idx_i, jmin, jmax):
                    sum1 += int(temp_nbr)
            idx_j += 1
        idx_i += 1

    idx_i = 0
    while (idx_i < length_x):
        idx_j = 0
        while (idx_j < length_y - 2):
            input_ij = list_of_file[idx_i][idx_j]
            if input_ij in star:
                list_of_neighboors = check_around_star(list_of_file, idx_i, idx_j)
                if len(list_of_neighboors) > 1:
                    sum2 += multiply_list_ele(list_of_neighboors)
            idx_j += 1
        idx_i += 1

    print('The solution to get first star is : ' + str(sum1))
    print('The solution to get second star is : ' + str(sum2))
