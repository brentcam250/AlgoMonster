from typing import List

KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

def letter_combinations_of_phone_number(digits: str) -> List[str]:
    def dfs(path, res):
        if len(path) == len(digits):
            res.append(''.join(path))
            return
        next_number = digits[len(path)]
        for letter in KEYBOARD[next_number]:
            path.append(letter)
            dfs(path, res)
            path.pop()
    res = [] 
    dfs([], res)
    return res

if __name__ == '__main__':
    digits = input()
    res = letter_combinations_of_phone_number(digits)
    print(' '.join(res))

    #     for i, letter in enumerate(letters):
    #         if(used[i]):
    #             continue
    #         path.append(letter)
    #         used[i] = True
    #         dfs(path, used, res)
    #         path.pop()
    #         used[i] = False 
    # res = []
    # dfs([], [False] * len(letters), res)


# function dfs(node, state):
#     if state is a solution:
#         report(state) # e.g. add state to final result list
#         return

#     for child in children:
#         if child is a part of a potential solution:
#             state.add(child) # make move
#             dfs(child, state)
#             state.remove(child) # backtrack

# Identify the state(s).
# Draw the state-space tree.
# DFS/backtrack on the state-space tree.