class Solution:
    def minPartitions(self, n: str) -> int:
        for c in "9876543210":
            if c in n:
                return int(c)


if __name__ == "__main__":
    sol = Solution()
    print(sol.minPartitions("32"))
    print(sol.minPartitions("82734"))
    print(sol.minPartitions("27346209830709182346"))
