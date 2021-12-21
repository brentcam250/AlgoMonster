from typing import List

def find_min_rotated(arr: List[int]) -> int:
    last_val = arr[-1]
    left = 0 
    right = len(arr)-1 
    boundary_index = 0
    if len(arr) == 1:
        return 0
    while (left <= right): 
      mid = (left + right) //2
      if arr[mid] <= last_val:
        right = mid-1 
        boundary_index = mid
      else:
        left = mid+1


    return boundary_index


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = find_min_rotated(arr)
    print(res)
