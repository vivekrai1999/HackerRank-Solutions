import textwrap
def merge_the_tools(string, k):
    main_list = textwrap.wrap(string, k) #splits the string in k parts and returns a list
    for content in main_list: # run loop for each item in the main_list
        s = content # save the item of the main list to varibale s
        data = [s[0]] #first character of the string in data by default
        for item in s: # check if the item exist in the data list if yes then pass if no then append that item to the list
            if item in data:
                pass
            else:
                data.append(item)
        print(''.join(data))
