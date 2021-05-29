class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1, reverse=True)
        #nums2 = sorted(nums2, reverse=True)
        nums2 = sorted(nums2)
        somme = 0
        for k1 in nums1:
            if k1 in nums2:
                nums2.remove(k1)
            else:
                k2 = nums2.pop()
                somme += (k1 ^ k2)
        return somme


def test(nums1, nums2, expected):
    sol = minimumXORSum(nums1, nums2)
    if sol == expected:
        print("Congratulations!")
    else:
        print(f"sol = {sol}")
        print(f"expected = {expected}")
    print()

if __name__ == "__main__":
    test_id = 0

    test_id += 1
    print(f"testcase {test_id}")
    nums1 = [1,2]
    nums2 = [2,3]
    expected = 2
    test(nums1, nums2, expected)

    test_id += 1
    print(f"testcase {test_id}")
    nums1 = [1,0,3]
    nums2 = [5,3,4]
    expected = 8
    test(nums1, nums2, expected)
    
    test_id += 1
    print(f"testcase {test_id}")
    nums1 = [72,97,8,32,15]
    nums2 = [63,97,57,60,83]
    expected = 152
    test(nums1, nums2, expected)

