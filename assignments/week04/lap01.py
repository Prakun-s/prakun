"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Oshi", 0, "Nakonsawan", "thailand")  # name, age, city, country
    hobbies = []


    # Your code here
    while True:

        print("1.display into")
        print("2.add hobby")
        print("3.Remove hobby")
        print("4.Edit age")
        print('5.Exit')
        choice = input("What do you want to do :" )

        if choice == "1":
            print("Name : ", person[0])
            print("Age : ", person[1])
            print("City : ", person[2])
            print("conntry ; ", person[3])
            print("Hobbies : ", hobbies)

        elif choice == "2":
            hobby = input("insert new hobby : ")
            hobbies.append(hobby)
        
        elif choice == "3":
            del hobbies[0]
        
        elif choice == "4":
            age = input("insert new age : ")
            person_list = list(person) #["Oshi", 19, "Nakonsawan", "Thailand"]
            person_list[1] = age
            person = tuple(person_list)

        elif choice == "5":
            break
        

if __name__ == "__main__":
    personal_info_manager()
