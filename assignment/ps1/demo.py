length = int(input("Please input length: "))

# for-loop
for i in range(length):
    # print((i + 1) * "* ")
    result = "\t" * (length - (i+1))
    for j in range(i + 1):
        result += f"{j+1}x{i+1}={((i+1) * (j+1))}\t"
    print(result)

# write in while-loop
i = 0
while i < length:

    result = "\t" * (length - (i+1))
    j = 0
    while j < i + 1:
        result += f"{j+1}x{i+1}={((i+1) * (j+1))}\t"
        j += 1

    i += 1
    print(result)