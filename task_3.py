
def is_symmetric(string: str) -> bool:
    brackets = {'}': '{', ']': '[', ')': '('}
    stack = []
    for char in string:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


print(is_symmetric("( ){[ 1 ]( 1 + 3 )( ){ }}"))
print(is_symmetric("( 23 ( 2 - 3);"))
print(is_symmetric("( 11 }"))

