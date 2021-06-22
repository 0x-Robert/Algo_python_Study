# def append(number,number_list=[]):
#     number_list.append(number)
#     return number_list

# print("예상결과[5]",append(5)) 
# print("예상결과[5,2]",append(7)) 
# print("예상결과[5,2,7]",append(2)) 


# def append(number,number_list=None):
#     if number_list is None:
#         number_list = []

#     number_list.append(number)
#     return number_list

# print("append[5]",append(5))
# print("append[7]",append(7))
# print("append[2]",append(2))


# import sys

# def main():
#     for arg in sys.argv[1:]:
#         print(arg)


# if __name__ == "__main__":
#     main()

# x = int(input("숫자를 입력하세요:"))
# if x < 0:
#     x =0 
#     print("음수를 입력하여 x를 0으로 변경했습니다.")
# elif x == 0:
#     print("0이 입력되었습니다.")
# elif x == 1:
#     print("1이 입력되었습니다.")
# else:
#     print("2이상의 숫자가 입력되었습니다.")



# if not users:
#     print("사용자가 없습니다.")

# if foo ==0:
#     handle_zero()

# if i % 10 == 0:
#     handle_multiple_of_ten()


# if len(users) == 0:
#     print("사용자가 없습니다.")


# if foo is not None and not foo:
#     handle_zero()


# if not i % 10:
#     handle_multiple_of_ten()

# a = [1,2,3]
# def f(a):
#     while a:
#         print("a.pop()",a.pop())
#         yield a.pop()

# f(a)


# def fib_generator():
#     a,b = 0,1
#     while True:
#         yield b
#         a, b = b, a+b

# if __name__ == "__main__":
#     fib = fib_generator()
#     print(next(fib))
#     print(next(fib))
#     print(next(fib))
#     print(next(fib))
#     print(next(fib))
#     print(next(fib))
#     print(next(fib))


# for i in range(10):
#     if i == 4:
#         break
#     print(i)
# else:
#     print("for 문 종료")



# for i in range(10):
#     if i % 2 ==0:
#         continue
#     print(i)
# else:
#     print("for 문 종료!")

# a = range(10)
# b = range(4,10)
# c = range(0,10,3)
# print("a",a)
# print("b",b)
# print("c",c)

# def cube(x): return x*x*x
# print("a: ",list(map(cube,range(1,11))))

# seq = range(8)
# def square(x): return x*x
# print("b:" ,list(zip(seq,map(square,seq))))


# def area(b,h):
#     return 0.5 * b * h
# print("Area",area(5,4))


# area2= lambda b,  h : 0.5 * b *h
# print("Area2",area2(5,4))


# import collections 
# minus_one_dict = collections.defaultdict(lambda:-1)
# point_zero_dict =  collections.defaultdict(lambda: (0,0))
# message_dict = collections.defaultdict(lambda:"No message")

# print("minus_one_dict",minus_one_dict)
# print("point_zero_dict",point_zero_dict)
# print("message_dict",message_dict)