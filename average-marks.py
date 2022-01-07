# solution notes:
# name, *line means that the first element of the list obtained by input().split() will be assigned to name and rest of the items will be assigned to the line(list of rest items)
# interger marks further converted into list of float using map and list method
# approch: iterate through all the keys in dictionary
#          check if the key name matches the query name
#          if matches then access the value by using key
# float precision use: "{:.2f}".format(data_to_be_formatted)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores # creating dictionary
    query_name = input()
    
    for key in student_marks:
        if key == query_name:
            print("{:.2f}".format(sum(student_marks[key])/3))
