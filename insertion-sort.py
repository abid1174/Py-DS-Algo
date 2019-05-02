"""
Insertion sort implementation
"""

print("Enter the elements: ")

elements = list(map(int, input().split(" ")))

for i in range(len(elements)): 
    j = i
    while j > 0 and elements[j] < elements[j-1]:
        elements[j], elements[j-1] = elements[j-1], elements[j]
        j = j-1

print(elements)