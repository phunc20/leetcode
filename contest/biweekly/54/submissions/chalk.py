class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # loop thru the list `chalk` one time first,
        # to know its sum.
        somme = 0
        for i, n_i in enumerate(chalk):
            k -= n_i
            if k < 0:
                return i
            somme += n_i
        k %= somme
        # k < somme for sure now.
        for i, n_i in enumerate(chalk):
            k -= n_i
            if k < 0:
                return i

def test(chalk, k, expected):
    sol = chalkReplacer(chalk, k)
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
    chalk = [5,1,5]
    k = 22
    expected = 0
    test(chalk, k, expected)

    test_id += 1
    print(f"testcase {test_id}")
    chalk = [3,4,1,2]
    k = 25
    expected = 1
    test(chalk, k, expected)
    



