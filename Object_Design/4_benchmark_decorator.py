import random
import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        print("t",t)
        res = func(*args, **kwargs)
        print("{0} {1}".format(func.__name__, time.perf_counter()-t))
        return res

    return wrapper

#파이썬에서 코드 실행시간을 측정하는 방법을 찾아 테스트해봤습니다.
#파이썬 3.3 이상부터 perf_counter와 process_time을 사용할 수 있는데 차이점은 다음과 같습니다.

# perf_counter는 sleep 함수를 호출하여 대기한  시간을 포함하여 측정합니다. 
# process_time는 실제로 연산하는데 걸린 시간만 측정합니다. 

@benchmark
def random_tree(n):
    temp = [ n for n in range(n)]
    for i in range(n+1):
        temp[random.choice(temp)] = random.choice(temp)
    return temp


if __name__ == "__main__":
    random_tree(10000)