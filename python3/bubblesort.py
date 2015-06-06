def bubblesort(input):
    count = 1
    while count > 0:
        count = 0
        for i in range(len(input)-1):
            temp = input[i]
            if temp < input[i+1]:
                pass
            else:
                input[i], input[i+1] = input[i+1], temp
                count += 1
    return input

print(bubblesort([4,5,3,2,1]))

print(bubblesort([1]))

print(bubblesort(["a","z","T","^","{}"]))