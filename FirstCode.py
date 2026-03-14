# with open("data.txt", "w") as file:
#     file.write("") 
command = 0
while command != 5:
    
    command = int(input("1.Show Student\n2.Add Student\n3.Update Student\n4.Delete Student\n5.Exit\n"))

    if command == 1:
        with open("data.txt", "r") as file:
            print(f"{file.read()}\n")
            

    elif command == 2:
        with open("data.txt", "a") as file:
            name = input("Name:")
            age = input("Age:")
            file.write(f"\n{name},{age}")

    elif command == 3:
        students = []
        upd = input("Print name,that you want to Update:")
        newname = input("NewName:")
        newage = int(input("NewAge:"))
        with open("data.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                name,age = line.strip().split(",")
                if name ==  upd:
                    students.append(f"{newname},{newage}")
                    if not line == lines[-1]:
                        students.append("\n")
                else:
                    students.append(line)
                    
        with open("data.txt", "w") as file:
            file.writelines(students)

    elif command == 4:
        students = []
        with open("data.txt", "r") as file:
            lines = file.readlines()
            students.extend(lines)
            print(students)
            delt = input("Name of the person that you want to delete: ")
            with open("data.txt", "w") as file:
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
