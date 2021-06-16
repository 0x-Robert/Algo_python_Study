from collections import Counter


def counter_example():
    """항목의 발생 횟수를 매핑하는 딕셔너리를 생성한다."""
    seq1=[1,2,3,5,1,2,5,5,2,5,1,4]
    seq_counts=Counter(seq1)
    print("seq_counts : Counter(seq1) ",seq_counts)

    """항목의 발생 횟수를 수동적으로 갱신하거나, update()메서드를 사용할 수 있다."""
    seq2 = [1,2,3]
    seq_counts.update(seq2)
    print("seq_counts.update(seq2)",seq_counts)

    seq3 = [1,4,3]
    for key in seq3:
        seq_counts[key]+=1
    print("seq_counts[key]+=1",seq_counts)


    """ a+b, a-b 같은 연산을 사용할 수 있다."""

    seq_counts_2= Counter(seq3)
    print("seq_counts_2", seq_counts_2)
    print("seq_counts + seq_counts_2",seq_counts + seq_counts_2)
    print("seq_counts - seq_counts_2",seq_counts - seq_counts_2)

if __name__ == "__main__":
    counter_example()
