def linear_search(L, x):
    n = len(L)
    i = 0

    while i < n:
        if L[i] == x:
            return i
        
        i += 1
    i = -1
    return i

if __name__ == "__main__":
    l = [1, 2, 3, 55, 33, 88, 23, 45]
    if linear_search(l, 88) == -1:
        print('The number is not found in the list.')
    else:
        print('The value is found at {}th position'.format(linear_search(l, 88)+1))
