import random
class inputAll():
    def __init__(self):
        self.name = input("Enter name: ")
        self.mname = input("Enter Mother name: ")
        self.fname = input("Enter father name: ")
        self.stream = input("Enter Stream: ")
        self.school_n = input("Enter School name: ")
        self.ms_no = random.randrange(1000000,9999999)
        self.rno = random.randrange(1000000,9999999)
        self.cno = random.randrange(10000,99999)
        self.reg = random.randrange(1000000,9999999)
        #self.dob = date(input("Enter Your DOB:"))
        self.s1m=int(input("Enter the Marks of Hindi"))
        self.s2m=int(input("Enter the Marks of English"))
        self.s3m=int(input("Enter the Marks of Physics"))
        self.s4m=int(input("Enter the Marks of Chemistry"))
        self.s5m=int(input("Enter the Marks of Maths"))


    def displayAll(self):
        print(f"{self.school_n:^95}")
        msc = f"Ms. No.: {self.ms_no}"
        print(f"\n{msc:>100}")

        #print(f{:>80 "Ms. No.":{self.ms_no}})
        print(f"Name: {self.name}")
        print(f"Mother Name: {self.mname}")
        print(f"Father Name: {self.fname}")
            
        print(f"\nRoll no.:{self.rno}"," "*19,f"\tCenter no.:{self.cno}")
        print(f"\nRegistration no.:{self.reg}"," "*15,f"Faculty:{self.stream}\n")
        print(f"College nmae/Schol Name: \n{self.school_n}\n")
        
        print("Subjects"," "*4,"Marks\n")
        print(f"Hindi"," "*7,self.s1m)
        print(f"English"," "*5,self.s2m)
        print(f"Physics"," "*5,self.s3m)
        print(f"Chemistry"," "*3,self.s4m)
        print(f"Maths"," "*7,self.s5m)
    
        

inp = inputAll()
inp.displayAll()
