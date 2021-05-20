import string
import sys

    #입력한 파일에서 사용한 단어를 추출하는 스크립트
    #string.whitespace 공백으로 간주하는 모든 ASCII 문자를 포함하는 문자열. # 여기에는 스페이스, 탭, 줄 바꿈, 캐리지 리턴, 세로 탭 및 폼 피드 문자가 포함됩니다.
    #string.puctuation C 로케일에서 구두점 문자로 간주하는 ASCII 문자의 문자열: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
    #string.digits 문자열 '0123456789'.

def count_unique_word():
    words = {}
    print('words',words)
    strip = string.whitespace + string.punctuation + string.digits + "\"'"
    
    print('strip',strip)
    for filename in sys.argv[1:]:
        with open(filename,  encoding='UTF8') as file:
            for line in file:
                print('line',line)
                for word in line.lower().split():
                    word = word.strip(strip)
                    print('word',word)
                    if len(word) > 2:
                        words[word] = words.get(word,0) + 1
                        #사용한 워드 빈도수 세기 
                        print('words.get : ',  words[word] )

    for word in sorted(words):
        print("{0}: {1}번".format(word, words[word]))
    #sorted() 오름차순 정렬
if __name__ == "__main__":
   count_unique_word()
