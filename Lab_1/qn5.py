"""
A school decided to replace the desks in three classrooms. Each desk sits two students.
Given the number of students in each class, print the smallest possible number of desks
that can be purchased.
The program should read three integers: the number of students in each of the three
classes, a, b and c respectively.
In the first test there are three group. The first group has 20 students and thus needs 10
desks. The second group has 21 students, so they can get by with no fewer than 11 desks.
11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.
"""
students_a=int(input("Enter the number of student in class a:"))
students_b=int(input("Enter the number of student in class b:"))
students_c=int(input("Enter the number of student in class c:"))
if (students_b+students_c+students_a)%2!=0:
    bencha=(students_a+students_b+students_c)//2+1
    print(f"the bench{bencha}")
else:
    benchb=(students_a+students_b+students_c)//2
    print(f"the bench required is {benchb}")
