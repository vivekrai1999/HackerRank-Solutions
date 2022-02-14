# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for key, value in attrs:
            print(f'-> {key} > {value}')
        
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for key, value in attrs:
            print(f'-> {key} > {value}')
n = int(input())    
html = [input() for _ in range(n)]     
parser = MyHTMLParser()
parser.feed("".join(html))
