
'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''

d = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


def letterCombination(num: str):

    if num == '':
        return []

    if len(num) == 1:
        return d[num]

    return [letter + item for letter in d[num[0]] for item in letterCombination(num[1:])]


print(letterCombination('423'))
