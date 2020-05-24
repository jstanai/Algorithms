def partition(arr, low, high):

    # starts at right-most element
    pivot = arr[high]

    i = low - 1 # swapping starting position

    for j in range(low, high):

        # on correct side, so increment i
        if (arr[j] <= pivot):
            i += 1
            
            # swap the elements
            arr[j], arr[i] = arr[i], arr[j]

            print(
                'i: {}, j: {}, arr[i]: {}, arr[j]: {}'.format(
                    i, j, arr[i], arr[j]
                )
            )

            print('arr: {}'.format(arr))

    # finally, put pivot where it belongs
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(arr)
    return(i + 1)


# example  
arr = [10, 80, 30, 90, 40, 50, 70]
low = 0
high = len(arr) - 1
result = partition(arr, low, high)

print(result)