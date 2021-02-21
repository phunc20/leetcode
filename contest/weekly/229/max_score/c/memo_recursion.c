


int maximumScore(int* nums, int numsSize, int* multipliers, int multipliersSize){
  float memo[numsSize][numsSize];
  // Initialize the values in memo to empty (We choose 0.5 to represent empty)
  float empty = 0.5;
  for (int l=0; l<numsSize; l++) {
    for (int r=0; r<numsSize; r++) {
      memo[l][r] = empty;
    }
  }
  float epsilon = 1e-5;
  int in_memo(int left, int right) {
    return abs(memo[left][right] - empty) > epsilon;
  }
  // (?1) Existe-t-il Dictionary dans C?
  int recursive_dp(int left, int right)
  {
      /* left ~ right (both end included) */
      /* 0 <= left < right <= n-1         */
      if (in_memo(left, right))
        return memo[left][right];
      int n_multiplied = numsSize - (right - left + 1);
      int *remainig_multipliers = multipliers + n_multiplied;
      // Python's if len(remainig_multipliers) == 1 must be translated to the following
      int ans;
      int ll, rr;
      if (multipliersSize - n_multiplied == 1) {
        ll = *(nums+left)  * (*remainig_multipliers);
        rr = *(nums+right) * (*remainig_multipliers);
      }
      else {
        ll = *(nums+left)  * (*remainig_multipliers) + recursive_dp(left+1, right);
        rr = *(nums+right) * (*remainig_multipliers) + recursive_dp(left, right-1);
      }
      ans = ll > rr ? ll : rr;
      memo[left][right] = ans;
      return ans;
  }

  return recursive_dp(0, numsSize-1);
}







def maximumScore(nums, multipliers):
    """
    Greedy cannot give the best solution.
    Brute force with care = dynamic programming
    """
    m = len(multipliers)
    n = len(nums)
    memo = {}
    def recursive_dp(left, right):
        """
        left ~ right (both end included)
        0 <= left < right <= n-1
        """
        if (left, right) in memo:
            return memo[(left, right)]
        n_multiplied = n - (right - left + 1)
        remainig_multipliers = multipliers[n_multiplied:]
        ## Wrong (when n > m)
        #if len(remainig_multipliers) == 2:
        #    maximum = max(nums[left]*remainig_multipliers[0] + nums[right]*remainig_multipliers[1],
        #                  nums[left]*remainig_multipliers[1] + nums[right]*remainig_multipliers[0])
        # Correct: 2 is hard, down to 1.
        if len(remainig_multipliers) == 1:
            maximum = max(nums[left]*remainig_multipliers[0],
                          nums[right]*remainig_multipliers[0])
        else:
            maximum = max(nums[left]*remainig_multipliers[0] + recursive_dp(left+1, right),
                          nums[right]*remainig_multipliers[0] + recursive_dp(left, right-1))
        memo[(left, right)] = maximum
        #print(f"memo[({left}, {right})] = {maximum}")
        return maximum

    return recursive_dp(0, n-1)

