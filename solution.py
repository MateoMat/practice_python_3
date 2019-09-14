def numbers_lower_than_input():
    user_input = input("Write a number, and I will show you my number which is lower in a list:")
    my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print([aa for aa in my_list if aa < int(user_input)])
    


numbers_lower_than_input()

