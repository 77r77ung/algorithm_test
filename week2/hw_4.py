'''
[Ubse Algorithm_test] Homework / week2
문제 4. 스택 카드 문제

TODO 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 올리기
'''
import sys
N = int(sys.stdin.readline())

stack = []
result = []
for _ in range(1, N+1):
    stack.append(_)

print(stack)

for i in range(N+1):
    if i == 0 or i%2 == 1:
        stack.pop()
    else:
        stack.pop()
        stack.append(i)
        
print(stack)