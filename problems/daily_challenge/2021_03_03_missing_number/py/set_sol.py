def missingNumber(nums):
    n = len(nums)
    ## The following returns a set, not an int.
    #return set(range(n+1)) - set(nums)
    ## The following results in an error -- Python set are not indexable.
    #return (set(range(n+1)) - set(nums))[0]
    ## Note that pop() remove and return an ARBITRARY element from the set.
    ## It works here because our set contains exactly one element.
    return (set(range(n+1)) - set(nums)).pop()

def test_case(k, nums, expected):
    print(f"Test case {k:02d}")
    ans = missingNumber(nums)
    if ans == expected:
        print("Correct.")
    else:
        print(f"Incorrect. ans = {ans}, expected = {expected}")
    print()


if __name__ == "__main__":
    k = 1
    nums = [3,0,1]
    expected = 2
    test_case(k, nums, expected)

    k = 2
    nums = [0,1]
    expected = 2
    test_case(k, nums, expected)

    k = 3
    nums = [9,6,4,2,3,5,7,0,1]
    expected = 8
    test_case(k, nums, expected)

    k = 4
    nums = [0]
    expected = 1
    test_case(k, nums, expected)
