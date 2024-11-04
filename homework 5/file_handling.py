# exercise 1
print("ex 1")
def file_read(filename):
    txt=open(filename)
    print(txt.read())
file_read("bnb.txt")

# exercise 2
print("ex 2")
def first_line(filename):
    txt=open(filename)
    print(txt.readline())
first_line("bnb.txt")

# exercise 3
print("ex 3")
def file_append(filename):
    from itertools import islice 
    with open(filename,'w') as file:
        file.write('python exercise/n')
        file.write('java exercies')
    txt=open(filename)
    print(txt.read())
file_append('test.txt')

# exercise 4
print('ex 4')
import sys
import os
def file_lastline(filename,lines):
    bufsize=8192
    fsize=os.stat(filename).st_size
    iter=0
    with open(filename) as f:
        if bufsize>fsize:
            bufsize=fsize-1
            data=[]
            while True:
                iter +=1
                f.seek(fsize-bufsize*iter)
                data.extend(f.readlines())
                if len(data)>= lines or f.tell()==0:
                    print(''.join(data[-lines:]))
                    break

file_lastline('bnb.txt',2)

# exercise 5
print("ex 5")
def file_read(filename):
    with open(filename) as f:
        content_list=f.readlines()
        print(content_list)

file_read('bnb.txt')

# exercise 6
print('ex 6')
def file_lines(filename):
    with open(filename,'r') as myfile:
        data=myfile.readlines()
        print(data)
file_lines('bnb.txt')

# exercise 7
print('ex 7')
def file_read(filename):
    content_array=[]
    with open(filename,'r') as m:
        for line in m:
            content_array.append(line)
            print(content_array)
file_read('bnb.txt')

# exercise 8
print('ex 8')
def longest_word(filename):
    with open(filename,'r') as infile:
        words=infile.read().split()
        max_len=(len(max(words,key=len)))
        return [word for word in words if len(word)==max_len]
print(longest_word('bnb.txt'))

# exercise 9
print('ex 9')
def file_length(filename):
    with open(filename) as m:
        for i,l in enumerate(m):
            pass
        return i+1
print('Number of lines in the file:',file_length('bnb.txt'))

# exercise 10
print('ex 10')
from collections import Counter
def word_count(filename):
    with open(filename) as m:
        return Counter(m.read().split())
print('Number of words in the file:',word_count('bnb.txt'))

# exercise 11
print('ex 11')
def file_size(filename):
    import os
    statinfo=os.stat(filename)
    return statinfo.st_size
print('File size in bytes of plain file:',file_size('bnb.txt'))

# exercise 12
print('ex 12')
color=['Red','Green','White','Black','Yellow','Brown']
with open('bnb.txt','w') as m:
    for c in color:
        m.write("%s\n"%c)
    
content=open('bnb.txt')
print(content.read())
