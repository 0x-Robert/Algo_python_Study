def convert_dec_to_any_base_rec(number, base):
    convertString = "0123456789ABCDEF"
    print("number",number)
    print("base",base)
   
    if number < base:
        print("if")
        return convertString[number]
    else:
        print("else")
        return convert_dec_to_any_base_rec(number // base, base)\
            + convertString[number % base]
       

def test_convert_dec_to_any_base_rec():
    number = 9 
    base = 2
    assert(convert_dec_to_any_base_rec(number,base) == "1001")
    print("테스트 통과!")


if __name__ == "__main__":
    test_convert_dec_to_any_base_rec()
