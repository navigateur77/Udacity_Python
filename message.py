# get and process input for a list of names
names =  input('Enter names separated by commas: ')
names = list(names.split(','))

print(names)

# get and process input for a list of the number of assignments

assignments =  input('Enter assignments counts separatedby commas: ')
assignments = list(assignments.split(','))
print(assignments)

# get and process input for a list of grades

grades =  input('Enter grades separated by commas: ')
grades = list(grades.split(','))
print(grades)

# message string to be used for each student
# HINT: use .format() with this string in your for loop

for n, a, g in zip(names, assignments, grades):
	message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
	submit before you can graduate. You're current grade is {} and can increase \
	to {} if you submit all assignments before the due date.\n\n".format(n, int(a), int(g), (2*int(a) + int(g)))
 
	print(message)