#class Solution:
#    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
#        pass

"""
def areSentencesSimilar(sentence1, sentence2):
    def index_first_disagree(lang, kurz):
        for i in range(len(kurz)):
            if lang[i] != kurz[i]:
                return i
        return -1
    if len(sentence1) > len(sentence2):
        longer = sentence1
        shorter = sentence2
    else:
        longer = sentence2
        shorter = sentence1
    #if shorter in longer:
    if shorter == longer[:len(shorter)] or shorter == longer[-len(shorter):]:
        return True
    else:
        index = index_first_disagree(longer, shorter)
        print(f"index = {index}")
        minus_index = index - len(shorter)
        print(f"minus_index = {minus_index}")
        return longer[minus_index:] == shorter[index:]
"""


def areSentencesSimilar(sentence1, sentence2):
    L1 = sentence1.split()
    L2 = sentence2.split()
    def index_first_disagree(lang, kurz):
        for i in range(len(kurz)):
            if lang[i] != kurz[i]:
                return i
        return -1
    if len(L1) > len(L2):
        longer = L1
        shorter = L2
    else:
        longer = L2
        shorter = L1
    #if shorter in longer:
    if shorter == longer[:len(shorter)] or shorter == longer[-len(shorter):]:
        return True
    else:
        index = index_first_disagree(longer, shorter)
        print(f"index = {index}")
        minus_index = index - len(shorter)
        print(f"minus_index = {minus_index}")
        return longer[minus_index:] == shorter[index:]



def test(s1, s2):
    print(f"sentence1 = {s1}")
    print(f"sentence2 = {s2}")
    if areSentencesSimilar(s1, s2):
        print("Similar!!")
    else:
        print("Not similar!!")
    print()


if __name__ == "__main__":
    print("Exmaple 1")
    sentence1 = "My name is Haley"
    sentence2 = "My Haley"
    test(sentence1, sentence2)

    print("Exmaple 2")
    sentence1 = "of"
    sentence2 = "A lot of words"
    test(sentence1, sentence2)

    print("Exmaple 3")
    sentence1 = "Eating right now"
    sentence2 = "Eating"
    test(sentence1, sentence2)

    print("Exmaple 4")
    sentence1 = "Luky"
    sentence2 = "Lucccky"
    test(sentence1, sentence2)
