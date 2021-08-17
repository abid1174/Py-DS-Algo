"""
Jump Search implementation with Python3
Step 1: Sort the Array.
Step 2: Find the jump block --> sqrt(Array length)
Step 3: Iterate while the value is greater than the target
Step 4: Back a step and Linear search from previous step to next step
"""
import math


def jump_search(arr, target):
    length = len(arr)
    sorted_arr = sorted(arr)

    # Finding block size to be jumped
    step = math.sqrt(length)

    # Finding the block in between the target exists
    prev = 0
    while sorted_arr[int(min(step, length))-1] < target:
        prev = step
        step += math.sqrt(length)

        if prev >= length:
            return -1
    
    # Linear search inside the block
    while sorted_arr[int(prev)] < target:
        prev += 1

        # If we reached next block or end
        # of array, element is not present.
        if prev == min(step, length):
            return -1
    
    if sorted_arr[int(prev)] == target:
        return prev

    return -1



if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    target = 610

    # find the index of target using jump search 
    index = jump_search(arr, target)

    print("Number", target, "is at index", "%.0f"%index)

