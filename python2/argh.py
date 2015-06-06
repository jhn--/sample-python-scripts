count = 0
for i in l:
    m=open(os.getcwd()+'/folder1/'+i, 'r')
    print m
    n = m.read()
    print n
    if re.search('200', n):
        count = count + 1
print count
