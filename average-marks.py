# solution notes:
# name, *line means that the first element of the list obtained by input().split() will be assigned to name and rest of the items will be assigned to the line(list of rest items)
# interger marks further converted into list of float using map and list method
# approch: directly access the value of the query name from dictionary
#          add all items of list using sum()
#          divide the sum with the number of items in the score list that is the length of the score list.
#          print the average with 2 decimal float precision.
# float precision use: "{:.2f}".format(data_to_be_formatted)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores # creating dictionary
    query_name = input()
    
    print("{:.2f}".format(sum(student_marks[query_name]/len(scores)))
