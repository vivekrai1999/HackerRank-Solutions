# solution notes pending
if __name__ == '__main__':
    my_list = []
    N = int(input())
    for _ in range(N):
        string = input().split()
        command = string[0]
        argument = string[1:]
        if command != "print":
            command += "("+ ",".join(argument) +")"
            eval("my_list."+command)
        else:
            print(my_list)
        
