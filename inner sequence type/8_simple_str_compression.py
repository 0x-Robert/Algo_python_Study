def str_compression(s):
    count, last = 1, ""
    list_aux = []
    for i, c in enumerate(s):
        #반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
        #인덱스 번호와 컬렉션의 원소를 tuple형태로 반환합니다.
        print("i",i)
        print("c",c)
        print("last",last)
        print("count",count)
        if last == c:
            count += 1
        else:
            if i != 0:
                list_aux.append(str(count))
            list_aux.append(c)
            print("list_aux",list_aux)
            count = 1
            last = c
    list_aux.append(str(count))
    print("list_aux",list_aux)
    return "".join(list_aux)

if __name__ == "__main__":
    result = str_compression("aabcccccaaa")
    print(result)