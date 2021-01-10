object Solution {
  def twoSum(nums: Array[Int], target: Int): Array[Int] = {
    def searchFrom(i: Int, j: Int): Array[Int] =
      if (i >= nums.length)
        Array(0,1)
      else if (j >= nums.length)
        searchFrom(i+1, i+2)
      else if ( nums(i) + nums(j) == target )
        Array(i,j)
      else
        searchFrom(i, j+1)
        
    searchFrom(0, 1)
  }
}
