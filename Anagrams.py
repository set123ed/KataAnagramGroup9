from typing import Dict

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