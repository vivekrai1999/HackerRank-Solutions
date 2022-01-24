# solution notes
if __name__ == '__main__':
    s_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        s_list.append([name, score])
    sor_list = sorted(s_list, key = lambda x:x[1])
    first_minimum = min(x[1] for x in sor_list)
    toDelete = [x for x in sor_list if x[1] == first_minimum]
    for i in range(0, len(toDelete)):
        sor_list.pop(0)
    minimum = min(x[1] for x in sor_list)
    final = [x[0] for x in sor_list if x[1] == minimum]
    name_sorted = sorted(final)
    for i in name_sorted:
        print(i)
