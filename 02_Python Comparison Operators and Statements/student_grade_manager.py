student = {"Erfan":19,"Ali":16,"Maryam":20,"Sara":18,"Reza":17}


print("================================")
print("Student Grade Management System")
print("================================")

running = True

while running:
	print()
	print("1.  Show Students")
	print("2.  Show Average Grade")
	print("3.  Show Highest Grade")
	print("4.  Show Lowest Grade")
	print("5.  Add Student")
	print("6.  Remove Student")
	print("7.  Search Student")
	print("8.  Update Student Grade")
	print("9.  Show Students Above Average")
	print("10. Show Grade Statistics")
	print("11. Exit")
	print()
	entry= int(input("Select an Option"))

	if entry > 11 or entry == 0:
		print("Out Of Range! Please Choose Available Option")


	else:
		if entry == 1:
			for name in student:
				print(name,":", student[name])

		elif entry == 2:
			counter = 0
			total = 0
			for name in student:
				total += student[name]
				counter += 1
			average = total / counter
			print ("The Average Grade is: ", average)

		elif entry == 3:
			highest_grade = 0
			for name in student :
				if student[name] > highest_grade:
					highest_grade = student[name]
			print("The Maximum Grade is: ",highest_grade)


		elif entry == 4:
			lowest_grade = 100
			for name in student:
				if student[name] < lowest_grade:
					lowest_grade = student[name]
			print("The Minimum Grade is: ", lowest_grade)

		elif entry == 5:
			student_name = input("Enter Student Name: ")
			student_grade = float(input("Enter Student Grade: "))
			student[student_name] = student_grade
			print("New Student Added Successfully")

		elif entry == 6:
			student_name = input("Enter Student Name: ")
			if student_name in student:
				del student[student_name]
				print(student_name,":","Student Removed Successfully")
			else:
				print("Student Not Found!")

		elif entry == 7:
			student_name = input("Search an Student \nEnter Student Name: ")
			if student_name in student:
				print(student_name,":",student[student_name])
			else:
				print("Student Not Found!")

		elif entry == 8:
			student_name = input("Update Student Grade \nEnter Student Name: ")
			if student_name in student:
				new_grade = float(input("Enter New Grade: "))
				student[student_name] = new_grade
				print("New Grade Set!")
				print(student_name,":",student[student_name])
			else:
				print("Student Not Found!")

		elif entry == 9:
			counter = 0
			total = 0
			for name in student:
				total += student[name]
				counter += 1
			average = total / counter
			for name in student:
				if student[name]> average:
					print("Students with grades above average: ",name,":",student[name])

		elif entry == 10:
			print("=================")
			print("Statistic Report")
			print("=================")
			print()
			counter = 0
			total = 0
			for name in student:
				total += student[name]
				counter += 1
			average = total / counter
			print("Total Students: ",counter)
			print("Average Grade: ",average)

			highest_grade = 0
			for name in student :
				if student[name] > highest_grade:
					highest_grade = student[name]
			print("The Maximum Grade is: ",highest_grade)

			lowest_grade = 100
			for name in student:
				if student[name] < lowest_grade:
					lowest_grade = student[name]
			print("The Minimum Grade is: ", lowest_grade)

		elif entry ==11:
			print("Good Bye!")
			running = False