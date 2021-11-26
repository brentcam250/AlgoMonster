

def binary_search(arr, target)
  leftPointer = 0;
  rightPointer = arr.length -1 
  while(leftPointer <= rightPointer)
    mid = (leftPointer + rightPointer)/2.foor()
    if(target > arr[rightPointer])
      leftPointer = rightPointer;
      rightPointer = arr.length- 1;
    elsif (target < arr[rightPointer])
      rightPointer = rightPointer/2.floor();
    elsif (target == arr[rightPointer])
      return rightPointer
    end
  end
end

arr = [1,3,4,6,7,45,67,86];
target = 45;
binary_search(arr, target)