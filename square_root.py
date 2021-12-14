def square_root(n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left = 1
    right = n 
    mid = right//left
    output = left
    while left <= right:
      if (mid * mid) < n:
        output = mid
        left = mid + 1
        mid = right//left
      elif (mid * mid) > n:
        output = mid 
        right = mid -1
        mid = right//left

      elif (mid * mid) == n: 
        return mid  
        
    return output

if __name__ == '__main__':
    n = int(input())
    res = square_root(n)
    print(res)