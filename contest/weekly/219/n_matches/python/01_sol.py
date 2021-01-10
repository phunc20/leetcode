class Solution:
    def numberOfMatches(self, n: int) -> int:
        n_matches = 0
        n_survivals = n
        while n_survivals > 1:
            half = n_survivals // 2
            n_matches += half
            n_survivals = half + n_survivals % 2
        return n_matches


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfMatches(7))
    print(sol.numberOfMatches(14))
