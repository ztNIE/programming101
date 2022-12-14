def basic_add(a, b):
    return a + b

def class_add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    num1 = 11
    num2 = 22
    str1 = "1111"
    str2 = "2222"
    print("basic_add num: {}".format(basic_add(num1, num2)))
    print("basic_add str: {}".format(basic_add(str1, str2)))
    print("class_add num: {}".format(class_add(num1, num2)))
    print("class_add str: {}".format(class_add(str1, str2)))