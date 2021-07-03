from collections import deque

q = deque(["버피","잰더", "윌로"])
print(q)

q.append("자일스")
print(q)

print(q.popleft())
print(q.pop())
print(q)

q.appendleft('엔젤')
print(q)

print("시프트 테스트")
print("rotate(n) 메서드는 n이 양수면 오른쪽으로 n이 음수면 왼쪽으로 시프트시킨다.")

q.rotate(1)
print(q)

q.rotate(2)
print(q)

q.rotate(3)
print(q)

q.rotate(4)
print(q)

q.rotate(-1)
print(q)

q.rotate(-2)
print(q)

#heapq.merge test
for x in heapq.merge([1,3,5], [2,4,6]):
    print(x)
    