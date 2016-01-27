__author__ = 'zhenghu'
from typings import type_check
# // How to implement OOP in Python?
graph = []

for x in graph:
    print(x)

z = 3

@type_check.type_checked
def getX() -> int:
    x = 0
    if z > 4:
        x = 1
    else:
        x = "haha"
    return x

# z = 5
print(getX() + 1)
print(getX() + 1)
