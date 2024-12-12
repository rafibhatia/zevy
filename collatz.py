def collatz(number):
    
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

user_number = int(input("Please enter a number: "))

while True:
    user_number = collatz(user_number)
    print(user_number)
    if user_number == 1:
        break
