def binary_search(L, x):
    L = sorted(L)                    # first, sort the list in assending order
    left, right = 0, len(L)-1

    while left <= right:
        mid = (left + right) // 2   # integer division

        if L[mid] == x:
            return mid
        
        if L[mid] < x: 
            left = mid + 1
        else:
            right = mid - 1
    
    return -1                       # if not found then return -1


if __name__ == "__main__":
    l = [1, 2, 3, 55, 33, 88, 23, 45]
    if binary_search(l, 88) == -1:
        print('The number is not found in the list.')
    else:
        print('The value is found at correct position')





