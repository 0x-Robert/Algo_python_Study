def convert_to_decimal(number, base):
    multiplier , result = 1,0

    while number > 0:
        result += number % 2 * multiplier
        #result = result + namerge 
        #result = 10^number + namerge
        # result = 1 
        # result = 1 + 0
        # result = 1 + 0
        # result = 1 +  1 * multi = 1001
        multiplier *= 10
        #multiplier = 10
        #multiplier = 100
        #multiplier = 1000
        #multiplier = 10000
        number = number // 2
        #number = 4
        #number = 2
        #number = 1
        #number = 0

    return result



def test_convert_to_decimal():
    number , base = 9 ,2
    assert(convert_to_decimal(number,base) == 1001)
    print("test 통과!!")




if __name__ == "__main__":
   test_convert_to_decimal()