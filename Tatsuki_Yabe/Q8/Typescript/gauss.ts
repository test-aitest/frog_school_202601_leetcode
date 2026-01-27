function missingNumber2(nums: number[]): number {
  var n = nums.length;
  var intendedSum = (n * (n + 1)) / 2;
  var actualSum = 0;

  for (const num of nums) {
    actualSum += num;
  }

  return intendedSum - actualSum;
}
