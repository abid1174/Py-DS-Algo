def selection_sort(L):
    n = len(L)

    for i in range(n-1):
        index_min = i

        for j in range(i+1, n):
            if L[j] < L[index_min]:
                index_min = j
        
        if index_min != i:
            L[i], L[index_min] = L[index_min], L[i]


if __name__ == "__main__":
    L = [6, 4, 3, 9, 2, 1]
    print("Before sort: ", L)
    selection_sort(L)
    print("After sort: ", L)
