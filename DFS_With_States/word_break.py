from typing import List

def word_break(s: str, words: List[str]) -> bool:
    def dfs(i):
        if i == len(s):
            return True 

        for word in words: 
            if s[i:].startswith(word):
                if dfs(i + len(word)):
                    return True 
        return False
    return dfs(0)

if __name__ == '__main__':
    s = input()
    words = input().split()
    res = word_break(s, words)
    print('true' if res else 'false')