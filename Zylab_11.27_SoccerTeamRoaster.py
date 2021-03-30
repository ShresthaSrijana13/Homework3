# Srijana Shrestha
# 1918305

import collections  # import collection to sorting and ordering

dict1 = {}  # assigning empty dictionary

for i in range(1, 6):  # for loop to iterate 5 times
    jersey_number = int(input('Enter player {}\'s jersey number:\n'.format(i)))  # user input for jersey number
    rating = int(input('Enter player {}\'s rating:\n'.format(i)))  # user input for rating
    print()  # printing empty line

    dict1[jersey_number] = rating  # assigning jersey number to rating in dictionary
    dict2 = collections.OrderedDict(sorted(dict1.items()))  # sorting and ordering dictionary

print('ROSTER')  # printing header
for k, v in dict2.items():  # for loop to iterate in dictionary
    print('Jersey number:', str(k) + ',', 'Rating:', v)  # printing key and its value from dictionary

option = ''
while option.upper() != 'Q':  # while loop if option is not equal to Q
    print('\nMENU\na - Add player\nd - Remove player\nu - Update player rating\n' 'r - Output players above a rating\n'
          'o - Output roster\nq - Quit\n')  # printing menu
    option = input('Choose an option:\n')  # printing the user input

    if option == 'a':  # if condition for option a
        newJersey = int(input('Enter a new player\'s jersey number:\n'))  # printing user input for new jersey number
        newRating = int(input('Enter the player\'s rating:\n'))  # printing user input for new rating
        dict2.update({newJersey: newRating})  # updating new jersey number and new rating in dictionary

    elif option == 'd':  # if condition for option d
        delJersey = int(input('Enter a jersey number:\n'))  # printing user input for jersey number
        dict2.pop(delJersey)  # deleting key and value from dictionary

    elif option == 'u':  # if condition for option u
        jerseyKey = int(input('Enter a jersey number:\n'))  # printing user input for jersey number
        RatingValue = int(input('Enter a new rating for player:\n'))  # printing new rating
        dict2[jerseyKey] = RatingValue  # assigning key to the new value in dictionary

    elif option == 'r':  # if condition for option r
        dict3 = {}  # creating new dictionary
        rating = int(input('Enter a rating:\n'))  # printing new user input for rating
        for key, value in dict2.items():
            if value > rating:  # compare if value is greater than user input rating
                dict3.update({key: value})  # updating dict3 with value which greater than user input rating
        print('ABOVE {}'.format(rating))

        for k, v in dict3.items():
            print('Jersey number:', str(k) + ',', 'Rating:', v)  # printing updated key and value form dictionary

    elif option == 'o':  # if condition for option o
        print('ROSTER')
        dict2 = collections.OrderedDict(sorted(dict2.items()))  # sorting and ordering dictionary
        for k, v in dict2.items():
            print('Jersey number:', str(k) + ',', 'Rating:', v)  # printing the menu
