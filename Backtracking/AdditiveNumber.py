def check(num1, num2, rest):
    if (len(num1) > 1 and num1[0] == "0") or (len(num2) > 1 and num2[0] == "0"):
        return False
    strSum = str(int(num1) + int(num2))

    if strSum == rest:
        return True
    elif rest.startswith(strSum):
        return check(num2, strSum, rest[len(strSum):])
    else:
        return False


def solve(number):
    length = len(number)

    for i in range(1, length//2+1):
        for j in range(1, (length-i)//2 + 1):
            firstNum, secondNum, rest = number[:i], number[i : i+j], number[i+j:]
            if check(firstNum, secondNum, rest):
                return True
                
    return False

#------------------------------------------------#

number = input()
if solve(number) == True:
    print("true")
else:
    print("false")