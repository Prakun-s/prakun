# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")

    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option (1-4) : ")
    
        if choice == "1":
             print("Now, you have : ",balance)

        if choice == "2":
            withdraw = float(input("Withdraw amount :"))
            if withdraw <= balance:
                balance = balance - withdraw
                print("Now, you have : ",balance)

        if choice == "3":
            deposit = float(input("Deposit amount :"))
            if deposit <= balance:
                balance = balance + deposit
                print("Now, you have : ",balance)

        if choice == "4":
            print("Thank you to use out ATM")
            break

else:
    print("Invalid PIN")
