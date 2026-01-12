function maxArea1(height: number[]): number {
  var maxarea = 0;
  var n = height.length;

  for (var p1 = 0; p1 < n; p1++) {
    for (var p2 = p1 + 1; p2 < n; p2++) {
      let length = Math.min(height[p1], height[p2]);
      let width = p2 - p1;
      let area = length * width;
      maxarea = Math.max(maxarea, area);
    }
  }

  return maxarea;
}
