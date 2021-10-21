# get and process input for a list of names
names =  input('Enter names separated by commas: ').title().split(',')

# get and process input for a list of the number of assignments

assignments =  input('Enter assignments counts separatedby commas: ').split(',')

# get and process input for a list of grades

grades =  input('Enter grades separated by commas: ').split(',')

# message string to be used for each student
# HINT: use .format() with this string in your for loop

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"
for n, a, g in zip(names, assignments, grades):
	print(message.format(n, a, int(g), int(a * 2)))