object Solution {
  def twoSum(nums: Array[Int], target: Int): Array[Int] = {
    var i = 0
    var found = false
    var ans = Array(0,1)
    while (i < nums.length && !found) {
      var j = i + 1
      while (j < nums.length && !found) {
        if ( nums(i) + nums(j) == target ) {
          ans = Array(i, j)
          found = true
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
