from collections import deque

def is_palindrom(string: str) -> bool:
    queue = deque(string.lower().replace(' ', ''))
    while len(queue) > 1:
        if  queue.popleft() != queue.pop():
            return False
    return True


print(is_palindrom("A man, a plan, a canal: Panama"))
print(is_palindrom("race a car"))
print(is_palindrom("0P0"))