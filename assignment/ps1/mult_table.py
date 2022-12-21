# Print 9x9 multiply table

if __name__ == "__main__":
    for i in range(1, 10):
        result = ""
        for j in range(i, 10):
            result += f"{i}x{j}={i*j}\t"
        print(result)
        