from collections import Counter

def find_top_N_recurring_words(seq,N):
    dcounter = Counter()
    for word in seq.split():
        dcounter[word] += 1
    return dcounter.most_common(N)

def test_find_top_N_recurring_words():
    seq = "버피 에인절 몬스터 잰더 윌로 버피 몬스터 슈퍼 버피 에인절"
    N=3
    assert(find_top_N_recurring_words(seq,N) == [("버피",3), ("에인절",2), ("몬스터",3)])
    print("테스트 통과")

if __name__ == "__main__":
    test_find_top_N_recurring_words()

    