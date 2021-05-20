import math

def find_fibonacci_seq_iter(n):
    if n < 2:return n 
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def find_fibonacci_seq_rec(n):
    if n < 2: return n
    return find_fibonacci_seq_rec(n - 1) + find_fibonacci_seq_rec(n - 2)

def find_fibonacci_seq_form(n):
    sq5 = math.sqrt(5)
    phi = ( 1 + sq5) / 2
    return int(math.floor(phi ** n / sq5))
    #sqrt(x) x의 제곱근을 반환합니다.
    #floor 함수는 실수를 입력하면내림하여 정수를 반환하는 함수이다. 
    #floor은 바닥을 의미한다. 실수의 바닥의 수인 바로 아래 정수로 내림


def test_find_fib():
    n = 10
    assert(find_fibonacci_seq_rec(n) == 55)
    assert(find_fibonacci_seq_iter(n) == 55)
    assert(find_fibonacci_seq_form(n) == 55)
    print("테스트 통과!!")

if __name__ == "__main__":
    test_find_fib()