def find_recursive_sum(number_to_sum_to):
    print(f'we are going to sum up to: {number_to_sum_to}.')
    
    if 1 == number_to_sum_to:
        print('now we can return 1')
        return 1
    else:
        print('we are not at the base case.')
        if 0 == number_to_sum_to % 2:
            print('our number is even')
            print('so we don\'t need to add anything')
            print(f'skip {number_to_sum_to} and keep adding with {number_to_sum_to - 1}.')
            return find_recursive_sum(number_to_sum_to - 1)
        else:
            print('our number is odd')
            print(f'we are going to add {number_to_sum_to} and {number_to_sum_to - 1}.')
            return number_to_sum_to + find_recursive_sum(number_to_sum_to - 1)

def find_simple_sum(number_to_sum_to):
    #print(f'we are going to sum up to: {number_to_sum_to}.')
    sum = 0
    for our_number in range(1, (number_to_sum_to + 1)):
        #print(f'our number is: {our_number}.')
        #sum = sum + our_number
        if not 0 == our_number % 2:
            sum += our_number
        #print(f'sum is now: {sum}.')
    return sum

if __name__ == '__main__':
    print('welcome to the problem 5.4.9.')
    print('what is the sum of n positive odd numbers?')

    user_selected_positive_integer = int(input('what do you want to sum up to? '))
    #print(f'you entered {user_selected_positive_integer}.')

    simple_sum = find_simple_sum(user_selected_positive_integer)
    print(f'the simple function says the sum is: {simple_sum}.')

    recursive_sum = find_recursive_sum(user_selected_positive_integer)
    print(f'the recursive function says the sum is: {recursive_sum}.')