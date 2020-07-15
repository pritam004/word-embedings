import re
def read_corpus(x):
    file=open('data/'+x,'r')
    Lines=file.readlines()
    data=[]
    for l in Lines:
        data.append(re.split(' |\n',l))
    return data