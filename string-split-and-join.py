# solution notes
# .split() => converts all the words of a string to different strings and put them into a list. e.g. "this is a code editor" => ["this", "is", "a", "code", "editor"]
# "seperator goes here".join(pass list here) => joins the list items into a string
def split_and_join(line):
    # write your code here
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
