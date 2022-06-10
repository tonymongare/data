# optimized bubble sort
def BubbleSort(array):
    array_length = len(array)

    for i in range(array_length):
        swapped = False

        for j in range(0, array_length - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

        if not swapped:
            break

