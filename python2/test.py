#!/opt/local/bin/python2.6

state='singapore'
print('it never snows in sunny %s.' % state)

infile=file('tmp.txt','r')
content=infile.read()
print content
infile.close()

afile=file('tmp.txt','r')
for line in afile:
    print 'Line:', line
infile.close()

s1='abcd'
for a in s1:
    print a