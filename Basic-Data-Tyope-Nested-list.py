# solution notes pending
# task: 1. create a nested list which will contain child lists with student name and students score. ex. [[name, score],[name, score].....]
# 2. find the second lowest score and print the name of the student with second lowest score.
# 3. if there are multiple students with second lowest score then print their name in sorted order
# Solution logic:
# at first sort the list according to second element in the nested list.
# remove the minimum score student from the list and if more than one student have minimum marks check with the minimum value and remove that also
# now the second lowest score will become the minimum score
# now get the minimum score and check if other student also have the minimum score if yes then save them into a list
if __name__ == '__main__':
    s_list = []
    for _ in range(int(input())): # getting n inputs (score and name)
        name = input()
        score = float(input())
        s_list.append([name, score]) # append name and score to the s_list
    sor_list = sorted(s_list, key = lambda x:x[1]) # sort the nested list according to the second element in the nested list(lambda x:x[1] => second element in the nested list)
    first_minimum = min(x[1] for x in sor_list) # getting first minimum using min function and list comprehension (for every x in sor_list we will get value of x[1] and pass that container to min function)
    toDelete = [x for x in sor_list if x[1] == first_minimum] # checking if another students also have the value equal to first minimum using list comprehension( for every x in sor_list get x if value of x[1] is equal to first minimum value)
    for i in range(0, len(toDelete)): # suppose we have two students with minimum marks, we already have a sorted list so first two values are the first minimum values so we have to get rid of them.
        sor_list.pop(0) # use pop method to get rid of the first minimum items. when first element pops then the second element autometically gets the index value of first one so we use index 0 always.
    minimum = min(x[1] for x in sor_list) # now find the min from the list after all the pop operations
    final = [x[0] for x in sor_list if x[1] == minimum] # check if any other name has same value as minimum and if yes then get x[0] i.e. name of the student.
    name_sorted = sorted(final) # sort the final  list
    for i in name_sorted: # print the final list
        print(i)

# solution 2 - 21 feb 2022

if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
    l_sorted = sorted(l, key = lambda x: x[1])
    lowest = l_sorted[0][1]
    l_final = [i for i in l_sorted if i[1]!=lowest]
    sec_lowest = l_final[0][1]
    final = sorted([i[0] for i in l_final if i[1]==sec_lowest])
    for name in final:
        print(name)
