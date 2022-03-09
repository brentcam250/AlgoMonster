from typing import List

def partition(s: str) -> List[List[str]]:
    output = []
    n = len(s)
    def is_palindrome(word):
        return word == word[::-1]
    def dfs(start, cur_path):
        if start == n:
            output.append(cur_path[:])
            return
        for i in range(start + 1, n +1):
            prefix = s[start: i]
            if is_palindrome(prefix):
                dfs(i, cur_path + [prefix])

        dfs(0,[])
    # WRITE YOUR BRILLIANT CODE HERE
    return output

if __name__ == '__main__':
    s = input()
    res = partition(s)
    for row in res:
        print(' '.join(row))