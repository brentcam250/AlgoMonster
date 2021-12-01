// Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index. Return -1 if the target is not in the array.

// Input:

// arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
// target = 3
// Output:

// 1
// Explanation: First occurrence of 3 is at index 1.

function findFirstOccurrence(arr, target) {
  // WRITE YOUR BRILLIANT CODE HERE
  let current = 0;
  while (current <= arr.length){
    if (arr[current] === target ){
      return current;
    }else {
      current ++;
    }
  }
  return 0;
}

function splitWords(s) {
  return s == "" ? [] : s.split(' ');
}

function* main() {
  const arr = splitWords(yield).map((v) => parseInt(v));
  const target = parseInt(yield);
  const res = findFirstOccurrence(arr, target);
  console.log(res);
}

class EOFError extends Error {}
{
  const gen = main();
  const next = (line) => gen.next(line).done && process.exit();
  let buf = '';
  next();
  process.stdin.setEncoding('utf8');
  process.stdin.on('data', (data) => {
      const lines = (buf + data).split('\n');
      buf = lines.pop();
      lines.forEach(next);
  });
  process.stdin.on('end', () => {
      buf && next(buf);
      gen.throw(new EOFError());
  });
}

test = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
testT = 3
console.log(findFirstOccurrence(test, testT));