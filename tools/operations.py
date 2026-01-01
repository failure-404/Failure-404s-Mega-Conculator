#addition

def addition(numbers):
    sum = 0
    for number in numbers:
        sum = sum+number
    print(sum)


'''user_input = input(f'Input the numbers you want to add, seperated by spaces: ')
numbers_list = [int(x) for x in user_input.split()]
addition(numbers_list)'''


#substraction

def substraction(numbers):
    diff = 0
    i = 0
    for number in numbers:
        if i == 0:
            diff = number
        else:
            diff = diff-number
        i += 1
    print(diff)

'''user_input = input(f'Input the numbers you want to add, seperated by spaces: ')
numbers_list = [int(x) for x in user_input.split()]
substraction(numbers_list)'''


#multiplication

def multiplication(numbers):
    prod = 1
    for number in numbers:
        prod = prod*number
    print(prod)

'''user_input = input(f'Input the numbers you want to add, seperated by spaces: ')
numbers_list = [int(x) for x in user_input.split()]
multiplication(numbers_list)'''


#division

def division(numbers):
    quot = 1
    i = 0
    for number in numbers:
        if i == 0:
            quot = number
        else:
            quot = quot/number
        i += 1
    print(quot)

user_input = input(f'Input the numbers you want to add, seperated by spaces: ')
numbers_list = [int(x) for x in user_input.split()]
division(numbers_list)