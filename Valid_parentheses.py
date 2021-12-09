from collections import deque
def valid_parentheses(s: str) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    stack = []
    pairs = { ')': '(', '}': '{', '[' : ']'}
    for char in s:
      if char in pairs: 
        if (len(stack) > 0) and (stack[-1] == pairs[char]):
          stack.pop()
        else:
          return False
      else: 
        stack.append(char)
    return False if (len(stack) > 0) else True

if __name__ == '__main__':
    s = input()
    res = valid_parentheses(s)
    print('true' if res else 'false')
