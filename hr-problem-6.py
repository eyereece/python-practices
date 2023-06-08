if __name__ == '__main__':
    arr = []
    N = int(input())
    while N > 0:
        command = input()
        current_command = command.split(" ")

        for i in range(len(current_command)):
            if i == 0:
                continue
            current_command[i] = int(current_command[i])

        if current_command[0] == "insert":
            arr.insert(current_command[1], current_command[2])
        elif current_command[0] == "print":
            print(arr)
        elif current_command[0] == "remove":
            arr.remove(current_command[1])
        elif current_command[0] == "append":
            arr.append(current_command[1])
        elif current_command[0] == "sort":
            arr.sort()
        elif current_command[0] == "pop":
            arr.pop()
        elif current_command[0] == "reverse":
            arr.reverse()
        N -= 1