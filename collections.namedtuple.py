# solution notes
# namedtuple is a class present in the collections module which have enhanced capability of accessing elements by both names and integer indices.
# note: columan data can be given in any sequence and the data will also be given in the same sequence as the column
from collections import namedtuple
n = int(input()) # number of students
col_name = input().split() # columns name in any order
total = 0
for _ in range(n): # running loop n time to get data of n students
    students = namedtuple('students',col_name) # creating a namedtuple with the column names
    f1,f2,f3,f4 = input().split() # get the student data and save it into four fields
    s = students(f1,f2,f3,f4) # for each column put value to it(assuming the sequence of column and the sequence of data matches)
    total += int(s.MARKS) # accessing marks from the namedtuple by name and adding it to the varible total so ge finally get sum of all the students marks
print(int(total)/n) # calculating average of students marks by dividing total marks with the number of students
