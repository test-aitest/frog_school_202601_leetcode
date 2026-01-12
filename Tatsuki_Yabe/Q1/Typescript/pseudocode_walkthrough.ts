function maxArea2(height: number[]): number {
  var l = 0;
  var r = height.length - 1;
  var maxarea = 0;

  while (l < r) {
    let length = Math.min(height[l], height[r]);
    let wigth = r - l;
    let area = length * wigth;
    maxarea = Math.max(maxarea, area);

    if (height[l] < height[r]) {
      l++;
    } else {
      r--;
    }
  }

  return maxarea;
}
