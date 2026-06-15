import random
class inputAll():


    def checkname(self,name, name_type):
        if len(name)<50:
            return name
        else:
            print("enter name in the limit of 50 characters")
            name = self.checkname(input(f"Enter {name_type}: "),name_type)

    def checknum(self,mark,mark_type):
        ''' if type(mark) is not int:
            print("Enter marks in integer format")
            return self.checknum(int(input(f"Enter {mark_type}: ")),mark_type)'''

        if mark<=80 and mark>=0:
            return mark
        
        else:
            print("enter a valid mark")
            self.checknum(int(input(f"Enter {mark_type}: ")),mark_type) 

    def checknum1(self,pmark,pmark_type):
        if pmark<=20 and pmark>=0:
           return pmark
        else:
             print("Enter number between 0 to 20")
             return self.checknum1(int(input(f"Enter {pmark_type}: ")),pmark_type)

                   

    def __init__(self):

        self.name = self.checkname(input("Enter name: "), name_type = "name")

        self.mname = self.checkname(input("Enter Mother name: "), name_type = "mname")
        self.fname = self.checkname(input("Enter father name: "), name_type = "fname")
        self.stream = self.checkname(input("Enter Stream (PCM,PCB,Commerce): "),name_type = "stream")
        self.school_n = input("Enter School name: ")
        self.ms_no = random.randrange(1000000,9999999)
        self.rno = random.randrange(1000000,9999999)
        self.cno = random.randrange(10000,99999)
        self.reg = random.randrange(1000000,9999999)
        #self.dob = date(input("Enter Your DOB:"))
        self.s1m = self.checknum(int(input("Enter the Marks of Hindi: ")), mark_type = "Theroy marks of hindi")

        self.s2m = self.checknum(int(input("Enter the Marks of English: ")), mark_type = "Thoery marks of English")
        self.s3m = self.checknum(int(input("Enter the Marks of Physics: ")), mark_type = "Thoery marks of Physics")
        self.s4m = self.checknum(int(input("Enter the Marks of Chemistry: ")), mark_type = "Thoery marks of Chemistry")
        self.s5m = self.checknum(int(input("Enter the Marks of Maths:" )), mark_type = "Thoery marks of Maths")


        self.p1m = self.checknum1(int(input("Enter the Practical Marks of Hindi: ")), pmark_type = "Practical marks of hindi")

        self.p2m = self.checknum1(int(input("Enter the Practical Marks of English: ")), pmark_type = "Practical marks of English")
        self.p3m = self.checknum1(int(input("Enter the Practical Marks of Physics: ")), pmark_type = "Practical marks of Physics")
        self.p4m = self.checknum1(int(input("Enter the Practical Marks of Chemistry: ")), pmark_type = "Practical Marks of Chemistry")
        self.p5m = self.checknum1(int(input("Enter the Practical Marks of Maths:" )), pmark_type = "Practical Marks of Maths")


        self.hindi = self.s1m + self.p1m
        self.eng = self.s2m + self.p2m
        self.phy = self.s3m + self.p3m
        self.chem = self.s4m + self.p4m
        self.math = self.s5m + self.p5m


        self.total= self.hindi + self.eng + self.phy + self.chem + self.math

    def displayAll(self):

        print('|'+"="*104+'|')
        print("|",f"{self.school_n:^95}",f"{'|':>8}")

        print("|",f"{'|':>104}")

        msc = f"Ms. No.: {self.ms_no}"
        print("|",f"{msc:>100}{'|':>4}")

        #print(f{:>80 "Ms. No.":{self.ms_no}})
        print('|'+"="*104+'|')

    
        
        text = f"Name: {self.name}"
        print("|"+text+(" "*(104-len(text)))+"|")

        
        text = f"Mother Name: {self.mname}"
        print("|"+text+(" "*(104-len(text)))+"|")
        
        text = f"Father Name: {self.fname}"
        print("|"+text+(" "*(104-len(text)))+"|")
            
        print('|'+f"{'|':>105}")

        print('|'+f"Roll no.:{self.rno}"," "*35,f"Center no.:{self.cno}"+" "*35+'|')


        text= f"Registration no.:{self.reg}"+" "*27+f"Stream:{self.stream}"
        print('|'+text+(" "*(104-len(text)))+'|')
        
        print('|'+" "*104+'|')

        print('|'+"College name/School Name:"+" "*79+'|')
        print('|'f"{self.school_n}"+(" "*(104-len(self.school_n)))+'|')
        print('|'+" "*104+'|')
        
        print("|"+"="*104+"|")


        print('|'+" Subjects"," "*2+'|'+'  ',"Theory Marks"," "*3+'|'+' ',"Practical Marks"," "*2+'|'+'  '
            ,"Full Marks"," "*2+'|'+' ',"Pass Mark"," "*1+'|',"Total Marks"," "*6+'|')

        print("|"+"="*104+"|")

        print('|'+f" {'Hindi'}{'|':>7}{self.s1m:^19}|{self.p1m:^20}|{'100':^16}|{'33':^13}|{self.hindi:^19}|")
        print('|'+f" {'English'}{'|':>5}{self.s2m:^19}{'|'}{self.p2m:^20}{'|'}{'100':^16}{'|'}{'33':^13}|{self.eng:^19}|")
        print('|'+f" Physics{'|':>5}{self.s3m:^19}|{self.p3m:^20}|{'100':^16}|{'33':^13}|{self.phy:^19}|")
        print('|'+f" Chemistry{'|':>3}{self.s4m:^19}|{self.p4m:^20}|{'100':^16}|{'33':^13}|{self.chem:^19}|")
        print('|'+f" Maths{'|':>7}{self.s5m:^19}|{self.p5m:^20}|{'100':^16}|{'33':^13}|{self.math:^19}|")


        print('|'+"="*104+'|')

        print('|'+f"Total Agregate: {self.total}")

        if(self.total<166):
            print('|'+"Result: FAIL"+" "*92+'|')

        else:
             print('|'+"Result: PASS"+" "*92+'|') 



        if(self.total>299):
             print('|'+"Division: 1st"+" "*91+'|')

        elif(self.total<300 and self.total>249):
             print('|'+"Division: 2nd"+" "*91+'|')

        elif(self.total<250 and self.total>164):
            print('|'+"Division: 3rd"+" "*91+'|')

        else:
            print('|'+"Division: 4th"+" "*91+'|')        
        
        print('|'+"="*104+'|')


inp = inputAll()

inp.displayAll()

