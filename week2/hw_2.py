import sys
N = int(sys.stdin.readline())
result = 0
stacks = []
for i in range(N):
    num = int(input())
    if num > 0:
        stacks.append(num)
    else:
        stacks.pop()

for _ in stacks:
    result += _

print(result)