# with open("data2.txt", "w") as file:
#     file.write("") 

command = 0
while command != 5:
    
    command = int(input("1.Show Student\n2.Add Student\n3.Update Student\n4.Delete Student\n5.Exit\n"))

    if command == 1:
        with open("data2.txt", "r") as file:
            print(f"{file.read()}\n")
            

    elif command == 2:
        with open("data2.txt", "a") as file:
            Id = input("Id:")
            first_name = input("First Name:")
            last_name = input("Last Name:")
            email = input("Email:")
            phone_number = input("Phone Number:")
            file.write(f"\n{Id},{first_name},{last_name},{email},{phone_number}")

    elif command == 3:
        students = []
        upd = input("Print Id, that you want to Update:")
        new_Id = int(input("New Id:"))
        new_first_name = input("New First Name:")
        new_last_name = input("New Last Name:")
        new_email = input("New email:")
        new_phone_number = (input("New Phone Number:"))

        with open("data2.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                Id, first_name, last_name, email, phone_number = line.strip().split(",")
                if Id ==  upd:
                    students.append(f"{new_Id},{new_first_name},{new_last_name},{new_email},{new_phone_number}")
                    if not line == lines[-1]:
                        students.append("\n")
                else:
                    students.append(line)
                    
        with open("data2.txt", "w") as file:
            file.writelines(students)

    elif command == 4:
        students = []
        with open("data2.txt", "r") as file:
            lines = file.readlines()
            students.extend(lines)
            print(students)
            delt = input("Id of the person that you want to delete: ")
            with open("data2.txt", "w") as file:
                for line in students:
                    if not line.startswith(delt):
                        file.write(line)

    else:
        if command == 5:
            print("Successful Exit")
            break
        else:
            print("Worng Command")
            break
