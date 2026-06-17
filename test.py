from marksheet import inputAll

while True:

	print("To add student press 1")
	print("To check the data of student with roll number press 2")
	check = input("enter your choice: ")
	if check == "1":
		inp=inputAll()
		inp.take_input()
		inp.insert_all()
		break
	elif check == "2":
		inp=inputAll()
		inp.get_student()
		break
	elif check == "3":
		print(" ")
		break



