principal = int(input("Enter amount: "))
numberOfYears = 1
rate = 7 / 100
while numberOfYears < 31:
    amount = principal * ((1 + rate) ** numberOfYears)
    numberOfYears += 1

    if numberOfYears == 10:
        print('Total amount at year 10: ', amount)
    if numberOfYears == 20:
        print('Total amount at year 20: ', amount)
    if numberOfYears == 30:
        print('Total amount at year 30: ', amount)
