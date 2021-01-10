object Solution {
  def twoSum(nums: Array[Int], target: Int): Array[Int] = {
    var ans = Array(0,1)
    for (i <- 0 until nums.length) {
      for (j <- i+1 until nums.length) {
        if (nums(i)+nums(j) == target) {
          //val ans = Array(i, j)
          ans = Array(i, j)
        }
      }
    }
    ans
  }
}



object Solution {
  def twoSum(nums: Array[Int], target: Int): Array[Int] = {
    //var ix_left = 0
    var ans = Array(1,2)
    for (i <- 0 until nums.length) {
      for (
        j <- 0 until nums.length;
        if j > i;
        if nums(i)+nums(j) == target
      ) {
        //val ans = Array(i, j)
        ans = Array(i, j)
      }
    }
    ans
  }
}
