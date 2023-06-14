import os

current_path = os.path.abspath(__file__)

current_path = os.path.join(current_path, '..', '..')
# print(current_path)

def recursion(count):
    print(count)
    if count == 5:
        return
    recursion(count + 1)
    print(count)

recursion(0)
    
print(recursion(5))