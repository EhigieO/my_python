""" Display the sum, average, product, smallest and
largest of the numbers. Note that each of these is a reduction in functionalstyle programming"""

numberOne = int(input("Enter first number:"))
numberTwo = int(input("Enter second number:"))
numberThree = int(input("Enter third number:"))

sumOfNumbers = numberOne + numberTwo + numberThree
averageOfNumbers = sumOfNumbers/3
productOfNumbers = numberOne * numberTwo * numberThree
smallestNumber = numberOne
if smallestNumber > numberTwo:
    smallestNumber = numberTwo
if numberThree < smallestNumber:
    smallestNumber = numberThree

largestNumber = numberOne
if largestNumber < numberTwo:
    largestNumber = numberTwo
if largestNumber < numberThree:
    largestNumber = numberThree


print('Sum of numbers is ', sumOfNumbers)

print('Average of numbers is ', averageOfNumbers)
print('Product of numbers is ', productOfNumbers)
print('Smallest of numbers is ', smallestNumber)
print('largest of numbers is', largestNumber)