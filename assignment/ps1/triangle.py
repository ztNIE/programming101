length = int(input("Please input length: "))
for i in range(1, length + 1):
    # print("* "*i)
    result = ""
    for j in range(i):
        result += "* "
    print(result)