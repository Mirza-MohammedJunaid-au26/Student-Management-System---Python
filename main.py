### STUDENT MANAGMENT SYSTEM

class AttainU:
    
    roll_no = 1
    Attain_U = []
    def __init__(self):
        self.Welcome()

    def Welcome(self):
        print()
        print("!!! Welcome to AttainU !!!")
        print("1. Create Student Details")
        print("2. Access Student Details")
        print("3. Delete Student Details")        
        print("4. All Student Details")        
        print("5. Edit Student Details")        
        opt_inp = int(input("Enter Option : "))
        if opt_inp == 1:
            self.create_Student()            
        elif opt_inp == 2:
            self.Access_Student()            
        elif opt_inp == 3:
            self.Delete_Student()            
        elif opt_inp == 4:
            self.All_Student()            
        elif opt_inp == 5:
            self.Edit_Student()            
        else:
            print("!!! Enter Valid Option !!!")
            self.Welcome()            
    
    def create_Student(self):
        student_FName = input("First Name : ")
        student_MName = input("Middle Name : ")
        student_LName = input("Last Name : ")
        student_std = input("Enter Std : ")
        student_fees = input("Fees Paid :")  
        s = student_FName[0]

        if s == "a" or s == "A" or s == "b" or s == "B" or s == "c" or s == "C":
            print("!!! Congratulation !!!")
            print(student_FName,student_MName,student_LName,"Your Division is A")
            div = "A"
            print("Your Roll No is :",self.roll_no)
        elif s == "d" or s == "D" or s == "e" or "E" or s == "f" or s == "F":
            print("!!! Congratulation !!!")
            print(student_FName,student_MName,student_LName,"Your Division is B")
            div = "B"
            print("Your Roll No is :",self.roll_no)
        elif s == "g" or s == "G" or s == "h" or s == "H" or s == "i" or s == "I":
            print("!!! Congratulation !!!")
            print(student_FName,student_MName,student_LName,"Your Division is C")
            div = "C"
            print("Your Roll No is :",self.roll_no)
        else:
            print("!!! Congratulation !!!")
            print(student_FName,student_MName,student_LName,"Your Division is D")
            div = "D"
            print("Your Roll No is :",self.roll_no)

        for i in range(1):
            self.Attain_U.append(self.roll_no)
            self.Attain_U.append(student_FName)
            self.Attain_U.append(student_MName)
            self.Attain_U.append(student_LName)
            self.Attain_U.append(student_std)
            self.Attain_U.append(div)
            self.Attain_U.append(student_fees)

        self.roll_no = self.roll_no+1

        self.Welcome()

    def Access_Student(self):
        access_Student = int(input("Enter Roll No :"))

        index = self.Attain_U.index(access_Student)
   
        print("First Name :",self.Attain_U[index+1])
        print("Middle Name :",self.Attain_U[index+2])
        print("Last Name :",self.Attain_U[index+3])
        print("Roll No :",self.Attain_U[index])
        print("Std :",self.Attain_U[index+4])
        print("Div :",self.Attain_U[index+5])
        print("Fees Paid :",self.Attain_U[index+6])
        
        self.Welcome()

    def Delete_Student(self):
        delete_Student = int(input("Enter Roll No :"))

        delete_index = self.Attain_U.index(delete_Student)

        for i in range(7):
            self.Attain_U.pop(delete_index)

        print("!!! Deleted Successfully !!!")

        self.Welcome()     

    def All_Student(self):
        print("Rollno   FName        MName       LName         Std      Div     Fees Paid")
        
        index_i = 0

        if index_i<len(self.Attain_U):
            for i in range(index_i,len(self.Attain_U)):
                print(self.Attain_U[i],end="        ")
                if i<=6:
                    if i%6==0 and i>0:
                        print(" ")
                else:
                    if i%7==0 and i>7:
                        print(" ")
        self.Welcome()

    def Edit_Student(self):
        student_inp = int(input("Enter Roll No"))
        index = self.Attain_U.index(student_inp)
        print("First Name :",self.Attain_U[index+1])
        print("Middle Name :",self.Attain_U[index+2])
        print("Last Name :",self.Attain_U[index+3])
        print("Roll No :",self.Attain_U[index])
        print("Std :",self.Attain_U[index+4])
        print("Div :",self.Attain_U[index+5])
        print("Fees Paid :",self.Attain_U[index+6])

        print("Choose Option For Changes")
        
        print("1. First Name")
        print("2. Middle Name")
        print("3. Last Name")
        print("4. std")
        print("5. Div")
        print("6. Fees Paid")
        opt = int(input("Enter :"))
        
        if opt==1:
            fname = input("Enter First Name : ")
            self.Attain_U[index+1] = fname
            print("!!!First Name Changed Successfully!!!") 
        elif opt==2:
            mname = input("Enter Middle Name : ")
            self.Attain_U[index+2] = mname
            print("!!!Middle Name Changed Successfully!!!") 
        elif opt==3:
            lname = input("Enter Last Name : ")
            self.Attain_U[index+3] = lname
            print("!!!Last Name Changed Successfully!!!") 
        elif opt==4:
            student_std = input("Enter Std : ")
            self.Attain_U[index+4] = student_std
            print("!!!Std Changed Successfully!!!") 
        elif opt==5:
            student_div = input("Enter Div : ")
            self.Attain_U[index+5] = student_div
            print("!!!Division Changed Successfully!!!") 
        elif opt==6:
            fees_paid = input("Enter Fees : ")
            self.Attain_U[index+6] = fees_paid
            print("!!!Fees Changed Successfully!!!") 
        else:
            print("Enter Valid Number")
            self.Edit_Student()
        
        self.Welcome()
        
obj= AttainU()
