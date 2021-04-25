student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}


for key in student_scores:
	grades = student_scores[key]
	if grades >= 91 and grades <=100:
		student_grades [key] = "Outstanding"
	elif grades >=81 and grades <=90:
		student_grades[key]= "Exceeds Expectations"
	elif grades >=71 and grades <=80:
		student_grades[key] = "Acceptable"
	elif grades<=70:
		student_grades[key]= "Fail"	
    

print(student_grades)





