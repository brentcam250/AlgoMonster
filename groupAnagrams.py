from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    # WRITE YOUR BRILLIANT CODE HERE
    hash = {}
    # position = 0
    for word in strs:
      alphabatized = (''.join(sorted(word)))
      if alphabatized in hash:
        hash[alphabatized].append(word)
      else:
        hash[alphabatized] = [word]
        
      
    return list(hash.values())

if __name__ == '__main__':
    strs = input().split()
    res = group_anagrams(strs)
    for row in res:
        row.sort()
    res.sort(key=lambda row: row[0])
    for row in res:
        print(' '.join(row))