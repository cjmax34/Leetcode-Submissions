def letterCombinations(digits):
    res = []
    keyboard = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def backtrack(i, curr):
        if len(curr) == len(digits):
            res.append(curr)
            return

        for c in keyboard[digits[i]]:
            backtrack(i+1, curr+c)

    backtrack(0, "")

    return res