

def binary_search(arr, target)
  leftPointer = 0;
  rightPointer = arr.length() -1 
  while(leftPointer <= rightPointer)
    mid = (leftPointer + rightPointer)/2.floor()
    if arr[mid] == target 
      return mid
    elsif arr[mid] < target 
      leftPointer = mid + 1
    else
      rightPointer = mid -1

    end

  end
end


arr = [1,3,4,6,7,45,67,86];
target = 45;
binary_search(arr, target)