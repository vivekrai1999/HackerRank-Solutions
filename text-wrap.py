# solution notes
# textwrap => module in python, contains TextWrapper class(does most of the things)
# .width() => method in TextWrap class, The maximum length of wrapped lines
# .wrap() => Wraps the single paragraph in text (a string) so every line is at most width characters long
#            Returns a list of output lines
# "\n".join() => joines all items of list, takes a seprator
import textwrap

def wrap(string, max_width):
    final = textwrap.TextWrapper(width=max_width) # accessing TextWrapper class from textwrap module abd creating an object of TextWrap class
    # same as 
    # final = TextWrapper()
    # final.width(max_width)
    return "\n".join(final.wrap(text=string))
   
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
