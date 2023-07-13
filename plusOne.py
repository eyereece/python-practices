def plusOne(digits):
    strings = ""
    for n in digits:
        strings += str(n)
    temp = str(int(strings) + 1)
        
    return [int(temp[i]) for i in range(len(temp))]


digits = [1,2,3]
print(plusOne(digits))