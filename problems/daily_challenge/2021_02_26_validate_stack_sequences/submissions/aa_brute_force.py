class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        length = len(pushed)
        i = 0
        L = []
        for j, entier in enumerate(popped):
            coincide = False
            while not coincide:
                last = L[-1] if len(L) != 0 else None
                if entier == last:
                    L.pop()
                    coincide = True
                else:
                    if i >= length:
                        return False
                    else:
                        L.append(pushed[i])
                        i += 1
        return True

"""


        coincide = False
        while True:
            if pushed[i] != entier:
                L.append(pushed[i])
                i += 1
            else:
"""


def example(id_, pushed, popped, expected):
    print(f"Example {id_}")
    output = validateStackSequences(pushed, popped)
    if  output == expected:
        print("Correct")
    else:
        print(f"Incorrect. pushed = \"{pushed}\", popped = \"{popped}\", output = {output}, expected = {expected}")


if __name__ == "__main__":
    example(id_=1, pushed=[1,2,3,4,5], popped=[4,5,3,2,1], expected=True)
    example(id_=2, pushed=[1,2,3,4,5], popped=[4,3,5,1,2], expected=False)
