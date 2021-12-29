from typing import List


# min days = 1 if truck capacity is sum weights
# max days = len(weights), if the truck capacity is the largest single package, and no two packages can fit together.
def can_ship_in_days(weights: List[int], max_weight: int,  d: int) -> int:
  req_days = 1
  capacity = max_weight
  i = 0
  n = len(weights)
  while i < n :
    if weights[i]<= capacity:
      capacity -= weights[i];
      i+=1
    else:
      req_days += 1
      capacity = max_weight

  
  return req_days <= d 

def min_max_weight(weights: List[int], d: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left = max(weights) #smallest possible capacity is just the single largest package
    right = sum(weights) #largest necessary is a truck that can carry all packages
    # truckSize = 0
    boundary_index = right
    while left <= right: 
      mid = (left + right)//2
      if can_ship_in_days(weights, mid, d):
        boundary_index = mid
        right = mid -1 
      else:
        left = mid + 1

    return boundary_index



if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    d = int(input())
    res = min_max_weight(weights, d)
    print(res)