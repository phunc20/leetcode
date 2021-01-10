## About the given python3 starting function signature

```ipython
In [1]: List[int]
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-098e96cd7034> in <module>
----> 1 List[int]

NameError: name 'List' is not defined

In [2]: class Solution:
   ...:     def twoSum(self, nums: List[int], target: int) -> List[int]:
   ...:         for i in range(len(nums)):
   ...:             for j in range(i+1, len(nums)):
   ...:                 num_i = nums[i]
   ...:                 num_j = nums[j]
   ...:                 if num_i + num_j == target:
   ...:                     return [i, j]
   ...:
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-2-476a8bd772a2> in <module>
----> 1 class Solution:
      2     def twoSum(self, nums: List[int], target: int) -> List[int]:
      3         for i in range(len(nums)):
      4             for j in range(i+1, len(nums)):
      5                 num_i = nums[i]

<ipython-input-2-476a8bd772a2> in Solution()
      1 class Solution:
----> 2     def twoSum(self, nums: List[int], target: int) -> List[int]:
      3         for i in range(len(nums)):
      4             for j in range(i+1, len(nums)):
      5                 num_i = nums[i]

NameError: name 'List' is not defined

In [3]: class Solution:
   ...:     def twoSum(self, nums: list[int], target: int) -> list[int]:
   ...:         for i in range(len(nums)):
   ...:             for j in range(i+1, len(nums)):
   ...:                 num_i = nums[i]
   ...:                 num_j = nums[j]
   ...:                 if num_i + num_j == target:
   ...:                     return [i, j]
   ...:
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-2d8f113a9fa7> in <module>
----> 1 class Solution:
      2     def twoSum(self, nums: list[int], target: int) -> list[int]:
      3         for i in range(len(nums)):
      4             for j in range(i+1, len(nums)):
      5                 num_i = nums[i]

<ipython-input-3-2d8f113a9fa7> in Solution()
      1 class Solution:
----> 2     def twoSum(self, nums: list[int], target: int) -> list[int]:
      3         for i in range(len(nums)):
      4             for j in range(i+1, len(nums)):
      5                 num_i = nums[i]

TypeError: 'type' object is not subscriptable

In [4]: class Solution:
   ...:     def twoSum(self, nums: list, target: int) -> list:
   ...:         for i in range(len(nums)):
   ...:             for j in range(i+1, len(nums)):
   ...:                 num_i = nums[i]
   ...:                 num_j = nums[j]
   ...:                 if num_i + num_j == target:
   ...:                     return [i, j]
   ...:

In [5]:
```
