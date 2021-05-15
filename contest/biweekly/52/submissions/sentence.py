class Solution:
    def sortSentence(self, s: str) -> str:
        D = {}
        for word_i in s.split():
            i = int(word_i[-1])
            word = word_i[:-1]
            D[i-1] = word
        sentence = ""
        for i in range(len(D)):
            sentence += f"{D[i]} "
        return sentence.rstrip()

def test(s, expected):
    sol = sortSentence(s)
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
    s = "is2 sentence4 This1 a3"
    expected = "This is a sentence"
    test(s, expected)

    test_id += 1
    print(f"testcase {test_id}")
    s = "Myself2 Me1 I4 and3"  
    expected = "Me Myself and I"
    test(s, expected)
    


