'''
[Ubse Algorithm_test] Homework / week2
문제 4. 스택 카드 문제
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