function missingNumber(nums: number[]): number {
  var numsMap = new Map<number, boolean>();
  var output = 0;
  nums.forEach((num) => {
    numsMap.set(num, true);
  });

  for (var i = 1; i <= nums.length; i++) {
    if (!numsMap.get(i)) {
      output = i;
    }
  }

  return output;
}
