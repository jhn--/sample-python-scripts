from html.parser import HTMLParser

file = '/Users/john/Dropbox/bookmarks_12_26_14.html'
f = open(file, 'r', encoding='utf-8')
abc = f.read()
f.close()

class myHTMLParser(HTMLParser):
#    def handle_starttag(self, tag, attrs):
#        print("Encountered a start tag :", tag)
#    def handle_endtag(self, tag):
#        print("Encountered an end tag :", tag)
#    def handle_data(self, data):
#        print("Encountered some data :", data)
    def handle_starttag(self, tag, attrs):
        print("self is {0}".format(self))
        print("tag is {0}".format(tag))
        print("attrs is {0}".format(attrs))
        if tag == 'a':
            for name, value in attrs:
                if name == "href":
                    print(name, "=", value)

parser = myHTMLParser()
#parser.feed('<html><head><title>test</title></head>'
#            '<body><h1>Parse me!</h1></body></html>')
parser.feed(abc)
'''
expect:
self is <__main__.myHTMLParser object at 0x10cc798d0>
tag is a
attrs is [('href', 'http://htmlgear.lycos.com/specs/event.html'), ('add_date', '1409876904')]
href = http://htmlgear.lycos.com/specs/event.html
'''

#handle_starttag('a', [('href', 'http://www.cwi.nl/')])