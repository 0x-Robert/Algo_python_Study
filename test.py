# # from fractions import Fraction

# # def rounding_floats(number1, places):
# #     return round(number1, places)

# # def float_to_fractions(number):
# #     return Fraction(*number.as_integer_ratio())

# # def get_denominator(number1, number2):
# #     """ 분모를 반환한다."""
# #     a = Fraction(number1, number2)
# #     return a.denominator

# # def get_numerator(number1,number2):
# #     """ 분자를 반환한다."""
# #     a = Fraction(number1, number2)
# #     return a.numerator

# # def test_testing_floats():
# #     number1 = 1.25
# #     number2 = 1
# #     number3 = -1
# #     number4 = 5/4
# #     number6 = 6
# #     assert(rounding_floats(number1,number2) == 1.2)
# #     assert(rounding_floats(number1*10, number3) == 10)
# #     assert(float_to_fractions(number1) == number4)
# #     assert(get_denominator(number2, number6) == number6)
# #     assert(get_numerator(number2, number6) == number2)
# #     print("테스트 통과!")


# # if __name__ == "__main__":aadsf
# #     test_testing_floats()

# #"{} {} {}".format("파이썬","자료구조","알고리즘")
# # print("{} {} {}".format("파이썬","자료구조","알고리즘"))


# # import decimal
# # a= "{0} {0!s} {0!r} {0!a}".format(decimal.Decimal("99.9"))
# # print(a)


# # hero="버피"
# # number=999

# # b="{number}: {hero}".format(**locals())
# # print(b)


# # slayers="버피*크리스-메리*16"
# # fields = slayers.split("*")
# # print(fields)
# # job=fields[1].split("-")
# # print(job)


# #문자열 제거하


# # def erase_space_from_String(string):
# #     s1 = string.split(" ")
# #     s2 = "".join(s1)
# #     return s2
# # c = erase_space_from_String("asdf asdfs bbbb dddd")
# # print(c)


# # slayers = ["버피","앤","아스틴"]
# # b= " ".join(slayers)
# # print(b)

# name = "프레드"
# testa = f"그의 이름은{name!r}입니다."
# print(testa)

# testb = f"그의 이름은{repr(name)}입니다." #repr()은 !r과 같다.
# print(testb)

# import decimal
# width=152
# precision = 4
# #value = decimal.Decimal("12.34567")
# #value = decimal.Decimal("12.534567")
# value = decimal.Decimal("12.135567")
# testc= f"결과: {value:{width}.{precision}}"
# print(testc)
# print(value) 


# def example_args(a,b,c):
#     return a * b * c #여기에서 *연산자는 곱셈이다.
# L=[2,3,4]
# a=example_args(*L)
# print("a", a)

# b=example_args(2,*L[1:])
# print("b",b)


# a = [ y for y in range(1900,1940) if y%4 == 0]
# print("a",a)

# b = [2 ** i for i in range(13)]
# print("b",b)

# c = [x for x in a if x%2==0]
# print("c",c)

# d = [str(round(355/113.0,i) for i in range(1,6))]
# print("d",d)

# words = 'Buffy is awesome and vampire slayer'.split()
# e = [[w.upper(), w.lower(), len(w) ] for w in words] 
# for i in e:
#         print(i)


# def test():
#     result = []
#     for x in range(10):
#         for y in range(5):
#             if x * y > 10:
#                 result.append((x,y))
#                 print("result",result)

#     for x in range(5):
#         for y in range(5):
#             if x != y:
#                 for z in range(5):
#                     if y != z:
#                         yield (x, y, z)
#                         # print("x,y,z",x,y,z)


#     return ((x, complicated_transform(x))
#             for x in long_generator_function(parameter)
#             if x is not None)
            

#     squares = [ x * x for x in range(10)]

#     eat(jelly_bean for jelly_bean in jelly_beans
#         if jelly_bean.color == 'black')


# if __name__ == "__main__":
#     test()
# # for i in [1, 2, 3]:
#     yield i

# def test2():
#     result = [(x,y) for x in range(10) for y in range(5) if x * y > 10]
#     print("result",result)
#     return ((x,y,z)
#             for x in xrange(5)
#             for y in xrange(5)
#             if x != y
#             for z in xrange(5)
#             if y != z)

# test2()

# def test1():
#     l = []
#     for i in range(1000):
#         l = l + [i]
#         #print("l",l)

# def test2():
#     l = []
#     for i in range(1000):
#         l.append(i)

# def test3():
#     l = [i for i in range(1000)]

# def test4():
#     l = list(range(1000))

# if __name__ == "__main__":
#     import timeit
#     t1 = timeit.Timer("test1()", "from __main__ import test1")
#     print("concat",t1.timeit(number=1000),"milliseconds")
#     t2 = timeit.Timer("test2()","from __main__ import test2")
#     print("append", t2.timeit(number=1000),"milliseconds")
#     t3 = timeit.Timer("test3()", "from __main__ import test3")
#     print("comprehension ", t3.timeit(number=1000), "milliseconds")
#     t4 = timeit.Timer("test4()", "from __main__ import test4")
#     print("list range", t4.timeit(number=1000), "milliseconds")

# blist = [1,2,3,255]
# the_bytes = bytes(blist)
# print(the_bytes)

# the_byte_array = bytearray(blist)
# print(the_byte_array)

# #the_bytes[1]=127 #불변
# #print(the_bytes)

# the_byte_array[1]=127 #가변(mutable)
# print(the_byte_array)


# x1 = 4
# 1 << x1
# print("x1",x1)

# x2 = 8
# a = x2 & (x2-1)
# print("a",a)

# x3 = 6
# b = x3 & (x3-1)
# print("b",b)



# def revert(s):
#     if s:
#         s = s[-1] + revert(s[:-1])
#     return s

# def revert2(string):
#     return string[::-1]

# if __name__ == "__main__":
#     str1 = "안녕 세상!"
#     str2 = revert(str1)
#     str3 = revert2(str1)
#     print(str2)
#     print(str3)



#a = 2
a=""
b = a or 3
print("b",b)