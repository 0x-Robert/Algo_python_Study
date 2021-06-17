import string

def delete_unique_word(str1):
    table_c = {key:0 for key in string.ascii_lowercase}
    print("string.ascii_lowercase",string.ascii_lowercase)
    
    for i in str1:
        table_c[i] += 1
        print("i",i)
        print("table_c",table_c[i])

    for key, value in table_c.items():
        #print("table_c.items()",table_c.items())
        if value >1:
            str1 = str1.replace(key, "")
        print("str1",str1)
    return str1


def test_delete_unique_word():
    str1 = "google"
    assert(delete_unique_word(str1) == "le")
    print("테스트 통과!")

if __name__ == "__main__":
    test_delete_unique_word()
