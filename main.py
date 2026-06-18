from marksheet import inputAll

while True:

	print("To add student press 1")
	print("To check the data of student with roll number press 2")
	print("To update the data of student with roll number press 3")
	print("To delete the data of student with roll number press 4")
	print("To Exit press 5")
	check = input("Enter your choice:")
	if check == "1":
		inp=inputAll()
		inp.take_input()
		inp.insert_all()
		inp.displayAll()
		break
	elif check == "2":
		inp=inputAll()
		inp.get_student()
		break
	elif check == "3":
		inp=inputAll()
		inp.update()
		break
	elif check == "4":
		inp = inputAll()
		inp.delete()
		break
	elif check == "5":
		print("Thank You")
		break
	else:
		print("Invalid Choice")



