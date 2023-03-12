def print_popcorn_time(bag_ounces):

    if bag_ounces < 3:
        print('Too small')
    elif bag_ounces > 10:
        print('Too large')
    else:
        print( 6 * bag_ounces, 'seconds')
    return user_ounces    

user_ounces = int(input('enter oz: '))
print_popcorn_time(user_ounces)
