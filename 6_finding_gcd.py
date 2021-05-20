
def finding_gcd(a, b):
    while (b != 0):
        result = b
        a, b = b, a % b
        print('a',a)
        print('b',b)
        print('result',result)
    return result


def test_finding_gcd():
    number1 = 21
    number2 = 12
    assert(finding_gcd(number1, number2) == 3)
    print("테스트 통과")

if __name__ == "__main__":
    test_finding_gcd()