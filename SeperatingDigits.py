number = int(input("Enter a five digit number: "))
num = 10000
separateNumber = ' '
while num >= 1:
    digit = number // num
    number = number % num
    num //= 10
    separateNumber += str(digit) + " "

print("separate Numbers: ", separateNumber)
