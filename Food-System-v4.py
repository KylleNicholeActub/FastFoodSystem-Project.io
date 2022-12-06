# Menu
print(f'\nGood day customer, what would you like to buy? These are in our menu:\n')
menu = [['Food Menu', ['1: Burger = ₱30.10', '2: Fries = ₱15.50', '3: Fried Chicken = ₱40']],
        ['Drink Menu', ['1: Cola = ₱17.25', '2: Sprite = ₱15.50', '3: Water = Free']]]

for available in menu:
    print(available[0])
    for food in available[1]:
        print('*', food)
    print()

# Account
name = 'ivan'
passcode = 'pass123'

# Account confirmation
while True:
    username = input('Enter your username: ')
    while True:
        password = input('Enter password: ')
        
        if username != name and password == passcode:
            print('Incorrect username')
            break
        elif username == name and password != passcode:
            print('Incorrect password')
        elif username == name and password == passcode:
            while True:
            
                    # Food Menu
                pick_food = int(input('Enter your choice of food  from the Food Menu (1, 2, 3) or (4) to skip: \n'))
    
                print()
                if pick_food in (1, 2, 3, 4):
                    if pick_food == 1:
                        print(f'Burger costs ₱',food_result := 30.10)
                    elif pick_food == 2:
                        print(f'Fries costs ₱',food_result := 25.30)
                    elif pick_food == 3:
                        print(f'Fried chicken costs ₱',food_result := 40)
                    elif pick_food == 4:
                        print(f'Having drinks only are we?',
                        food_result := 0)
    
                    # Drink Menu
                    pick_drink = int(input('Enter your choice of drink from the Drinks Menu next (1, 2, 3) '
                                           'to finish your order: '))
                    print()
                    if pick_drink in (1, 2, 3):
                        if pick_drink == 1:
                            print(f'Cola costs ₱',drink_result := 17.25)
                        elif pick_drink == 2:
                            print(f'Sprite costs ₱',drink_result := 15.50)
                        elif pick_drink == 3:
                            print(f'Water is for costs ₱',drink_result := 0)
                        print(f'Your total amount of cash is',total := food_result + drink_result)
                    cash = float(input('Enter the amount of cash: ₱'))
    
                    if cash < total:
                        print('Not enough cash')
                        continue
                    else:
                        exit()
                    
    else:
        print('Wrong username or password, try again')
        continue