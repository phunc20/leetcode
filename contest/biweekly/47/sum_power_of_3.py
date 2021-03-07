#class Solution:
#    def checkPowersOfThree(self, n: int) -> bool:
        
#def checkPowersOfThree(n):
#    def divisible_by_3(k):
#        return k % 3 == 0
#    #if 1 <= n <= 2:
#    if n == 2:
#        return False
#    if divisible_by_3(n):
#        return checkPowersOfThree(n//3)
#    else:
#        n = n - 1
#        if divisible_by_3(n):
#            return checkPowersOfThree(n//3)
#        else:
#            return False

qualified = {1, 3, 4, 9}
def checkPowersOfThree(n):
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
        if checkPowersOfThree(reduced):
            qualified.add(reduced)
            return True
        else:
            return False



if __name__ == "__main__":
    n = 12
    print(f"{checkPowersOfThree(n)}")
    n = 91
    print(f"{checkPowersOfThree(n)}")
    n = 21
    print(f"{checkPowersOfThree(n)}")
