from copy import deepcopy

a = 5

m = 10

list1 = [1,2,3,4,5]

def add_and_print(a):
    a += 1
    print(f"Now a={a}")

def print_list(l):
    l = deepcopy(l)
    while len(l) != 0:
        print(l.pop())

print(f"Before: {list1}")
print_list(list1)
print(f"After: {list1}")

print(f"Before: {a}")
add_and_print(a)
print(f"After: {a}")