def calculator():
    print("Select Operator")
    print('1.Add')
    print('2.Subract')
    print("3.Multiply")
    print("4.Divide")
choice = input('Enter Choice(1/2/3/4):')
num1=float(input('Enter First Number'))
num2=float(input('Enter Second Number'))

if choice == '1':
    result = num1 + num2
    print('The Result Is',result)
elif choice == '2':
    result = num1 - num2
    print('The Result Is',result)
elif choice == '3':
    result = num1 * num2
    print('The Result Is',result)
elif choice == '4':
    if num2!= 0:
        result = num1 + num2
        print('The Result Is',result)
    else:
        print("Error!")
