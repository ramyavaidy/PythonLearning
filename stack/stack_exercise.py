
stackstr = "We will conquer covid-19"

def reverse_string(stackstr):
    stack = []
    for char in stackstr:
        stack.append(char)

    reversed_str = ""
    while len(stack) > 0:
        reversed_str += stack.pop()

    return reversed_str

def is_balanced_parentheses(s):
    stack = []
    parentheses_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in parentheses_map.values():
            stack.append(char)
        elif char in parentheses_map.keys():
            if not stack or stack[-1] != parentheses_map[char]:
                return False
            stack.pop()

    return len(stack) == 0

print(reverse_string(stackstr))
print(is_balanced_parentheses("({a+b})"))  # True
print(is_balanced_parentheses("))((a+b}{}"))  # False
print(is_balanced_parentheses("[a+b]*(x+2y)*{gg*2k}"))  # True