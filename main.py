totalMarks = int(input("Enter the total marks"))
sub1 = float(input("Enter the marks of English: "))
sub2 = float(input("Enter the marks of Hindi: "))
sub3 = float(input("Enter the marks of Maths: "))
sub4 = float(input("Enter the marks of Science: "))
sub5 = float(input("Enter the marks of Social: "))
sub6 = float(input("Enter the marks of Telugu: "))
sub7 = float(input("Enter the marks of Computers: "))
marks = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7
percentage = marks / totalMarks  * 100
print("The percentage of your test is: ", percentage, "%")