from db import con,cur
import random
class inputAll():


    def checkname(self,name, name_type):

        name = name.strip()

        if len(name)==0:
            print("Field cannot be empty")
            return self.checkname(input(f"Enter {name_type}:"),name_type)

        if len(name)>50:
            print("enter name in the limit of 50 characters")
            return self.checkname(input(f"Enter {name_type}: "),name_type)


        for word in name.split():
            if not word.isalpha():
                print("It contain only alphabet and spaces")
                return self.checkname(input(f"Enter {name_type}:"),name_type)

        return name        

    def checknum(self,mark,mark_type):

        while True:
            mark = input(f"Enter {mark_type}:")
            if len(mark)==0:
                print("Field cannot be empty")
                continue

            if not mark.isdigit():
                print("Only numbers are allowed")
                continue

            mark = int(mark)

            if mark<=80 and mark>=0:
                return mark
        
            else:
                print("enter a valid mark")
                continue 

    def checknum1(self,pmark,pmark_type):
        while True:
            pmark = input(f"Enter {pmark_type}:")
            if len(pmark)==0:
                print("Field cannot be empty")
                continue

            if not pmark.isdigit():
                print("Only numbers are allowed")
                continue

            pmark = int(pmark)    

            if pmark<=20 and pmark>=0:
                return pmark

            else:
                print("Enter number between 0 to 20")
                continue


        '''if len(pmark)==0:
            print("Field cannot be empty")
            return self.checknum1(input(f"Enter {pmark_type}:"),pmark_type)

        if not pmark.isdigit():
            print("Only numbers are allowed")
            return self.checknum1(input(f"Enter {pmark_type}: "),pmark_type)

        pmark = int(pmark)    

        if pmark<=20 and pmark>=0:
           return pmark

        else:
             print("Enter number between 0 to 20")
             return self.checknum1(input(f"Enter {pmark_type}: "),pmark_type)'''
        
    def get_roll(self):
        while True:
            roll_no = input("Enter your roll number: ")

            if len(roll_no)==0:
                print("Roll number cannot be empty:")
                continue
            
            if not roll_no.isdigit():
                print("Roll number should be in Int numbers")
                continue
            
            if len(roll_no)!=7:
                print("Enter number in 7 digits")
                continue

            roll_no = int(roll_no)

            cur.execute("SELECT roll_no FROM students where roll_no = %s",(roll_no,))

            data = cur.fetchone()

            if data:
                print("Roll number already exist")
                continue

            return int(roll_no) 

            

    def insert_all(self):
        
        query = """INSERT into students(
                roll_no,
                name,
                mother_name,father_name,
                stream,school_name,
                ms_no,center_no,reg_no,
                hindi_theory,english_theory,physics_theory,chemistry_theory,maths_theory,
                hindi_practical,english_practical,physics_practical,chemistry_practical,maths_practical,
                hindi_total,english_total,physics_total,chemistry_total,maths_total,grand_total
                )

                values(%s,%s,%s,%s,%s,
                       %s,%s,%s,%s,%s,
                       %s,%s,%s,%s,%s,
                       %s,%s,%s,%s,%s,
                       %s,%s,%s,%s,%s)

                """
        values = (
                  self.rno,self.name,self.mname,self.fname,self.stream,self.school_n,
                  self.ms_no,self.cno,self.reg,self.s1m,self.s2m,self.s3m,self.s4m,self.s5m,
                  self.p1m,self.p2m,self.p3m,self.p4m,self.p5m,self.hindi,self.eng,self.phy,self.chem,
                  self.math,self.total
                  )          

        cur.execute(query,values)
        con.commit()
        print("Data saved")


    def get_student(self):

        roll_no = input("Enter your roll number:")

        cur.execute("SELECT * From students where roll_no=%s",(roll_no,))

        data = cur.fetchone()

        if not data:
            print("Student not found")
            return

        self.rno = data[0]
        self.name = data[1]
        self.mname = data[2]
        self.fname = data[3]
        self.stream = data[4]
        self.school_n = data[5]
        self.ms_no = data[6]
        self.cno= data[7]
        self.reg = data[8]
        self.s1m = data[9]
        self.s2m = data[10]
        self.s3m = data[11]
        self.s4m = data[12]
        self.s5m = data[13]
        self.p1m = data[14]
        self.p2m = data[15]
        self.p3m = data[16]
        self.p4m = data[17]
        self.p5m = data[18]
        self.hindi = data[19]
        self.eng = data[20]
        self.phy = data[21]
        self.chem = data[22]
        self.math = data[23]
        self.total = data[24]

        self.displayAll()


    def update(self):
        roll_no = input("Enter the roll number which you want to update: ")

        cur.execute("SELECT * FROM students where roll_no=%s",(roll_no,))

        data = cur.fetchone()

        if not data:
            print("Student not found")
            return

        print("Enter new details:")

        self.s1m = self.checknum(self, mark_type = "Theroy marks of hindi")
        self.s2m = self.checknum(self, mark_type = "Thoery marks of English")
        self.s3m = self.checknum(self, mark_type = "Thoery marks of Physics")
        self.s4m = self.checknum(self, mark_type = "Thoery marks of Chemistry")
        self.s5m = self.checknum(self, mark_type = "Thoery marks of Maths")


        self.p1m =  self.checknum1(self,pmark_type = "Practical marks of hindi")

        self.p2m = self.checknum1(self, pmark_type = "Practical marks of English")
        self.p3m = self.checknum1(self, pmark_type = "Practical marks of Physics")
        self.p4m = self.checknum1(self, pmark_type = "Practical Marks of Chemistry")
        self.p5m = self.checknum1(self, pmark_type = "Practical Marks of Maths")


        self.hindi = self.s1m + self.p1m
        self.eng = self.s2m + self.p2m
        self.phy = self.s3m + self.p3m
        self.chem = self.s4m + self.p4m
        self.math = self.s5m + self.p5m

        self.total= (self.hindi + self.eng + self.phy + self.chem + self.math)

        cur.execute(
            """
            Update students SET
            
            hindi_theory=%s,english_theory=%s,physics_theory=%s,chemistry_theory=%s,maths_theory=%s,
            hindi_practical=%s,english_practical=%s,physics_practical=%s,chemistry_practical=%s,maths_practical=%s,
            hindi_total=%s,english_total=%s,physics_total=%s,chemistry_total=%s,maths_total=%s,grand_total=%s
            
            Where roll_no=%s
            """,
            (self.s1m,self.s2m,self.s3m,self.s4m,self.s5m,
             self.p1m,self.p2m,self.p3m,self.p4m,self.p5m,self.hindi,self.eng,self.phy,self.chem,
             self.math,self.total,

             roll_no)
            )
        con.commit()
        print("Student Updated") 

        cur.execute("SELECT * From students where roll_no=%s",(roll_no,))

        data = cur.fetchone()

        if not data:
            print("Student not found")
            return

        self.rno = data[0]
        self.name = data[1]
        self.mname = data[2]
        self.fname = data[3]
        self.stream = data[4]
        self.school_n = data[5]
        self.ms_no = data[6]
        self.cno= data[7]
        self.reg = data[8]
        self.s1m = data[9]
        self.s2m = data[10]
        self.s3m = data[11]
        self.s4m = data[12]
        self.s5m = data[13]
        self.p1m = data[14]
        self.p2m = data[15]
        self.p3m = data[16]
        self.p4m = data[17]
        self.p5m = data[18]
        self.hindi = data[19]
        self.eng = data[20]
        self.phy = data[21]
        self.chem = data[22]
        self.math = data[23]
        self.total = data[24]

        self.displayAll()  

    def delete(self):
        roll_no = input("Enter the roll number which you want to delete: ")

        cur.execute("SELECT * From students where roll_no=%s",(roll_no,)) 

        data = cur.fetchone()

        if not data:
            print("Student no found")

        cur.execute("DELETE From students where roll_no=%s",(roll_no,))

        con.commit()
        print("Student data deleted")

    def checkresult(self):

        count = 0

        if self.s1m < 27:
            count+=1
        if self.s2m < 27:
            count +=1
        if self.s3m < 27:
            count +=1 
        if self.s4m < 27:
            count +=1
        if self.s5m < 27:
            count +=1 

        if count == 0:
            return "PASS"
        elif count <= 3:
            return f"Supply({count})"
        else:
            return "FAIL"    
   



    def __init__(self):

        pass

    def take_input(self,update=False):

        
        self.name = self.checkname(input("Enter name: "), name_type = "name")

        self.mname = self.checkname(input("Enter Mother name: "), name_type = "Mother Name")
        self.fname = self.checkname(input("Enter father name: "), name_type = "Father Name")
        self.stream = self.checkname(input("Enter Stream: "),name_type = "Stream")
        self.school_n = input("Enter School name: ")
        self.ms_no = random.randrange(1000000,9999999)
        
        self.rno = self.get_roll()
        
        self.cno = random.randrange(10000,99999)
        self.reg = random.randrange(1000000,9999999)
        #self.dob = date(input("Enter Your DOB:"))
        

        self.s1m = self.checknum(self, mark_type = "Theroy marks of hindi")
        self.s2m = self.checknum(self, mark_type = "Thoery marks of English")
        self.s3m = self.checknum(self, mark_type = "Thoery marks of Physics")
        self.s4m = self.checknum(self, mark_type = "Thoery marks of Chemistry")
        self.s5m = self.checknum(self, mark_type = "Thoery marks of Maths")


        self.p1m =  self.checknum1(self,pmark_type = "Practical marks of hindi")

        self.p2m = self.checknum1(self, pmark_type = "Practical marks of English")
        self.p3m = self.checknum1(self, pmark_type = "Practical marks of Physics")
        self.p4m = self.checknum1(self, pmark_type = "Practical Marks of Chemistry")
        self.p5m = self.checknum1(self, pmark_type = "Practical Marks of Maths")


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


        text= f"Registration no.:{self.reg}"+" "*29+f"Stream:{self.stream}"
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

        print('|'+f"Total Agregate: {self.total}"+" "*85+'|')

        
        
        result = self.checkresult()
        text = f"Result:{result}"
        print('|'+text+(" "*(104-len(text)))+'|') 



        if(self.total>299):
             print('|'+"Division: 1st"+" "*91+'|')

        elif(self.total<300 and self.total>249):
             print('|'+"Division: 2nd"+" "*91+'|')

        elif(self.total<250 and self.total>164):
            print('|'+"Division: 3rd"+" "*91+'|')

        else:
            print('|'+"Division: 4th"+" "*91+'|')        
        
        print('|'+"="*104+'|')


#inp = inputAll()

#inp.insert_all()
#inp.get_student()
#inp.displayAll()


	
