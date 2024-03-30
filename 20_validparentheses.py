def validParentheses(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}

    if len(s) % 2 == 1:
        return False    # not balanced

    for c in s:
        if c in ('(', '[', '{'):
            stack.append(c)
        elif len(stack) == 0 or pairs[stack.pop()] != c:
            return False

    return len(stack) == 0

print(validParentheses("((()))"))