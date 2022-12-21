# Print 9x9 multiply table

if __name__ == "__main__":
    for i in range(1, 10):
        result = ""
        for j in range(1, 10):
            if j < i:
                result += "\t"
            else:
                result += f"{i}x{j}={i*j}\t"
        print(result)
        