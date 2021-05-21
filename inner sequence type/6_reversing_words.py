def reversing_words_slice(word):
    new_word = []
    words = word.split(" ")
    print("words[::-1]",words[::-1])
    for word in words[::-1]:
       
        print("word",word)
        new_word.append(word)
    print("new_word",new_word)
    b = "".join(new_word)
    print("b",b)
    return " ".join(new_word)
    
if __name__ == "__main__":
    str1 = "파이썬 알고리즘 정말 재미있다."
    str2 = reversing_words_slice(str1)
    print(str2)
