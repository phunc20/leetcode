#class Solution:
#    def mergeAlternately(self, word1: str, word2: str) -> str:
        
def mergeAlternately(word1, word2):
    #merged = " " * (len(word1) + len(word2))
    merged = [None] * (len(word1) + len(word2))
    minimum = min(len(word1), len(word2))
    for i in range(minimum):
        #merged.extend([word1[i], word2[i]])
        merged[2*i] = word1[i]
        merged[2*i + 1] = word2[i]
    if minimum < len(word1):
        merged[2*minimum:] = list(word1[minimum:])
    elif minimum < len(word2):
        merged[2*minimum:] = list(word2[minimum:])
    #for i, c in enumerate(word1):
    #    merged[2*i] = c
    #merged = " " * (len(word1) + len(word2))
    #while True:
    return "".join(merged)


if __name__ == "__main__":
    word1 = "ab"
    word2 = "pqrs"
    print(mergeAlternately(word1, word2))
