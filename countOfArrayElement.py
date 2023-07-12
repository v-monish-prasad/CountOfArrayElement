def countOfArrayElement(array):
    if not array:
        return 0

    length = len(array)
    maxElem = array[0]
    count = 1

    for i in range(1, length):
        if array[i] == maxElem:
            count += 1
        elif array[i] > maxElem:
            maxElem = array[i]
            count = 1

    return length - count


if __name__ == "__main__":
    array = list(map(int, input().split()))
    print(countOfArrayElement(array))