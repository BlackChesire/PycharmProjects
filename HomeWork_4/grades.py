"""
Student: Asaf Yosef Ben Shabat
ID: 312391774
Assignment no. 4
Program: grades.py
"""
f = open('students.txt', 'r')
students_file = [x.split() for x in f.read().splitlines()]
f.close()
names_dict = {int(x[0]): ' '.join(x[1:]) for x in students_file}
m = open('grades.txt', 'r')
grades_file = [x.split() for x in m.read().splitlines()]
m.close()
grades_dict = {int(x[0]): [int(y) for y in x[1:]] for x in grades_file} # converting the keys/values to int in the dict
max_score = 0
for i in grades_dict.values():
    avg = (sum(i) / len(i)) # calcs the avg of each students
    if avg > max_score:
        max_score = avg  # saving the highest average
        best_student = i  # in order to find the key by the value
x = [k for k, v in grades_dict.items() if v == best_student]  # saving the key by value
grades = {x: 0 for x in range(0, 101)}  # creating a grades dict
for i in grades_dict.values():  # adding 1 for the grades value for every apperance , in order to find the most common
    for j in i:
        grades[j] += 1
maximum = max(grades, key=grades.get)  # finding the most common grade by the highest value
max_index = grades[maximum]
print("the student with the highest average is :", names_dict[x[0]], "with the average of ", avg)
list_of_most_common_grades = [i for i in grades if grades[i] == max_index]  # finding the most common grades
print("the most common scores among the students is :", list_of_most_common_grades)
list_of_less_common_grades = [i for i in grades if grades[i] == 0]  # finding the less common grades
print("there is no students with the following grades:", list_of_less_common_grades)