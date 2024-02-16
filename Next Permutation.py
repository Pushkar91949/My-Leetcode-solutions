def nextPermutation(arr):
    n = len(arr)

    index = -1

    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            index = i
            break

    if index == -1:
        arr.reverse()
        return arr

    else:
        for i in range(n-1, index, -1):
            if arr[i] > arr[index]:
                arr[i], arr[index] = arr[index], arr[i]
                break
        arr[index+1:] = arr[index+1:][::-1]
        return arr


array = [3, 2, 1]

print(nextPermutation(array))
