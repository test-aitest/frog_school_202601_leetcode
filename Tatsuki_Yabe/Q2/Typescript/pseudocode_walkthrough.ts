function validMountainArray(arr: number[]): boolean {
  var i = 1;
  while (i < arr.length && arr[i - 1] < arr[i]) {
    i++;
  }
  if (i == 1 || i == arr.length) {
    return false;
  }
  while (i < arr.length && arr[i] < arr[i - 1]) {
    i++;
  }

  return i == arr.length;
}
