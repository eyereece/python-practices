if __name__ == '__main__':
    # store student's information in a list
    student = []
    test = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
        test.append(score)
        
    # Remove duplicates and sort scores in increasing order
    test = sorted(list(set(test)))

    # i = second lowest grade; store all the satisfied names in list_name
    i = test[1]
    list_name = []
    for a in student:
        if a[1] == i:
            list_name.append(a[0])
    
    # Order their names alphabetically
    list_name.sort()
    for name in list_name:
        print(name)
