/**
 * The knows API is defined in the parent class Relation.
 * isBadVersion(version: number): boolean {
 *     ...
 * };
 */

var solution = function (isBadVersion: any) {
  return function (n: number): number {
    var left = 1;
    var right = n;

    while (left < right) {
      var mid = Math.floor((left + right) / 2);
      if (isBadVersion(mid)) {
        return mid;
      } else {
        left = mid + 1;
      }
    }

    return left;
  };
};
