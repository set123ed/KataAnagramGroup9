import time
from typing import Dict

def read_file(path): 
    with open(path) as f:
       for l in f:
            check(l.rstrip("\n"))

def sanitize(word):
  return str(sorted(word))

dic: Dict = {}

def check(word):
    key = sanitize(word)
    match = key in dic
    if match:
        dic[key].append(word)
    else: 
        dic.setdefault(key, [])
        dic[key].append(word)
    return match
    
def count():
    count = 0     
    for key, value in dic.items():
        if  len(value) > 1:    
            count += 1
    return count

if __name__ == '__main__':
    start_time = time.time()
    read_file("wordlist.txt")
    
    resul = ""

    for key, value in dic.items():
        if  len(value) > 1:    
            resul += str(value) + '\n'

    print(resul)
    end_time = time.time()
    print(end_time-start_time)