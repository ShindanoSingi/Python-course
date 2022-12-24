#
# Example file for parsing and processing HTML

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encountered a comment:", data)
        pos = self.getpos()
        print("At line:", pos[0]," position", pos[1])

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        pos = self.getpos()
        print("At line:", pos[0]," position", pos[1])

    def handle_data(self, data):
        if data.isspace:
            return
        print("Encountered text data:", data)
        pos = self.getpos()
        print("At line:", pos[0]," position", pos[1])

def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()

    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read() # read the entire file
        parser.feed(contents)

if __name__ == "__main__":
    main()
