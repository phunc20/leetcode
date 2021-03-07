qualified = {1, 3, 4, 9}
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n in qualified:
            return True
        remainder = n % 3
        if remainder == 2:
            return False
        #elif remainder == 1:
        #    reduced = (n-1) // 3
        #    if checkPowersOfThree(reduced):
        #        qualified.add(reduced)
        #        return True
        #    else:
        #        return False
        else:
            reduced = (n-remainder) // 3
            if self.checkPowersOfThree(reduced):
                qualified.add(reduced)
                return True
            else:
                return False

