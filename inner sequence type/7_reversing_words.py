def reversing_words(str1):
    words = str1.split(" ")
    print("words",words)
    rev_set = " ".join(reversed(words))
    return rev_set

def reversing_words2(str1):
    words = str1.split(" ")
    print("words",words)
    words.reverse()
    return " ".join(words)

if __name__ == "__main__":
    str1 = "파이썬 알고리즘 정말 재미있다"
    str2 = reversing_words(str1)
    str3 = reversing_words2(str1)
    print(str2)
    print(str3)