from collections import Counter

def is_anagram(s1,s2):
    counter = Counter()
    print("counter",counter)
    for c in s1:
        counter[c] += 1
        print("+=c : ",c)
        print("counter[c]1:",counter[c])
    for c in s2:
        counter[c] -= 1
        print("-=c : ", c)
        print("counter[c]2:",counter[c])
    for i in counter.values():
        if i:
            print("for i in counter.values",i)
            print("counter.values",counter.values())
            return False
    return True

def test_is_anagram():
    s1 = "marina"
    s2 = "aniram"
    assert(is_anagram(s1,s2) is True)
    s1 = "google"
    s2 = "gouglo"
    assert(is_anagram(s1,s2) is False)
    print("테스트 통과")

if __name__ == "__main__":
    test_is_anagram()

