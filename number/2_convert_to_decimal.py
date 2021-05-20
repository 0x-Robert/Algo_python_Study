def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    #multiplier = 1 , result=0
    while number > 0:
        result += number % 10 * multiplier # % = 나머지 
        #result = 1 one
        #result = 1 two
        #result = 1 three
        #result = 9 four
        multiplier *= base
        #base = 2
        #multiplier = 2 one
        #multiplier = 4  two
        #multiplier = 8 three
        #multiplier = 16 four
        number = number // 10 #  // = 몫
        #number = 100
        #number = 10
        #number = 1
        #number = 0

        
    print('multiplier',multiplier)
    print("result",result)
    return result

def test_convert_to_decimal():
    number , base = 1001, 2
    assert(convert_to_decimal(number,base) == 9)
    print("테스트 통과!")

if __name__ == "__main__":
    test_convert_to_decimal()