class inputAll:
	def __init__(self,msnum,name,mname,fname,roll,cno,stream,school_n):
		self.msnum=int(input("Enter the Ms no.:"))
		self.name=input("Enter name:")
		self.mname=input("Enter Mother name:")
		self.fname=input("Enter father name:")
		self.roll=int(input("Enter roll no.:"))
		self.cno=int(input("Enter Center no.:"))
		self.stream=input("Enter Stream")
		self.school_n=input("Enter School name:")

	def displayAll(self,msnum,name,mname,fname,roll,cno,stream,school_n):
		print(displayAll())

inp=inputAll()
inp.displayAll()

