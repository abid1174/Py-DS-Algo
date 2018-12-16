def bubble_sort(L):
    n = len(L)

    for i in range(n):
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]

if __name__ == "__main__":
    L = [3, 4, 2, 9, 1, 5, 7]
    print("Before Bubble Sort: ", L)
    bubble_sort(L)
    print("After Bubble Sort: ", L)
