import random
class inputAll():


    def checkname(self,name, name_type):
        if len(name)<50:
            return name
        else:
            print("enter name in the limit of 50 characters")
            name = self.checkname(input(f"Enter {name_type}: "),name_type)

    def checknum(self,mark,mark_type):
        if mark<=80 and mark>=0:
           return mark
        else:
             print("enter a valid mark")
             mark = self.checknum(int(input(f"Enter {mark_type}: ")),mark_type)       

    def __init__(self):

        self.name = self.checkname(input("Enter name: "), name_type = "name")

        self.mname = self.checkname(input("Enter Mother name: "), name_type = "mname")
        self.fname = self.checkname(input("Enter father name: "), name_type = "fname")
        self.stream = self.checkname(input("Enter Stream: "),name_type = "stream")
        self.school_n = input("Enter School name: ")
        self.ms_no = random.randrange(1000000,9999999)
        self.rno = random.randrange(1000000,9999999)
        self.cno = random.randrange(10000,99999)
        self.reg = random.randrange(1000000,9999999)
        #self.dob = date(input("Enter Your DOB:"))
        self.s1m = self.checknum(int(input("Enter the Marks of Hindi: ")), mark_type = "s1m")

        self.s2m = self.checknum(int(input("Enter the Marks of English: ")), mark_type = "s2m")
        self.s3m = self.checknum(int(input("Enter the Marks of Physics: ")), mark_type = "s3m")
        self.s4m = self.checknum(int(input("Enter the Marks of Chemistry: ")), mark_type = "s4m")
        self.s5m = self.checknum(int(input("Enter the Marks of Maths:" )), mark_type = "s5m")


    def displayAll(self):

        print("|","="*102,"|")
        print("|",f"{self.school_n:^95}",f"{'|':>8}")

        print("|",f"{'|':>104}")

        msc = f"Ms. No.: {self.ms_no}"
        print("|",f"{msc:>100}{'|':>4}")

        #print(f{:>80 "Ms. No.":{self.ms_no}})
        print("|","="*102,"|")

    
        
        print("|",f"Name: {self.name}",f"{'|':>91}")

        
        print("|",f"Mother Name: {self.mname}",f"{'|':>91}")
        print(f"Father Name: {self.fname}")
            
        print(f"\nRoll no.:{self.rno}"," "*20,f"\tCenter no.:{self.cno}")
        print(f"\nRegistration no.:{self.reg}"," "*15,f"Faculty:{self.stream}\n")
        print(f"College nmae/Schol Name: \n{self.school_n}\n")
        
        print("|","="*102,"|")

        print("Subjects"," "*4,"Marks\n")
        print(f"Hindi"," "*7,self.s1m)
        print(f"English"," "*5,self.s2m)
        print(f"Physics"," "*5,self.s3m)
        print(f"Chemistry"," "*3,self.s4m)
        print(f"Maths"," "*7,self.s5m)
    
        

inp = inputAll()

inp.displayAll()

