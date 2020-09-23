import numpy as np

grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])

print("SUM:",grades.sum())
print("MIN:",grades.min())
print("MAX:",grades.max())
print("MEAN:",grades.mean())
print("STANDARD DEV:",grades.std())
print("VARIANCE:",grades.var())


print("ASSIGNMENT AVERAGE:", grades.mean(axis=0)) # average grades of the exams
print("STUDENT AVERAGE:", grades.mean(axis=1)) # student's average for all exams


numbers = np.array([1,4,9,16,25,36])
print(np.sqrt(numbers)) # squareroot of numbers in array


print(grades[0,1]) # gives first student's second exam score (1st row, seocnd col)
print(grades[1]) # prints all of the exam scores for student 2
print(grades[0:2]) # gives all grades for first two students (upper limit not counted)
print()
print(grades[[1,3]]) # gives you all of the grades for student 2 and 4, DOUBLE BRACKETS gives a list of rows to pull
print()
print(grades[:,0]) # prints exam 1 scores for all students (the whole column)
print(grades[0:2,0]) # prints exam 1 scores only for students 1 and 2
print(grades[0,0:2]) # prints the first two exam scores for student 1
print()
print(grades[:,1:3]) #prints exam 2 and 3 scores for all students