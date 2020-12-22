a=1
while a == True:
        try:
            num1 = float(input("Enter number one: "))
            a=0
        except ValueError:
            print("This input is invalid, try again")

method=False
while method == False:
    op = input('Enter operator(+,-,*,/):')
    if (op == '+'):
        method=1
    elif (op == '-'):
        method=2
    elif (op == '*'):
        method=3
    elif (op == '/'):
        method=4
    else: 
        print('You enered wrong operator, please try again')
        method = False
        
a=1
while a == True:
        try:
            num2 = float(input("Enter number two: "))
            a=0
        except ValueError:
            print("This input is invalid, try again")
            
a=1
while a == True:
    equal_sign = input("Enter equal mark: ")
    if equal_sign != '=':
        print("This is not equal mark, don't waste your precious time... ")
        a=1
    else: a=0    

print('The answer is: ')
if (method == 1):
    ans = num1 + num2
    print(ans)
elif (method == 2):
    ans = num1 - num2
    print(ans)
elif (method == 3):
    ans = num1 * num2
    print(ans)
elif (method == 4):
    ans = num1 / num2
    print(ans)
    