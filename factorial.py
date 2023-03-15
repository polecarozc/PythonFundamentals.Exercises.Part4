number = input("Enter a number and i'll give you the factorial: ")

def factorial(n):
    answer = 1
    for i in range(1,n +1):
        answer = answer * i
    return answer
print(factorial(int(number)))