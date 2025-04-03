class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
def is_symmetric(string: str) -> bool:
    brackets = {'}': '{', ']': '[', ')': '('}
    stack = Stack()
    for char in string:
        if char in brackets.values():
            stack.push(char)
        elif char in brackets.keys():
            if stack.peek() == brackets[char]:
                stack.pop()
            else:
                return False
    return stack.size() == 0


print(is_symmetric("( ){[ 1 ]( 1 + 3 )( ){ }}"))
print(is_symmetric("( 23 ( 2 - 3);"))
print(is_symmetric("( 11 }"))


