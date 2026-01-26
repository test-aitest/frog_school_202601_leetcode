/**
 Do not return anything, modify nums in-place instead.
 */
function moveZeroes(nums: number[]): void {
  var i = 0;
  nums.forEach((num) => {
    if (num != 0) {
      nums[i] = num;
      i++;
    }
  });
  for (var j = i; j < nums.length; j++) {
    nums[j] = 0;
  }
}
