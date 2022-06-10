def selectionsort(array, length):
    for element in range(length):
        minimum_element = element
        for j in range(element + 1, length):
            if array[j] < array[minimum_element]:
                temp = array[minimum_element]
                array[minimum_element] = array[j]
                array[j] = temp


array = [-2, -7, 3, 1, 9, 3, 4, 1]
length = len(array)
selectionsort(array, length)
print(array)

