from html.parser import HTMLParser

class myHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print(f'-> {attr[0]} > {attr[1]}')
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print(f'-> {attr[0]} > {attr[1]}')
        
parser = myHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
