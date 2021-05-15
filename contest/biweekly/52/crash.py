#class Solution:
#    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        
def memLeak(memory1, memory2):
    i = 1
    #while memory1 >= i or memory2 >= i:
        #max_ = memory2 if memory2 > memory1 else memory1
    while True:
        if memory2 > memory1:
            if memory2 < i:
                return [i, memory1, memory2]
            else:
                memory2 -= i
        else:
            if memory1 < i:
                return [i, memory1, memory2]
            else:
                memory1 -= i
        i += 1


def test(memory1, memory2, expected):
    sol = memLeak(memory1, memory2)
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
    memory1 = 2
    memory2 = 2
    expected = [3,1,0]
    test(memory1, memory2, expected)

    test_id += 1
    print(f"testcase {test_id}")
    memory1 = 8
    memory2 = 11
    expected = [6,0,4]
    test(memory1, memory2, expected)
    


