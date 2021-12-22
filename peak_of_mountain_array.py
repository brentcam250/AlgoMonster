from typing import List

def peak_of_mountain_array(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left = 0
    right = len(arr)-1
    boundary_index = -1
    while (left <= right ): 
      mid = left // right
      if arr[mid] > arr[mid+1]:
        # descending move right pointer left 
        boundary_index = mid 
        right = mid -1 

      else:
        #ascending move left pointer right 
        left = mid + 1

    return boundary_index

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = peak_of_mountain_array(arr)
    print(res)