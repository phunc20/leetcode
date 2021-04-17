#class Solution:
#    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
def getMaximumXor(nums, maximumBit):
    n = len(nums)
    answer = [0 for _ in range(n)]
    # N.B. Nobody says maximumBit > 0
    if maximumBit <= 0:
        return answer

    # From now on, we are assured maximumBit is a positive integer
    xor_int = nums[0]
    for i in range(1,n):
        xor_int ^= nums[i]
    # Decide k for each i below
    for i in range(n):
        xor_bitstr = bin(xor_int)[2:]
        n_bits = len(xor_bitstr)
        if n_bits >= maximumBit:
            #sub_xor_bitstr = xor_bitstr[-maximumBit:]
            sub_xor_int = xor_int & int("1"*maximumBit, 2)
            k = ~sub_xor_int & int("1"*(len(bin(sub_xor_int))-2), 2)
        else:
            k_bitstr = "1"*(maximumBit - n_bits) + xor_bitstr.replace("0", "2").replace("1", "0").replace("2", "1")
            k = int(k_bitstr, 2)
        answer[i] = k
        discarded = nums.pop()
        xor_int ^= discarded
    return answer


def test(nums, maximumBit, expected):
    sol = getMaximumXor(nums, maximumBit)
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
    nums = [0,1,1,3]
    maximumBit = 2
    expected = [0,3,2,3]
    test(nums, maximumBit, expected)

    test_id += 1
    print(f"testcase {test_id}")
    nums = [2,3,4,7]
    maximumBit = 3
    expected = [5,2,6,5]
    test(nums, maximumBit, expected)

    test_id += 1
    print(f"testcase {test_id}")
    nums = [0,1,2,2,5,7]
    maximumBit = 3
    expected = [4,3,6,4,6,7]
    test(nums, maximumBit, expected)


