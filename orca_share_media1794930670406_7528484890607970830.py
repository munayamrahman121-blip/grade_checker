'''
grade checker application.
requirements:
	- ask the student for his name.
	- ask the user for his/er grade
	- Truthy / Falsy: use this and validate the inputted grade
	- we use conditions: if/elif/else with complicated nested conditions
	- assign a grade
	- print the name along with the grade
	- did you pass or fail?
	- if failed give warning -- Dhomok!
	- A or A+ --> congratulations! 
'''

name = input("Enter your name please: ")
mark_input = input(f"Enter your mark {name}: ")

# mark = "40"

# if mark_input == "":
# 	print("You should enter a valid mark")

# using a not operation <--- much better
# validation
# if not mark_input or int(mark_input) < 0:
# 	if not mark_input:
# 		print("You should enter a valid mark! Please.")

# 	if int(mark_input) < 0:
# 		print("Mark cant be less than 0")
# and, or, not

'''
Check your edge cases:
 - non-numric
 - wrong age / invalid

This is project
We need to check age
Infant, toddler, child, teenager, adult, senior
age >= 16: drive
A lot of conditions you want to implement
'''

# greedy/brute force approach: the happy path

if not mark_input:
	print("You should enter a valid mark! Please.")
else:
	print("valid mark entered: ", mark_input)
	mark = int(mark_input)

	if mark < 0 or mark > 100:
		print("Mark cant be less than 0 or greater than 100")
	else:
		if mark >= 90:
			grade = "A+"
		elif mark >= 80:
			grade = "A"
		elif mark >= 70:
			grade = "A-"
		elif mark >= 60:
			grade = "B"
		elif mark >= 50:
			grade = "C"
		elif mark >= 40:
			grade = "D"
		elif mark >= 33:
			grade = "D-"
		else:
			grade = "F"

		print(f"{name}, your grade is {grade}")

		if mark >= 33: # condition for pass: mininum mark is 33
			print("Your status: PASS")
			if grade == "A+" or grade == "A":
				print(f"Congratulations {name}, BRILLIANT BRAVO!")
		else:
			print("Your status: FAIL")
			print(f"Come with your guardian tomorrow, {name}")

		




