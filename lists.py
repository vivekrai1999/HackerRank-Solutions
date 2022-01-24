# solution notes 
# task: perform certain operations on list based on inputs like insert, pop, print etc.

if __name__ == '__main__':
    my_list = [] # list on which the operations to be performed
    N = int(input()) # number of operations to be performed
    for _ in range(N): # running loop n times to get n inputs
        string = input().split() # hetting input and splitting it into parts(eg. input = insert 0 5 so we split it as ['insert','0','5'])
        command = string[0] # our command is the 0 index element of the list so we save it in a varibale
        argument = string[1:] # all the elements from index 1 to last index are our argument so we save it in a varibale with help of slicing
        if command != "print": # print command is used in a different way than the regular commands in a list so when the command is not equal to print we do certain operation
            command += "("+ ",".join(argument) +")" # concatinate command + "(" + ",".join(argument) + ")" => command(argument1, argument2)
            eval("my_list."+command) # now use eval function to evaluate the string => "my_list."+command => "my_list."+"command(argument1, argument2)" => evaluated as my_list.command(argument1, argument2)
        else: # and if the command is equal to print then print the list simply
            print(my_list)
        
