#구글 파이썬 스타일 가이드
#좋은 예
items=['<table>']
for last_name, first_name in employee_list:
    items.append('<tr><td>%s,%s</td></tr>' %(last_name,first_name))
    items.append('</table>')
    employee_table=''.join(items)

# 나쁜 예
employee_table = '<table>'
for last_name, first_name in employee_list:
    employee_table += '<tr><td>%s, %s</td></tr>' % (last_name, first_name)
    employee_table += '</table>'


#########################
#cProfile 테스트
import cProfile
import time

def sleep():
    time.sleep(5)

def hello_world():
    print("Hello World!")

def main():
    sleep()
    hello_world()

cProfile.run('main()')


#########################
#실행시간 측정
import timeit
print(timeit.timeit("x = 2+2"))
print(timeit.timeit("x = sum(range(10))"))


